# -*- coding: utf-8 -*-
from openerp import api, fields ,models,  _

class Property(models.Model):
    _inherit = 'property'

    @api.multi
    def property_so_action_button(self):
        self.ensure_one()
        action = self.env.ref('toki_sale.property_so_action').read()[0]
        action['domain'] = [('property_id', '=', self.id)]
        return action
