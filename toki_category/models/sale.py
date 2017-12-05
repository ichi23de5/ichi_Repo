# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
from itertools import groupby

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    ### categoly subtotal with sale.layout ###
    product_subtotal = fields.Monetary('Product Subtotal', store=False, readonly=True, compute='_compute_subtotal')
    service_subtotal = fields.Monetary('Service Subtotal', store=False, readonly=True, compute='_compute_subtotal')
    discount_subtotal = fields.Monetary('Discount Subtotal', store=False, readonly=True, compute='_compute_subtotal')
    other_subtotal = fields.Monetary('Other Subtotal', store=False, readonly=True, compute='_compute_subtotal')


    @api.onchange('order_line')
    def _compute_subtotal(self):
        self.ensure_one()
        datas = 0
        datas2 = 0
        datas3 = 0
        datas4 = 0
        for category, lines in groupby(self.order_line, lambda l: l.sale_layout_cat_id):
            for c_line in lines:
                if c_line.sale_layout_cat_id.id == 1:
                    datas = datas + c_line.price_subtotal
                elif c_line.sale_layout_cat_id.id == 2:
                    datas2 = datas2 + c_line.price_subtotal
                elif  c_line.sale_layout_cat_id.id == 3:
                    datas3 = datas3 + c_line.price_subtotal
                else:
                    pass
            if datas3:
                datas4 = self.amount_untaxed - (datas + datas2 + datas3)
            else:
                datas4 = self.amount_untaxed - (datas + datas2)
            self.update({'product_subtotal': datas})
            self.update({'service_subtotal': datas2})
            self.update({'discount_subtotal': datas3})
            self.update({'other_subtotal': datas4})


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

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
            elif product.type == "service" and not self.product_id.is_warranty:
                self.update({"sale_layout_cat_id": 2})
        return {'domain': domain}


#class ProductSetAdd(models.TransientModel):
#    _inherit = 'product.set.add'


#    def prepare_sale_order_line_data(self, sale_order_id, set, set_line,
#                                     max_sequence=0):
#        if set_line.product_id.type:
#            if set_line.product_id.type == "product":
                ## Kikihi = 1  self.update({"sale_layout_cat_id": 1})
#                layout = 1
#            elif set_line.product_id.type == "service":
                ## Sekouhi = 2 self.update({"sale_layout_cat_id": 2})
#                layout = 2


#        return {
#            'order_id': sale_order_id,
#            'product_id': set_line.product_id.id,
#            'product_uom_qty': set_line.quantity * self.quantity,
#            'product_uom': set_line.product_id.uom_id.id,
#            'sequence': max_sequence + set_line.sequence,
#            'sale_layout_cat_id': layout 
#        }



class ProductCategory(models.Model):
    _inherit = 'product.category'

    sub_category = fields.Char('Sub Category')

