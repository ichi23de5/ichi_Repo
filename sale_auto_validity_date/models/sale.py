# -*- coding: utf-8 -*-


from datetime import datetime, timedelta
from openerp import api, fields, models, _
from dateutil.relativedelta import relativedelta

class SaleOrder(models.Model):
        _inherit = "sale.order"

        @api.onchange('date_order')
        def set_validity_date(self):
            if not self.date_order:
                 return
            else:
                the_day = fields.Date.from_string(self.date_order) + relativedelta(months=3)
                self.validity_date = fields.Date.to_string(the_day)

