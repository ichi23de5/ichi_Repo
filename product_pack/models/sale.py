# -*- coding: utf-8 -*-

from openerp import api, fields, models, _


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):

        if not self.product_id:
            return {'domain': {'product_uom': []}}

        vals = {}
        domain = {'product_uom': [('category_id', '=', self.product_id.uom_id.category_id.id)]}

        if self.product_id.pack_flag == True: 
            for line in self.product_id:
                pass
        else:
            return {'domain': domain}
