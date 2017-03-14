# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta
# Non-odoo library
# import random
# from random import randint
# import string

class Cloud(models.Model):
    _name = 'cloud'
    _order = 'date_cloud desc'

    date_cloud = fields.Datetime(string='Date', copy=False, default=fields.Datetime.now, required=True, index=True,)
    name = fields.Many2one('sale.order', string='Quotation Number', required=True,)
    #### auto input ### with name ###
    property_name = fields.Char(related='name.project_id.name', string='Property Name', readonly=True,)
    property_add = fields.Char(string='Property Add', readonly=True,)
    client_number = fields.Char(string='Client ID',readonly=True,)
    passward = fields.Char(string='Passward',)
    name_id = fields.Char(string='Name', readonly=True,)
    rep_name_id = fields.Char(string='Rep Name', readonly=True,)
    user_id = fields.Char(string='Salesperson', readonly=True,)
    ass_user_id = fields.Char(string='Assistant', readonly=True,)
    plan = fields.Char(string='TKCLOUD Plan', readonly=True,)
    rate_plan = fields.Char(string='TKCLOUD Rate Plan', readonly=True,)

    end_user = fields.Char(string='User Name',)

    sim_id = fields.Char(string='SIM ID', required=True, copy=False,)

    contractor_number = fields.Char(string='Contractor ID',)
    contractor_pass = fields.Char(string='Contractor PASS',)
    application_date = fields.Date(string='Apprication Date',)
    approval_date = fields.Date(string='Approval Date',)
    construction_date = fields.Date(string='Construction Date',)
    expiration_date = fields.Date(string='Expiration Date',)
    changeapp_date = fields.Date(string='Changeapp Date',)
    cancelapp_date = fields.Date(string='Cancelapp Date',)
    cancel_date = fields.Date(string='Cancel Date',)


#    @api.multi
#    def applicate_sim(self):
#	pass
        #self.ensure_one()
	#Generates a random name between 9 and 15 characters long and writes it to the record.
	#self.write({'name': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9,15)))})

#    @api.multi
#    def arrival_sim(self):
#	pass
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
