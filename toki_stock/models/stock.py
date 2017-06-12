# -*- coding: utf-8 -*-

from openerp import api, fields ,models,  _


class stock_picking(models.Model): 
    _inherit = 'stock.picking'

    property_name = fields.Char( string='Property Name',related='move_lines.procurement_id.sale_line_id.order_id.property_id.display_name', readonly=True)
    outside_order = fields.Boolean('Outside Flag', readonly=True, store=True)
    state = fields.Selection([
        ('draft', 'Draft'), ('cancel', 'Cancelled'),
        ('waiting', 'Waiting Another Operation'),
        ('confirmed', 'Waiting Availability'),
        ('partially_available', 'Partially Available'),
        ('assigned', 'Available'), ('waiting_shipment', 'Waiting Shipment'),
        ('done', 'Done')], string='Status', compute='_compute_state',
        copy=False, index=True, readonly=True, store=True, track_visibility='onchange',
        help=" * Draft: not confirmed yet and will not be scheduled until confirmed\n"
             " * Waiting Another Operation: waiting for another move to proceed before it becomes automatically available (e.g. in Make-To-Order flows)\n"
             " * Waiting Availability: still waiting for the availability of products\n"
             " * Partially Available: some products are available and reserved\n"
             " * Ready to Transfer: products reserved, simply waiting for confirmation.\n"
             " * Waiting Shipment: After inspecting, waiting for shipment in warehouse.\n"
             " * Transferred: has been processed, can't be modified or cancelled anymore\n"
             " * Cancelled: has been cancelled, can't be confirmed anymore")


    @api.multi
    def shipment(self):
        self.write({'state': 'waiting_shipment'})


class StockMove(models.Model):
    _inherit = 'stock.move'

    property_name = fields.Char(string='Property Name',related='procurement_id.sale_line_id.order_id.property_id.display_name',readonly=True)
    outside_order = fields.Boolean('Outside Flag', readonly=True, store=True)




class ProcurementOrder(models.Model): 
    _inherit = "procurement.order" 

    property_id = fields.Char(string='Property_name', related='sale_line_id.order_id.property_id.display_name', readonly=True)

