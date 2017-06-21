# -*- coding: utf-8 -*-

from openerp import api, fields ,models



class ResPartner2(models.Model):
    _inherit = "res.partner"


    outside_order = fields.Boolean("Outside Flag")
    mail_address = fields.Char("Email") #email field hidden#
    partner_number = fields.Char("Partner ID")
    maker = fields.Boolean("Maker Flag")
    default_code = fields.Char("Ryakusyou")
#    direct_transaction = fields.Boolean("Direct transaction", help="TOKI to cyokusetsu torihiki siteru kojin nado")


#    @api.onchange('direct_transaction')
#    def _direct_flag(self):
#        if self.direct_transaction:
#            self.update({'customer':True})
#            return

    @api.onchange('outside_order')
    def _outside_flag(self):
        if self.outside_order:
            self.update({'supplier':True})
            return

