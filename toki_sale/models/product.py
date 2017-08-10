# -*- coding: utf-8 -*-

from openerp import api, fields ,models, _


class Product(models.Model):
    _inherit = 'product.template'

    open_price = fields.Char('Vender Price', copy=True, default="OPEN")
    is_cloud = fields.Boolean('Cloud Flag')
    maker_id = fields.Many2one('res.partner', 'maker', domain="[('maker','=',True)]", help='TEC no Quotation ni kaku maker wo toroku sitene. res.partner no maker field to default_code field wo kanarazu touroku sitene.')

    is_warranty = fields.Boolean('Warranty Flag')
    scope_of_covaerage = fields.Char('Scope of Covaerage')
    range_coverage = fields.Integer('range_coverage')
    active = fields.Boolean('Active')
    property_war_id = fields.Many2one('property', 'Property warranty ID', index=True, ondelete='cascade', oldname='property_id')
