# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class CloudOrder(models.Model):
    _name = 'cloud.order'
    _order = 'date_cloud desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']


    state = fields.Selection([ 
         ('order', 'Order'),
         ('check', 'Check'), 
         ('work', 'Working'), 
         ('stop', 'Stopping'), 
         ('finish', 'Finished'), 
         ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='order',
         help='Order: Eigyo kara Tantou he touroku order. Check: Tantou ga check to sotsu test. Working: Kadochu. Stopping: Teishichu. Finished: Keiyakukikan End.Teishizumi.'
         ) 
    date_cloud = fields.Date('Check Date', copy=False, default=fields.Datetime.now, required=True, index=True, readonly=True, states={'order': [('readonly', False)]})
    communication_date = fields.Datetime('Communication Date', help='Sotsu kakunin Datetime order.')
    order_id = fields.Many2one('sale.order', 'Quotation Number', required=True, domain=[('purchase_order','=',True),('check_state','=',('manager','president'))], help='Hachusyo naito check dekinai')
    #### auto input ### with 'order_id' ###
    property_name = fields.Char(related='order_id.property_id.name', string='Property Name', store=True, help='Property name ha jiyu ni henkou siteyoi.')
    property_add = fields.Char(related='order_id.property_id.address', string='Property Add', readonly=True, store=True)
    partner_id = fields.Many2one('res.partner', related='order_id.partner_id', string='PartnerName', readonly=True)
    user_id = fields.Many2one('res.users', 'Salesperson', related='order_id.user_id', readonly=True)
    plan = fields.Selection([
           ('lite', 'Lite'),
           ('basic', 'Basic'),
           ('entry', 'Entry')],         
           string='TKCLOUD Plan', required=True)
    rate_id = fields.Many2one('cloud.rate.plan', 'Rate Plan', required=True)
    end_user = fields.Char('User Name')
    end_phone = fields.Char('User Phone Number')
    contact_check = fields.Boolean('Contact OK')

    cloud_partner_id = fields.Many2one('cloud.partner', 'Management Company', required=True, domain="[('partner_id', '=', partner_id)]", help='cloud ni toroku suru kanrigaisya.')
    dvr1 = fields.Many2one('product.product', string='dvr1', domain="[('type','=','product'), ('is_cloud','=',True)]")
    cam1 = fields.Integer('cam1')
    hdd1 = fields.Integer('hdd1', default='1')
    dvr2 = fields.Many2one('product.product', string='dvr2', domain="[('type','=','product'), ('is_cloud','=',True)]")
    cam2 = fields.Integer('cam2')
    hdd2 = fields.Integer('hdd2', default='1')
    dvr3 = fields.Many2one('product.product', string='dvr3', domain="[('type','=','product'), ('is_cloud','=',True)]")
    cam3 = fields.Integer('cam3')
    hdd3 = fields.Integer('hdd3', default='1')
    dvr4 = fields.Many2one('product.product', string='dvr4', domain="[('type','=','product'), ('is_cloud','=',True)]")
    cam4 = fields.Integer('cam4')
    hdd4 = fields.Integer('hdd4', default='1')
    sim_id = fields.Many2one('cloud.sim', string='SIM IP address', copy=False)
    memo = fields.Text('Memo')

    contractor_number = fields.Char('Contractor ID')
    contractor_pass = fields.Char('Contractor PASS')
    application_date = fields.Date('Apprication Date')
    approval_date = fields.Date('Approval Date')

    construction_date = fields.Date('Construction Date')
    #### auto input ### with constraction_date ###
    expiration_date = fields.Date('Expiration Date', store=True)
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
    def check(self):
        self.write({'state': 'check'})

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


class ProductTemplate(models.Model): 
    _inherit = 'product.template' 

    rate_id = fields.Many2one('cloud.rate.plan', 'CLOUD Rate Plan')



class CloudPartner(models.Model):
    _name = 'cloud.partner'
    _rec_name = 'name'

    name = fields.Char('Management Partner', required=True, help='Kanrigaisya toshite toroku sareru name.')
    address =  fields.Char('Management Partner address')
    phone = fields.Char('Management Partner phone')
    partner_id = fields.Many2one('res.partner', 'Partner name', required=True, help='Kanrigaisya wo motteiru partner.', 
                                 domain="[('company_type','=','company'), ('customer','=',True)]")
    management_number = fields.Char('Management ID')
    login_name = fields.Char('WEB login ID')
    login_pass = fields.Char('WEB login PASS') 
    mail1 = fields.Char('Mail Address 1')
    mail2 = fields.Char('Mail Address 2')
    mail3 = fields.Char('Mail Address 3')
