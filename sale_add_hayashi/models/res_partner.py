# -*- coding: utf-8 -*-

from openerp import api, fields ,models



class ResPartner2(models.Model):
    _inherit = "res.partner"


    outside_order = fields.Boolean(string="Outside Flag")
    mail_address = fields.Char(string="Email") #email field hidden#
    partner_number = fields.Char(string="Partner ID")
    maker = fields.Boolean("Maker Flag")
    default_code = fields.Char("Ryakusyou")



