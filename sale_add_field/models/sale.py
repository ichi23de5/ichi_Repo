# -*- coding: utf-8 -*-

from openerp import api, fields ,models, _

class SaleOrder(models.Model):
	_inherit = "sale.order"

	check_report = fields.Boolean('Report Check', readonly=False, store=True,)
        check_manager = fields.Boolean('Managers Check', readonly=False, store=True,)
        check_primer = fields.Boolean('Prime Check', readonly=False, store=True,)
