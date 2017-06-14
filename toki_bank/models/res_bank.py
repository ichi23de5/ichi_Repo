# -*- coding: utf-8 -*-

from openerp import api, fields ,models,  _



class Bank(models.Model):  
    _inherit = 'res.bank' 

    branch = fields.Char('Branch Name')



class ResPartnerBank(models.Model): 
    _inherit = 'res.partner.bank' 


    acc_type = fields.Selection([
        ('ordinary', 'Ordinary Account'),
        ('current', 'Current Account')
        ], string='type')
    branch = fields.Char('Branch Name', related='bank_id.branch', readonly=True, store=True)


class ResPartner(models.Model):
    _inherit = "res.partner"


#    payee_bank = fields.Many2one('res.partner.bank', 'Hurikomisaki')
#                                 domain="[('partner_id.id', '=', '1')]",
#                                 help='seikyu surutoki no TOKI furikomisaki bank')

