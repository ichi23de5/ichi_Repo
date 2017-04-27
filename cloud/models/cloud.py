# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class Cloud(models.Model):
    _name = 'cloud'
    _order = 'date_cloud desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']


    state = fields.Selection([ 
         ('check', 'Check'), 
         ('work', 'Working'), 
         ('stop', 'Stopping'), 
         ('finish', 'Finished'), 
         ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='check', help='finish ni ittara saikeiyaku') 
    date_cloud = fields.Date(string='Check Date', copy=False, default=fields.Datetime.now, required=True, index=True, readonly=True, states={'check': [('readonly', False)]})
    order_id = fields.Many2one('sale.order', string='Quotation Number', required=True,)
    #### auto input ### with name ###
    property_name = fields.Char(related='order_id.property_id.name', string='Property Name', store=True)
    property_add = fields.Char(related='order_id.property_id.address', string='Property Add', readonly=True, store=True)
    partner_id = fields.Char(related='order_id.partner_id.name', string='PartnerName', readonly=True, store=True)
#    rep_partner_name = fields.Char(string='Rep Name', related='order_id.partner_id.name', readonly=True, store=True)
    user_id = fields.Char(string='Salesperson', related='order_id.user_id.name', readonly=True, store=True)
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
    dvr1 = fields.Many2one('product.product', string='dvr1')
    dvr2 = fields.Many2one('product.product', string='dvr2')
    dvr3 = fields.Many2one('product.product', string='dvr3')
    dvr4 = fields.Many2one('product.product', string='dvr4')
    sim_id = fields.Many2one('sim', string='SIM ID', required=True, copy=False,)
    memo = fields.Text('Memo')

    contractor_number = fields.Char(string='Contractor ID',)
    contractor_pass = fields.Char(string='Contractor PASS',)
    application_date = fields.Date(string='Apprication Date',)
    approval_date = fields.Date(string='Approval Date',)

    construction_date = fields.Date(string='Construction Date', readonly=True, states={'check': [('readonly', False)]})
    #### auto input ### with constraction_date ###
    expiration_date = fields.Date(string='Expiration Date', store=True, readonly=True, states={'check': [('readonly', False)]})
#    end_date = fields.Date(string='Service End Date', store=True, readonly=True, states={'check': [('readonly', False)]})
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


#    contract_years = fields.Integer('Keiyakunensu', related='order_id.contract_years', invisible='1')

#    @api.onchange('construction_date')
#    def _date_service_end(self):
#        main = fields.Datetime.from_string(self.construction_date)
#        if main:
#            vals = self.contract_years
#            end = main + relativedelta(day=1, months=vals)
#            self.update({'end_date': end})
#            return






    ### state shift button ###
    @api.multi 
    def start(self): 
        self.write({'state': 'work'}) 

    @api.multi
    def stop(self):
        self.write({'state': 'stop'})

    @api.multi
    def finish(self):
        self.write({'state': 'finish'})

