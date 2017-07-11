# -*- coding: utf-8 -*-

from openerp import api, fields ,models,  _


class stock_picking(models.Model): 
    _inherit = 'stock.picking'

    property_name = fields.Char('Property Name', related='order_id.property_id.name')
    order_id = fields.Many2one('sale.order', 'Order Number')

    @api.onchange('order_id')
    def _onchange_order_number(self):
        sale = self.order_id.name
        if sale:
            self.update({'origin': sale})
            return






class ProcurementOrder(models.Model): 
    _inherit = "procurement.order" 

    property_id = fields.Char('Property_name',
                              related='sale_line_id.order_id.property_id.display_name', readonly=True)

