# -*- coding: utf-8 -*-

from openerp import api, fields ,models, _


class Product(models.Model):
    _inherit = "product.template"

    open_price = fields.Char('Vender Price', copy=True, default="OPEN")
    is_warranty = fields.Boolean("Warranty Flag")
    is_cloud = fields.Boolean("Cloud Flag")
    maker_id = fields.Many2one("res.partner", "maker", domain="[('maker','=',True)]", help="TEC no Quotation ni kaku maker wo toroku sitene. res.partner no maker field to default_code field wo kanarazu touroku sitene.")
