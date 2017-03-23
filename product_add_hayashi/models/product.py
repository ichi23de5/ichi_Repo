# -*- coding: utf-8 -*-

from openerp import api, fields ,models, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta



class Product(models.Model):
    _inherit = "product.template"



    open_price = fields.Char(string='Vender Price', required=True, store=True, copy=True, default="OPEN")
    is_warranty = fields.Boolean(string="Warranty Flag")
    is_cloud = fields.Boolean(string="Cloud Flag")
    is_payment = fields.Boolean(string="Monthly Payment Flag")
    pay_per = fields.Boolean(string="Pay per Flag")
#    manufacturer = fields.Char(string="Maker")
    manufacturer = fields.Many2one("res.partner", string="Maker")
