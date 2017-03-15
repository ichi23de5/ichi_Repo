# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
# Non-odoo library
# import random
# from random import randint
# import string

class Inspection(models.Model):
    _name = 'inspection'
    _order = 'date desc'

    ### property ###
#    property_id = fields.Many2one('property', string='Property ID', required=True,)
    ### inspection ###
    date = fields.Date(string='date', required=True,)
    inspector_id = fields.Many2one('res.users', string='Inspector', readonly=True,)
    act_type = fields.Char(string='Act Type',) #selection
    inspection_note = fields.Text(string='inspection_note',)
    product_memo = fields.Char(string='product_memo',)
    ### request ###
    request_id = fields.Many2one('inspection.request', string='Request')
    request_date = fields.Date(string='request_date', related='request_id.date', readonly=True)
    requester_name = fields.Char(string='requester_name', related='request_id.partner_id.name', readonly=True)
    request_note = fields.Text(string='request_note', related='request_id.request_note', readonly=True)
    responder_name = fields.Char(string='responder_name', related='request_id.user_id.name', readonly=True)
    ### ###
    state = fields.Char(string='state')




#    @api.onchange('reception_date')
#    def _date_calc(self):
#        main = fields.Datetime.from_string(self.reception_date)
#        if main:
#            arr = main + relativedelta(days=2)
#            self.update({'arrival_date': arr})
#            self.update({'charge_date': arr})
#            min = main + relativedelta(days=2, months=12)
#            self.update({'min_month': min})
#            exp = main + relativedelta(days=2, months=24) 
#            self.update({'expiration_date': exp})
#            return


#    @api.multi
#    def applicate_sim(self):
#	pass#
        #self.ensure_one()
	#Generates a random name between 9 and 15 characters long and writes it to the record.
	#self.write({'name': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9,15)))})

#    @api.multi
#    def arrival_sim(self):#
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


class InspectionRequest(models.Model):
    _name = 'inspection.request'
    _order = 'date desc'


    date = fields.Date(string='Date', required=True, copy=False,)
    partner_id = fields.Many2one('res.partner', string='partner_id',)
    request_note = fields.Text(string='request_note',)
    user_id = fields.Many2one('res.users', string='user_id', required=True,)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('inspection.request') or 'New'
        result = super(InspectionRequest, self).create(vals)
        return result

