# -*- coding: utf-8 -*-

from openerp import api, fields ,models, _

class SaleOrder(models.Model):
	_inherit = "sale.order"

#       check_report = fields.Boolean('Report Check', readonly=False, store=True,)
        analyzer_id = fields.Char('Analyzer Number', readonly=False, store=True, copy=False)

