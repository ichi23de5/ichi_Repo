# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import openerp.addons.decimal_precision as dp
from openerp.tools.misc import formatLang
from openerp.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
import time
from openerp.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    order_id = fields.Many2one('sale.order', 'Order')

class SaleOrder(models.Model):
    _inherit = "sale.order"

    outsource_count = fields.Integer(string='Outside Orders', compute='_compute_outsource')

    @api.multi
    def act_out(self):

        self.ensure_one()
        for ln in self:
            if not ln.outside_id:
                raise UserError(_('Please input Gaichuugyousha.'))
                return

        gaichu_product = self.env['product.template'].browse(10)
        str = "2017-9-1 00:00:00"
        dt = datetime.strptime( str,DATETIME_FORMAT)
     
        pur_vals = {
            'partner_id':  self.outside_id.id,
            'picking_type_id': "1",
            'company_id': self.company_id.id,
            'currency_id': self.env.user.company_id.currency_id.id,
            'date_order':  datetime.now().strftime(DATETIME_FORMAT),
            'date_planned':  datetime.now().strftime(DATETIME_FORMAT),
            'origin': self.name,
            'order_id': self.id,
            'order_line': [
                (0, 0, {
                    'name': gaichu_product.name,
                    'product_id': gaichu_product.id,
                    'product_qty': 1,
                    'product_uom': gaichu_product.uom_po_id.id,
                    'price_unit': gaichu_product.list_price,
                    'date_planned': dt,    
                })],
        }

        return self.env["purchase.order"].create(pur_vals)



    @api.multi
    def _compute_outsource(self):
        for order in self:
            poc = self.env['purchase.order'].search([('origin', '=', self.name)]) 
            order.outsource_count = len(poc)
