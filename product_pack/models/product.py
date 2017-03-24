
# -*- coding: utf-8 -*-

from openerp import api, fields, models, tools, _
from openerp.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    pack_flag = fields.Boolean("Pack_flag")
    product_packs = fields.One2many('product.pack','order_id',string='Pack Product',)



class ProductPack(models.Model):
    _name= "product.pack"

    order_id = fields.Many2one('product.product',string='Ref Product')
    product_id = fields.Many2one('product.product',string='Products',required=True)
    product_uom_qty = fields.Float('Quantity')
    product_uom = fields.Many2one('product.uom', string='Quantity')
