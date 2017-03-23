# -*- coding: utf-8 -*-

from openerp import api, fields ,models, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta



class Product(models.Model):
    _inherit = "product.template"


#       = fields.('', string='', readonly=True, store=True, copy=False, required=True, related='')

    reference_price = fields.Char(string="Reference Price", default="open")
    is_warranty = fields.Boolean(string="Warranty Flag")
    is_cloud = fields.Boolean(string="Cloud Flag")
    is_payment = fields.Boolean(string="Monthly Payment Flag")
    pay_per = fields.Boolean(string="Pay per Flag")
#    manufacturer = fields.Char(string="Maker")
    manufacturer = fields.Many2one("res.partner", string="Maker")
