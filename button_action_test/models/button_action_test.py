# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta
# Non-odoo library
# import random
# from random import randint
# import string

class daily_report_demo(models.Model):
    _name = 'daily.report'
    _order = 'date_report desc'

    name = fields.Char(string='Property Place' , required=True , default='Note a property place name!')
    daily_report = fields.Text(string='Report Note' , required=True , store=True)
    date_report = fields.Datetime(string='Report Date', required=True, readonly=True, index=True,  copy=False, default=fields.Datetime.now)


    @api.multi
    def function_a(self):
	pass
        #self.ensure_one()
	#Generates a random name between 9 and 15 characters long and writes it to the record.
	#self.write({'name': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9,15)))})

    @api.multi
    def function_b(self):
	pass
        #self.ensure_one()
	#Generates a random password between 12 and 15 characters long and writes it to the record.
	#self.write({
	#    'password': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(12,15)))
	#})

    @api.multi
    def function_c(self):
	pass
        #self.ensure_one()
	#self.write({
	#    'name': '',
	#    'password': ''
	#})
