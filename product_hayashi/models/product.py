# -*- coding: utf-8 -*-

from openerp import api, fields ,models, _

class ProductTemplate(models.Model):
	_inherit = "product.template"

#       check_report = fields.Boolean('Report Check', readonly=False, store=True,)
        analyzer_id = fields.Char('Analyzer Number', readonly=False, store=True, copy=False)

