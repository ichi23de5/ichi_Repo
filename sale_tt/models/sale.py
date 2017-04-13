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
        pro_vals = {}
        
        for line in self.env["purchase.order.line"].create(pro_vals)
            pro_ids =  {
                'name': line.order_line.name,
                'date_planned': datetime.now().strftime(DATETIME_FORMAT),
                'product_id': line.order_line.product_id.id,
                'product_qty': line.order_line.product_uom_qty,
                'price_unit': line.order_line.product_id.list_price,
                'state': "confirmed",
            }
            line.write(pro_ids)
        
        p_vals = {
            'date_order': datetime.now().strftime(DATETIME_FORMAT),
            'partner_id': 14,
            'currency_id':self.currency_id.id,
            'company_id':self.company_id.id ,
            'picking_type_id': 1,
            'order_line': [(6,0,order_dic)],
        }
        return self.env["purchase.order"].create(p_vals)
       
#        return self.env["procurement.order"].create(pro_vals)


#class SaleOrderLine(models.Model):
#    _inherit = 'sale.order.line'


#    @api.multi
#    def _action_procurement_create(self):
#        res = super(SaleOrderLine, self)._action_procurement_create()
#        orders = list(set(x.order_id for x in self))
#        for order in orders:
#            reassign = order.picking_ids.filtered(lambda x: x.state=='confirmed' or ((x.state in ['partially_available', 'waiting']) and not x.printed))
#            if reassign:
#                reassign.do_unreserve()
#                reassign.action_assign()
#        return res
