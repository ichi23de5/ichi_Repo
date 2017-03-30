# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class cloud(models.Model):
    _name = 'cloud'
    _order = 'date_cloud desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']



    date_cloud = fields.Datetime(string='Date', copy=False, default=fields.Datetime.now, required=True, index=True,)
    order_id = fields.Many2one('sale.order', string='Quotation Number', required=True,)
    #### auto input ### with name ###
#    property_name = fields.Char(related='name.project_id.name', string='Property Name', readonly=True,)
    property_name = fields.Char(related='order_id.property_id.name', string='Property Name', readonly=True,)
    property_add = fields.Char(related='order_id.property_id.address', string='Property Add', readonly=True,)
     #### Don't need it now ####
#    client_number = fields.Char(string='Client ID',readonly=True,)
#    passward = fields.Char(string='Passward',)

#    partner_id = fields.Char(related='order_id.parter_id.name', string='PartnerName', readonly=True,)
    rep_partner_id = fields.Char(string='Rep Name', readonly=True,)
    user_id = fields.Char(related='order_id.user_id.name',string='Salesperson', readonly=True,)
#    assinstant_id = fields.Char(related='order_id.assistant_id.name', string='Assistant', readonly=True,)
    plan = fields.Char(related='order_id.', string='TKCLOUD Plan', readonly=True,)
    rate_plan = fields.Char(string='TKCLOUD Rate Plan', readonly=True,)



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






class CloudContractor(models.Model):
    _name = 'cloud_contractor'
#    _order = ''

    
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

