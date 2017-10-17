# -*- coding: utf-8 -*-

import openerp.addons.decimal_precision as dp
from openerp import fields, models, api, _
from openerp.exceptions import UserError         


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    chr_open_price = fields.Char(string='chr_OpenPrice ', store=True, readonly=False)

    @api.onchange('open_price')
    def _compute_openprice(self):
        self.ensure_one()
        st = ""
        if self.open_price == 0 or not self.open_price:
            st = "" 
        elif self.open_price < 0:
            st = "OPEN"
        else:
            st = str(self.open_price)
      
        return self.update({"chr_open_price": st })
        

