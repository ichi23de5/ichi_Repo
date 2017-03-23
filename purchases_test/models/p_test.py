# -*- coding: utf-8 -*-

#from odoo import api, fields, models
#from datetime import datetime, timedelta


#class PurchaseOrder(models.Model):
#    _inherit = "purchase.order"


#    mainmenu_id = fields.Char('menu')
#    gourmet_report = fields.Text(string='Tabelog')
#    companion_id = fields.Many2one('res.users', string='companion')
#    date_report = fields.Date(string='Report Date', required=True, readonly=Tru$
#    val_del = fields.Boolean(string='Delicious?')
#    price_menu = fields.Integer(string='price', default=0)
#    image_main = fields.Binary(string='picture', attachment=True,)


#    @api.multi
#    def function_a(self):
#
#        self.ensure_one()
#        self.gourmet_report = "You push down the function A button!!"
#        return

#    @api.multi
#    def function_b(self):
#        self.ensure_one()
#        self.price_menu = 2000
#        return


#    @api.multi
#    def function_c(self):
#        self.write({'test':'Can you see?'})
#        return

