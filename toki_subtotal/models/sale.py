# -*- coding: utf-8 -*-

from itertools import groupby
from openerp import fields, models, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    product_subtotal = fields.Monetary(string='Product Subtotal', store=False, readonly=True, compute='_compute_subtotal')
    service_subtotal = fields.Monetary(string='Service Subtotal', store=False, readonly=True, compute='_compute_subtotal')
    discount_subtotal = fields.Monetary(string='Discount Subtotal', store=False, readonly=True, compute='_compute_subtotal')
    other_subtotal = fields.Monetary(string='Other Subtotal', store=False, readonly=True, compute='_compute_subtotal')

    @api.onchange('order_line')
    def _compute_subtotal(self):
        self.ensure_one()
        datas = 0
        datas2 = 0
        datas3 = 0
        datas4 = 0
        for category, lines in groupby(self.order_line, lambda l: l.sale_layout_cat_id):
            for c_line in lines:
                if c_line.sale_layout_cat_id.id == 1:
                    datas = datas + c_line.price_subtotal
                elif c_line.sale_layout_cat_id.id == 2:
                    datas2 = datas2 + c_line.price_subtotal
                elif  c_line.sale_layout_cat_id.id == 3:
                    datas3 = datas3 + c_line.price_subtotal
                else:
                    pass
            if datas3:
                datas4 = self.amount_untaxed - (datas + datas2 + datas3)
            else:
                datas4 = self.amount_untaxed - (datas + datas2)
            self.update({'product_subtotal': datas})
            self.update({'service_subtotal': datas2})
            self.update({'discount_subtotal': datas3})
            self.update({'other_subtotal': datas4})
