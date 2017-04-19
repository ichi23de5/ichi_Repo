# -*- coding: utf-8 -*-

from openerp import api, fields ,models,  _

class AccountInvoice(models.Model): 
    _inherit = "account.invoice" 

    property_id = fields.Many2one('property', string='Property Name')
    outside_order = fields.Boolean('Outside Flag')
    completion_date = fields.Date('Syunkoubi')
