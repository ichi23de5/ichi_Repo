# -*- coding: utf-8 -*-

from openerp import models, fields 

class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit =  ['sale.order.line', 'mail.thread', 'ir.needaction_mixin']
