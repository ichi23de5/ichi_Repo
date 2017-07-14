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
    date_cloud = fields.Date('Check Date', copy=False, default=fields.Datetime.now, required=True, index=True, readonly=True, states={'check': [('readonly', False)]})
    order_id = fields.Many2one('sale.order', string='Quotation Number', required=True, domain=[('purchase_order','=',True),('check_state','=',('manager','president'))], help='Hachusyo naito check dekinai')
    #### auto input ### with 'order_id' ###
    property_name = fields.Char(related='order_id.property_id.name', string='Property Name', store=True)
    property_add = fields.Char(related='order_id.property_id.address', string='Property Add', readonly=True, store=True)
    partner_id = fields.Char(related='order_id.partner_id.name', string='PartnerName', readonly=True, store=True)
    user_id = fields.Char('Salesperson', related='order_id.user_id.name', readonly=True, store=True)
    plan = fields.Selection([
           ('lite', 'Lite'),
           ('basic', 'Basic'),
           ('entry', 'Entry')],         
           string='TKCLOUD Plan', required=True)
    rate_id = fields.Many2one('cloud.rate.plan', 'Rate Plan', required=True)
#    rate_plan = fields.Selection([
#                ('monthly', 'Monthly Amount'),
#                ('yearly', 'Yearly Amount'),
#                ('lump2', 'Lump sum 2'),
#                ('lump5', 'Lump sum 5'),
#                ('lump7', 'Lump sum 7'),
#                ('incurred', 'Incurred Amount')],
#                string='TKCLOUD Rate Plan', required=True)
    end_user = fields.Char('User Name')
    end_phone = fields.Char('User Phone Number')
    contact_check = fields.Boolean('Contact OK')
    dvr1 = fields.Many2one('product.product', string='dvr1')
    dvr2 = fields.Many2one('product.product', string='dvr2')
    dvr3 = fields.Many2one('product.product', string='dvr3')
    dvr4 = fields.Many2one('product.product', string='dvr4')
    sim_id = fields.Many2one('sim', string='SIM User Number', required=True, copy=False)
    memo = fields.Text('Memo')

    contractor_number = fields.Char('Contractor ID')
    contractor_pass = fields.Char('Contractor PASS')
    application_date = fields.Date('Apprication Date')
    approval_date = fields.Date('Approval Date')

    construction_date = fields.Date('Construction Date', readonly=True, states={'check': [('readonly', False)]})
    #### auto input ### with constraction_date ###
    expiration_date = fields.Date('Expiration Date', store=True, readonly=True, states={'check': [('readonly', False)]})
    changeapp_date = fields.Date('Changeapp Date')
    cancelapp_date = fields.Date('Cancelapp Date')
    cancel_date = fields.Date('Cancel Date')



    @api.onchange('construction_date')
    def _date_calcloud(self):
        main = fields.Datetime.from_string(self.construction_date)
        if main:
            exp = main + relativedelta(day=1, months=25)
            self.update({'expiration_date': exp})
            return


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



class CloudRatePlan(models.Model):
    _name = 'cloud.rate.plan'
    _order = 'name desc'


    name = fields.Char('Plan Name', required=True)
    contract_years = fields.Integer('Keiyaku nensu')
    method = fields.Selection([
           ('lump', 'ikkatsu'),
           ('monthly', 'Monthly'),
           ('yearly', 'Yearly')],
           string='Payment method')
    pay_per_use = fields.Boolean('Juryokakin')
