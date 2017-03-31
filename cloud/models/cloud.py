# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class Cloud(models.Model):
    _name = 'cloud'
    _order = 'date_cloud desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']



    date_cloud = fields.Date(string='Date', copy=False, default=fields.Datetime.now, required=True, index=True,)
    order_id = fields.Many2one('sale.order', string='Quotation Number', required=True,)
    #### auto input ### with name ###
#    property_name = fields.Char(related='order_id.property_id.name', string='Property Name', store=True)
#    property_add = fields.Char(related='order_id.property_id.address', string='Property Add', readonly=True, store=True)
#    partner_id = fields.Char(related='order_id.partner_id.name', string='PartnerName', readonly=True, store=True)
    rep_partner_id = fields.Char(string='Rep Name', related='order_id.partner_id.name', readonly=True, store=True)
    user_id = fields.Char(string='Salesperson', related='order_id.user_id.name', readonly=True, store=True)
#    assistant_id = fields.Char(related='order_id.assistant.name', string='Assistant', readonly=True, store=True)
    plan = fields.Selection([
           ('lite', 'Lite'),
           ('standard', 'Standard'),
           ('pro', 'Pro')],         
           string='TKCLOUD Plan', required=True)
    rate_plan = fields.Selection([
                ('monthly', 'Monthly Amount'),
                ('yearly', 'Yearly Amount'),
                ('lump2', 'Lump sum 2'),
                ('lump5', 'Lump sum 5'),
                ('lump7', 'Lump sum 7'),
                ('incurred', 'Incurred Amount')],
                string='TKCLOUD Rate Plan', required=True)
    end_user = fields.Char(string='User Name')

    sim_id = fields.Many2one('sim', string='SIM ID', required=True, copy=False,)

    contractor_number = fields.Char(string='Contractor ID',)
    contractor_pass = fields.Char(string='Contractor PASS',)
    application_date = fields.Date(string='Apprication Date',)
    approval_date = fields.Date(string='Approval Date',)

    construction_date = fields.Date(string='Construction Date',)
    #### auto input ### with constraction_date ###
    expiration_date = fields.Date(string='Expiration Date', store=True)
    changeapp_date = fields.Date(string='Changeapp Date',)
    cancelapp_date = fields.Date(string='Cancelapp Date',)
    cancel_date = fields.Date(string='Cancel Date',)

#    quotation_ids = fields.One2many('sale.order','cloud_id', help='cloud no mitsumori zenbu ireru')


    @api.onchange('construction_date')
    def _date_calcloud(self):
        main = fields.Datetime.from_string(self.construction_date)
        if main:
            exp = main + relativedelta(day=1, months=25)
            self.update({'expiration_date': exp})
            return





##### for create passward model ####
#####################################
#class CloudContractor(models.Model):
#    _name = 'cloud_contractor'

    
#    contractor_number = fields.Char(string='Contractor ID', store=True)
#    contractor_pass = fields.Char(string='Contractor PASS',)
#    property_name = fields.Many2one('cloud', string='Property Name', readonly=True,)


#    @api.multi
#    def generate_record_name(self):
#        self.ensure_one()
        #Generates a random name between 9 and 15 characters long and writes it to the record.
#        self.write({
#            'contractor_pass': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9,15)))
#        })



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

