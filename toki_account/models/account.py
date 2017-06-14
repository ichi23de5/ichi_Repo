# -*- coding: utf-8 -*-

from openerp import api, fields ,models,  _

class AccountInvoice(models.Model): 
    _inherit = "account.invoice" 

    property_name = fields.Char(string='Property Name', readonly=True, store=True)
    completion_date = fields.Date('Syunkoubi', readonly=True, store=True)



class SaleOrder(models.Model):
    _inherit = 'sale.order'


    ### reflect account.invoice ###
    @api.multi
    def _prepare_invoice(self):
        self.ensure_one()
        journal_id = self.env['account.invoice'].default_get(['journal_id'])['journal_id']
        if not journal_id:
            raise UserError(_('Please define an accounting sale journal for this company.'))
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
            'property_name': self.property_id.name or '',
            'completion_date': self.completion_date
        }
        return invoice_vals

