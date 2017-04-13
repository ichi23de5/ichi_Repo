# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
import string
from openerp.exceptions import UserError, AccessError

class Cloud(models.Model):
    _name = 'cloud'
    _order = 'date_cloud desc'

    date_cloud = fields.Datetime(string='Date', copy=False, default=fields.Datetime.now, required=True, index=True,)
    name = fields.Many2one('sale.order', string='Quotation Number', required=True,)
    property_name = fields.Char(string='Property Name')
    property_add = fields.Char(string='Property Add')
    name_id = fields.Many2one('res.partner' , string='Name', domain=[('company_type','=','company')])
    rep_name_id = fields.Many2one('res.partner', string='Rep Name', domain=[('company_type','=','person'),('customer','=',True)])
    user_id = fields.Char(string='Salesperson')
    ass_user_id = fields.Char(string='Assistant')
    plan = fields.Char(string='TKCLOUD Plan')
    rate_plan = fields.Char(string='TKCLOUD Rate Plan')
    end_user = fields.Char(string='User Name',)

    sim_id = fields.Many2one('sim', string='SIM ID', required=True, copy=False,)

    contractor_number = fields.Char(string='Contractor ID',)
    contractor_pass = fields.Char(string='Contractor PASS',)
    application_date = fields.Date(string='Apprication Date',)
    approval_date = fields.Date(string='Approval Date',)
    construction_date = fields.Date(string='Construction Date',)
    #### auto input ### with constraction_date ###
    expiration_date = fields.Date(string='Expiration Date',)

    changeapp_date = fields.Date(string='Changeapp Date',)
    cancelapp_date = fields.Date(string='Cancelapp Date',)
    cancel_date = fields.Date(string='Cancel Date',)


    @api.onchange('construction_date')
    def _date_calcloud(self):
        main = fields.Datetime.from_string(self.construction_date)
        if main:
            exp = main + relativedelta(day=1, months=25)
            self.update({'expiration_date': exp})
            return


    @api.onchange('application_date')
    def _prepare_generate_code(self):
        self.ensure_one()
        c_day = ""
        c_month = ""
        c_year = ""
        if self.application_date:
            ad = self.application_date
            st = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            y = int(ad[0:4])
            yy = y-2016
            c_year = st[yy-1:yy]
            m = int(ad[5:7])
            c_month = st[m-1:m]
            d = int(ad[8:10])
            c_day = st[d-1:d]
       
        it = int(self.contractor_pass) 
        hx = hex(it)[2:7]
        if self.name_id.prefix_code:
            pf = self.name_id.prefix_code    
        else:
            pf = "Error"
        self.update({'property_name': pf + "-" + c_year + c_month + c_day + "-" + hx})
        self.update({'property_add': hx})
        





    @api.multi
    def flag_a(self):
        self.ensure_one()
        cont = self.env['res.partner'].browse(vals.get('partner_id')) 
        nm = ""
        for i in cont:
            nm += i.name + ","
        return self.write({'contractor_number': nm})



class CloudContractor(models.Model):
    _name = 'cloud_contractor'
#    _order = ''
#    _description = ''

    
    contractor_number = fields.Char(string='Contractor ID',)
    contractor_pass = fields.Char(string='Contractor PASS',)
#    property_name = fields.Many2one(related='name.project_id.name', string='Property Name', readonly=True,)



    @api.multi
    def generate_record_name(self):
        self.ensure_one()
        #Generates a random name between 9 and 15 characters long and writes it to the record.
        self.write({
            'contractor_pass': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9,15)))
        })



#    @api.multi
#    def generate_record_password(self):
#        self.ensure_one()
#        #Generates a random password between 12 and 15 characters long and writes it to the record.
#        self.write({
#            'contractor_pass': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(range(randint(12,15)))
#        })

#    @api.multi
#    def clear_record_data(self):
#        self.ensure_one()
#        self.write({
#            'contractor_number': '',
#            'contractor_pass': ''
#        })


