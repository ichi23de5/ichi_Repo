# -*- coding: utf-8 -*-


from openerp import models, fields, api, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import openerp.addons.decimal_precision as dp
from openerp.tools.misc import formatLang
from openerp.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
import time


class SaleOrder(models.Model):
    _inherit = "sale.order"


    @api.multi
    def act_out(self):

        self.ensure_one()
        gaichu_product = self.env['product.template'].browse(115)
#        self.write({'version': gaichu_product.name + str(gaichu_product.id) + str(gaichu_product.uom_po_id.id) + str(gaichu_product.list_price)})
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
