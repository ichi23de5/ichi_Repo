# -*- coding: utf-8 -*-

from openerp import api, fields ,models, _

class SaleOrder(models.Model):
	_inherit = "sale.order"

	report_ = fields.Boolean('Order Recieved', readonly=False, store=True, help="Flagged when recieve order from Customer")

