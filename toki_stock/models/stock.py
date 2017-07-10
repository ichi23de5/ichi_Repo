# -*- coding: utf-8 -*-

from openerp import api, fields ,models,  _


class stock_picking(models.Model): 
    _inherit = 'stock.picking'

    property_name = fields.Char('Property Name', related='order_id.property_id.name')
    order_id = fields.Many2one('sale.order', 'Order Number')







class StockMove(models.Model):
    _inherit = 'stock.move'

    property_name = fields.Char('Property Name',
                                related='procurement_id.sale_line_id.order_id.property_id.display_name',readonly=True)




class ProcurementOrder(models.Model): 
    _inherit = "procurement.order" 

    property_id = fields.Char('Property_name',
                              related='sale_line_id.order_id.property_id.display_name', readonly=True)

