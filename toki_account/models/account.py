# -*- coding: utf-8 -*-

from openerp import api, fields ,models,  _
from dateutil.relativedelta import relativedelta
from openerp.exceptions import UserError
from openerp.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT


class AccountInvoice(models.Model): 
    _inherit = "account.invoice" 


    ### invoice for property list ###
    property_line_ids = fields.One2many('account.property.line','invoice_id', string='Property Lines', oldname='property_line',
        readonly=True, states={'draft': [('readonly', False)]}, copy=True) 
#    amount_untaxed_pro = fields.Integer(string='Untaxed Amount', store=True, readonly=True, compute='_amount_pro', track_visibility='always')

#    @api.depends('property_line_ids.price_total') 
#    def _amount_pro(self):
#        for order in self: 
#            amount_untaxed_pro = 0.0 
#            for line in order.property_line_ids:
#                amount_untaxed_pro += line.price_total
#            order.update({ 
#                'amount_untaxed_pro': round(amount_untaxed_pro), 
#            }) 


class AccountInvoiceLine(models.Model): 
    _inherit = 'account.invoice.line' 

    completion_date = fields.Date('Syunkoubi', readonly=True, index=True)
    purchase_number = fields.Char('Purchase Number', readonly=True, index=True)


class AccountPropertyLine(models.Model):
    _name = 'account.property.line'
    _rec_name = 'origin'

    invoice_id = fields.Many2one('account.invoice', 'Invoice Reference', required=True, ondelete='cascade', index=True, copy=False)
    origin = fields.Char('Source', help='Reference of the document that produced this invoice')
    property_id = fields.Many2one('property', string='Property Name', readonly=True, index=True)
    completion_date = fields.Date('Syunkoubi', readonly=True, index=True)
    price_total = fields.Integer('Amount', readonly=True)
    purchase_number = fields.Char('Purchase Number', readonly=True, index=True)
    type_id = fields.Char('Act Type', help='Seikyusyo no KoujiSyubetsu wo kaku.', index=True)



class AccountActType(models.Model):
    _name = 'account.act.type'
    _rec_name = 'type_id'

    type_id = fields.Char('Act Type', required=True)
    category = fields.Selection([
        ('construction', 'Construction'),
        ('inspection', 'Inspection'),
        ('goods', 'Sale of Product'),
        ('other', 'Others')
        ], string='Category')


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    act_type = fields.Many2one('account.act.type', 'Act Type', help='Seikyusyo no KoujiSyubetsu wo kaku.')
    purchase_number = fields.Char('Purchase Number')
    completion_date = fields.Date('Syunkoubi Nohinbi', states={'draft': [('readonly', True)], 'sent': [('readonly', True)]})

    ### reflect account.invoice ###
    @api.multi
    def _prepare_invoice(self):
        self.ensure_one()
        journal_id = self.env['account.invoice'].default_get(['journal_id'])['journal_id']
        if not journal_id:
            raise UserError(_('Please define an accounting sale journal for this company.'))
        if not self.purchase_order:
            raise UserError(_('Hachusyo ga kiteimasen!'))
        invoice_vals = {
            'name': self.client_order_ref or '',
            'origin': self.name,
            'type': 'out_invoice',
            'account_id': self.partner_invoice_id.property_account_receivable_id.id,
            'partner_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'journal_id': journal_id,
            'currency_id': self.pricelist_id.currency_id.id,
            'comment': self.note,
            'payment_term_id': self.payment_term_id.id,
            'fiscal_position_id': self.fiscal_position_id.id or self.partner_invoice_id.property_account_position_id.id,
            'company_id': self.company_id.id,
            'user_id': self.user_id and self.user_id.id,
            'team_id': self.team_id.id,
            'property_line_ids': [(0, 0, {
                'origin': self.name,
                'property_id': self.property_id.id or False,
                'completion_date': self.completion_date,
                'price_total': self.amount_untaxed,
                'purchase_number': self.purchase_number or False,
                'type_id': self.act_type.type_id,
            })],           
        }
        return invoice_vals




class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"



    @api.multi
    def _prepare_invoice_line(self, qty):
        """
        Prepare the dict of values to create the new invoice line for a sales order line.

        :param qty: float quantity to invoice
        """
        self.ensure_one()
        res = {}
        account = self.product_id.property_account_income_id or self.product_id.categ_id.property_account_income_categ_id
        if not account:
            raise UserError(_('Please define income account for this product: "%s" (id:%d) - or for its category: "%s".') % \
                            (self.product_id.name, self.product_id.id, self.product_id.categ_id.name))

        fpos = self.order_id.fiscal_position_id or self.order_id.partner_id.property_account_position_id
        if fpos:
            account = fpos.map_account(account)

        res = {
            'name': self.name,
            'sequence': self.sequence,
            'origin': self.order_id.name,
            'account_id': account.id,
            'price_unit': self.price_unit,
            'quantity': qty,
            'discount': self.discount,
            'uom_id': self.product_uom.id,
            'product_id': self.product_id.id or False,
            'invoice_line_tax_ids': [(6, 0, self.tax_id.ids)],
            'account_analytic_id': self.order_id.project_id.id,
            'purchase_number': self.order_id.purchase_number,
            'completion_date': self.order_id.completion_date,
        }
        return res
