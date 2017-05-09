# -*- coding: utf-8 -*-

from openerp import api, fields ,models,  _


class stock_picking(models.Model): 
    _inherit = 'stock.picking'

    property_name = fields.Char('Property Name')
    outside_order = fields.Boolean('Outside Flag', readonly=True, store=True)

