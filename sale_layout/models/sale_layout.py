# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import api
from openerp.osv import osv, fields
from itertools import groupby


def grouplines(self, ordered_lines, sortkey):
    """Return lines from a specified invoice or sale order grouped by category"""
    grouped_lines = []
    for key, valuesiter in groupby(ordered_lines, sortkey):
        group = {}
        group['category'] = key
        group['lines'] = list(v for v in valuesiter)

        if 'subtotal' in key and key.subtotal is True:
            group['subtotal'] = sum(line.price_subtotal for line in group['lines'])
        grouped_lines.append(group)

    return grouped_lines


class SaleLayoutCategory(osv.Model):
    _name = 'sale_layout.category'
    _order = 'sequence, id'
    _columns = {
        'name': fields.char('Name', required=True, translate=True),
        'sequence': fields.integer('Sequence', required=True),
        'subtotal': fields.boolean('Add subtotal'),
        'separator': fields.boolean('Add separator'),
        'pagebreak': fields.boolean('Add pagebreak')
    }

    _defaults = {
        'subtotal': True,
        'separator': True,
        'pagebreak': False,
        'sequence': 10
    }


class AccountInvoice(osv.Model):
    _inherit = 'account.invoice'

    def sale_layout_lines(self, cr, uid, ids, invoice_id=None, context=None):
        """
        Returns invoice lines from a specified invoice ordered by
        sale_layout_category sequence. Used in sale_layout module.

        :Parameters:
            -'invoice_id' (int): specify the concerned invoice.
        """
        ordered_lines = self.browse(cr, uid, invoice_id, context=context).invoice_line_ids
        # We chose to group first by category model and, if not present, by invoice name
        sortkey = lambda x: x.sale_layout_cat_id if x.sale_layout_cat_id else ''

        return grouplines(self, ordered_lines, sortkey)


import openerp

class AccountInvoiceLine(osv.Model):
    _inherit = 'account.invoice.line'
    _order = 'invoice_id, categ_sequence, sequence, id'

    sale_layout_cat_id = openerp.fields.Many2one('sale_layout.category', string='Section')
    categ_sequence = openerp.fields.Integer(related='sale_layout_cat_id.sequence',
                                            string='Layout Sequence', store=True)

class SaleOrder(osv.Model):
    _inherit = 'sale.order'

    def sale_layout_lines(self, cr, uid, ids, order_id=None, context=None):
        """
        Returns order lines from a specified sale ordered by
        sale_layout_category sequence. Used in sale_layout module.

        :Parameters:
            -'order_id' (int): specify the concerned sale order.
        """
        ordered_lines = self.browse(cr, uid, order_id, context=context).order_line
        sortkey = lambda x: x.sale_layout_cat_id if x.sale_layout_cat_id else ''

        return grouplines(self, ordered_lines, sortkey)


class SaleOrderLine(osv.Model):
    _inherit = 'sale.order.line'
    _columns = {
        'sale_layout_cat_id': fields.many2one('sale_layout.category',
                                              string='Section'),
        'categ_sequence': fields.related('sale_layout_cat_id',
                                         'sequence', type='integer',
                                         string='Layout Sequence', store=True)
        #  Store is intentionally set in order to keep the "historic" order.
    }

    _order = 'order_id, categ_sequence, sale_layout_cat_id, sequence, id'

    def _prepare_order_line_invoice_line(self, cr, uid, line, account_id=False, context=None):
        """Save the layout when converting to an invoice line."""
        invoice_vals = super(SaleOrderLine, self)._prepare_order_line_invoice_line(cr, uid, line, account_id=account_id, context=context)
        if line.sale_layout_cat_id:
            invoice_vals['sale_layout_cat_id'] = line.sale_layout_cat_id.id
        if line.categ_sequence:
            invoice_vals['categ_sequence'] = line.categ_sequence
        return invoice_vals

    @api.multi
    def _prepare_invoice_line(self, qty):
        """
        Prepare the dict of values to create the new invoice line for a sales order line.

        :param qty: float quantity to invoice
        """
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        if self.sale_layout_cat_id:
            res['sale_layout_cat_id'] = self.sale_layout_cat_id.id
        return res


    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        if not self.product_id:
            return {'domain': {'product_uom': []}}

        vals = {}
        domain = {'product_uom': [('category_id', '=', self.product_id.uom_id.category_id.id)]}
        if not self.product_uom or (self.product_id.uom_id.id != self.product_uom.id):
            vals['product_uom'] = self.product_id.uom_id
            vals['product_uom_qty'] = 1.0

        product = self.product_id.with_context(
            lang=self.order_id.partner_id.lang,
            partner=self.order_id.partner_id.id,
            quantity=vals.get('product_uom_qty') or self.product_uom_qty,
            date=self.order_id.date_order,
            pricelist=self.order_id.pricelist_id.id,
            uom=self.product_uom.id
        )

        name = product.name_get()[0][1]
        if product.description_sale:
            name += '\n' + product.description_sale
        vals['name'] = name        

        self._compute_tax_id()

        if self.order_id.pricelist_id and self.order_id.partner_id:
            vals['price_unit'] = self.env['account.tax']._fix_tax_included_price(product.price, product.taxes_id, self.tax_id)
        self.update(vals)


        if product.type:
            if product.type == "product":
                self.update({"sale_layout_cat_id": 1})
            elif product.type == "service":
                self.update({"sale_layout_cat_id": 2})

        return {'domain': domain}


class ProductSetAdd(models.TransientModel):
    _inherit = 'product.set.add'


    def prepare_sale_order_line_data(self, sale_order_id, set, set_line,
                                     max_sequence=0):
        if set_line.product_id.type:
            if set_line.product_id.type == "product":
                ## Kikihi = 1  self.update({"sale_layout_cat_id": 1})
                layout = 1
            elif set_line.product_id.type == "service":
                ## Sekouhi = 2 self.update({"sale_layout_cat_id": 2})
                layout = 2


        return {
            'order_id': sale_order_id,
            'product_id': set_line.product_id.id,
            'product_uom_qty': set_line.quantity * self.quantity,
            'product_uom': set_line.product_id.uom_id.id,
            'sequence': max_sequence + set_line.sequence,
            'sale_layout_cat_id': layout 
        }
