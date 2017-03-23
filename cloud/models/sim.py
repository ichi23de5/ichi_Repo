# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta
# Non-odoo library
# import random
# from random import randint
# import string

class sim(models.Model):
    _name = 'sim'
    _order = 'date_sim desc'


    user_number = fields.Char(string='SIM User Number', required=True, copy=False,)
    tel_number = fields.Char(string='SIM Tel Number', required=True, copy=False,)
    size_code = fields.Char(string='Size Code', default="FBN0300001",)
    deta_code = fields.Char(string='Price Plan', default="YNSM0_09",)
    sim_number = fields.Char(string='SIM ID', copy=False,)
    date_sim = fields.Datetime(string='Record Date', required=True, index=True, copy=False, default=fields.Datetime.now,)
    iccid_number = fields.Char(string='Iccid Number', copy=False,)

    reception_date = fields.Date(string='Reception Date', required=True, copy=False, index=True,)
    #### auto input ### with reception_date ### 
    arrival_date = fields.Date(string='Arrival Date', readonly=True,)
    charge_date = fields.Date(string='Freebit Charge Date', readonly=True,)
    min_month = fields.Date(string='Minimum Usage Date', readonly=True,)
    expiration_date = fields.Date(string='Expiration Date', readonly=True,)

#### Don't need it now ####
#    cloud_name = field.Selection([
#        ('tkcloud', 'TKCLOUD'),
#        ('eagleeye', 'Eagle Eye'),
#        ], string='service', default='tkcloud')
    

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
