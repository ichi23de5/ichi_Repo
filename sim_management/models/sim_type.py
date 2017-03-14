# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta, date
#from dateutil.relativedelta import relativedelta
import math
# Non-odoo library
# import random
# from random import randint
# import string

class SimType(models.Model):
    _name = 'sim_type'
    _inherit = 'sim'
    _order = 'date_sim desc'


    size_code = fields.Char(string='Size Code', store=True,)
    deta_code = fields.Char(string='Price Plan', store=True,)
    date_sim = fields.Datetime(string='Record Date', required=True, index=True, copy=False, default=fields.Datetime.now,)
