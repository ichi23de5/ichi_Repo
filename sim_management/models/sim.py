# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import math
# Non-odoo library
# import random
# from random import randint
# import string

class Sim(models.Model):
    _name = 'sim'
    _order = 'date_sim desc'


    user_number = fields.Char(string='SIM User Number', required=True, copy=False,)
#    tel_number = fields.Char(string='SIM Tel Number', required=False, copy=False,)
    phone = fields.Char(string='SIM Tel Number', required=False, copy=False,)
    size_code = fields.Char(string='Size Code', default="FBN0300001",)
    deta_code = fields.Char(string='Price Plan', default="YNSM0_09",)
    sim_id = fields.Char(string='SIM ID', copy=False,)
    date_sim = fields.Datetime(string='Record Date', required=True, index=True, copy=False, default=fields.Datetime.now,)
    iccid_number = fields.Char(string='Iccid Number', copy=False,)

    reception_date = fields.Date(string='Reception Date', required=True, copy=False, store=True, index=True,)
    #### auto input ### with reception_date ### 
    arrival_date = fields.Date(string='Arrival Date', store=True)
    charge_date = fields.Date(string='Freebit Charge Date', store=True)
    min_month = fields.Date(string='Minimum Usage Date', store=True)
    expiration_date = fields.Date(string='Expiration Date', store=True)

#### Don't need it now ####
#    cloud_name = field.Selection([
#        ('tkcloud', 'TKCLOUD'),
#        ('eagleeye', 'Eagle Eye'),
#        ], string='service', default='tkcloud',)
#    emp_number = fields.Integer(string="Emp Number",)      

    @api.onchange('reception_date')
    def _date_calc(self):
        main = fields.Datetime.from_string(self.reception_date)
        if main:
            arr = main + relativedelta(days=2)
            self.update({'arrival_date': arr})
            self.update({'charge_date': arr})
            min = main + relativedelta(days=2, months=12)
            self.update({'min_month': min})
            exp = main + relativedelta(days=2, months=24) 
            self.update({'expiration_date': exp})
            return


    @api.multi
    def applicate_sim(self):
	pass
        #self.ensure_one()
	#Generates a random name between 9 and 15 characters long and writes it to the record.
	#self.write({'name': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9,15)))})

    @api.multi
    def arrival_sim(self):
	pass
        #self.ensure_one()
	#Generates a random password between 12 and 15 characters long and writes it to the record.
	#self.write({
	#    'password': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(12,15)))
	#})

#    @api.multi
#    def function_c(self):
#	pass
        #self.ensure_one()
	#self.write({
	#    'name': '',
	#    'password': ''
	#})
