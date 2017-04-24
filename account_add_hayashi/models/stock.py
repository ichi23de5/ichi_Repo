# -*- coding: utf-8 -*-

from openerp import api, fields ,models,  _


class stock_picking(models.Model): 
    _inherit = 'stock.picking'

    property_name = fields.Char('Property Name')
#    property_name = fields.Char('Property Name', related='order_id.property_id.name', store=True)
    order_id = fields.Many2one('sale.order', 'Order Number')
    outside_order = fields.Boolean('Outside Flag', readonly=True, store=True)

