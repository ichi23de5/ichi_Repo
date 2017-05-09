# -*- coding: utf-8 -*-

from openerp import api, fields ,models,  _

class AccountInvoice(models.Model): 
    _inherit = "account.invoice" 

    property_name = fields.Char(string='Property Name', readonly=True, store=True)
    completion_date = fields.Date('Syunkoubi', readonly=True, store=True)
