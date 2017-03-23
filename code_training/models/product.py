# -*- coding: utf-8 -*-

from openerp import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    analyzer_id = fields.Char(string='Analyzer ID' , related='product_variant_ids.product_tmpl_id.analyzer_id')
