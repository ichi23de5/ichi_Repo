# -*- coding: utf-8 -*-
import time
from openerp import api, fields ,models,  _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import openerp.addons.decimal_precision as dp
from openerp.tools.misc import formatLang

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    plan_id = fields.Char(string='Plan version')
    check = fields.Boolean(string='Order Checked')


#    @api.model
#    def create(self, vals):
#        if vals.get('name', 'New') == 'New':
#            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order') or '/'
#        return super(PurchaseOrder, self).create(vals)


    @api.multi
    def flag_b(self, vals):
        self.ensure_one()
        m_txt = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
        self.message_post(type="comment",subtype="mt_comment",body=m_txt,)
        p_vals = {
            'date_order':datetime.now().strftime(DATETIME_FORMAT),
            'partner_id': 14,
            'currency_id':self.currency_id.id,
            'company_id':self.company_id.id ,
            'picking_type_id': 1,
            
        }
        return self.env["purchase.order"].create(p_vals) 
