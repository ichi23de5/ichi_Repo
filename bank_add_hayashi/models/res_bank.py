# -*- coding: utf-8 -*-

from openerp import api, fields ,models,  _



class Bank(models.Model):  
    _inherit = 'res.bank' 

    branch = fields.Char(string='Branch Name')



class ResPartnerBank(models.Model): 
    _inherit = 'res.partner.bank' 


    acc_type = fields.Selection([
        ('ordinary', 'Ordinary Account'),
        ('current', 'Current Account')
        ], string='type')
    branch = fields.Char(string='Branch Name', related='bank_id.branch', readonly=True, store=True)

