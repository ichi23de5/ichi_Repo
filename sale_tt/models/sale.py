# -*- coding: utf-8 -*-
import time
from openerp import api, fields ,models,  _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import openerp.addons.decimal_precision as dp
from openerp.tools.misc import formatLang
from openerp.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    plan_id = fields.Char(string='Plan version')
    check = fields.Boolean(string='Order Checked')

    @api.multi
    def flag_b(self):
        self.ensure_one()
        m_txt = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
        self.message_post(type="comment",subtype="mt_comment",body=m_txt,)

        p_vals = {
            'date_order': datetime.now().strftime(DATETIME_FORMAT),
            'partner_id': 14,
            'currency_id':self.currency_id.id,
            'company_id':self.company_id.id ,
            'picking_type_id': 1,
        }
        p_order = self.env["purchase.order"].create(p_vals)
        
        for line in self:
            pro_ids =  {
                'name': line.order_line.name,
                'date_planned': datetime.now().strftime(DATETIME_FORMAT),
                'product_id': line.order_line.product_id.id,
                'product_qty': line.order_line.product_uom_qty,
                'price_unit': line.order_line.product_id.list_price,
                'product_uom':line.order_line.product_id.uom_id.id ,
                'order_id': p_order.id,
            }
            self.env["purchase.order.line"].create(pro_ids)
        return
        
      

