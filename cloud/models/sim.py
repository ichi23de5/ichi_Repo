# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


class CloudSim(models.Model):
    _name = 'cloud.sim'
    _order = 'date_sim desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _rec_name = 'ip_address'

    user_number = fields.Char('SIM User Number', required=True, copy=False,)
    phone = fields.Char('SIM Tel Number', required=False, copy=False,)
    sim_id = fields.Many2one('sim.type', 'SIM Type ID')
    date_sim = fields.Datetime('Record Date', required=True, copy=False, default=fields.Datetime.now, help='SIM moushikonda date')
    iccid_number = fields.Char('Iccid Number', copy=False,)

    reception_date = fields.Date('Reception Date', required=True, copy=False, index=True,)
    #### auto input ### with reception_date ### 
    arrival_date = fields.Date('Arrival Date', store=True)
    charge_date = fields.Date('Charge Date', store=True)
    min_month = fields.Date('Minimum Usage Date', store=True)
    expiration_date = fields.Date('Expiration Date', store=True)
    ip_address = fields.Char('IP Address', copy=False, required=True)


    @api.onchange('reception_date')
    def _date_calc(self):
        main = fields.Datetime.from_string(self.reception_date)
        if main:
            arr = main + relativedelta(days=2)
            self.update({'arrival_date': arr})
            self.update({'charge_date': arr})
            min = main + relativedelta(days=2, months=12)
            self.update({'min_month': min})
            exp = main + relativedelta(days=2, months=24) 
            self.update({'expiration_date': exp})
            return





class CloudSimType(models.Model):
    _name = 'cloud.sim.type'
    _rec_name = 'name' 

    name = fields.Char('SIM Type ID', required=True, copy=False,)
    max_storage = fields.Char('Max Strage')
    business_number = fields.Char('Business Number')
    size_code = fields.Char('Size Code')
    deta_code = fields.Char('Kakinkaishibi')
    datermination = fields.Char('Sansyutuhouhou')
    pay_per_up = fields.Char('Juuryoukakin Up')
    pay_per_down = fields.Char('Juuryoukakin Down')
    min_use_time = fields.Char('Minimum Perion of Use')
    supplier_id = fields.Many2one('res.partner', 'Supplier', domain="[('supplier','=',True), ('company_type','=','company')]")


    ### charge ###
    basic_charge = fields.Integer('Basic Charge')
    cancel_charge = fields.Integer('Cancel Charge')
    admin_charge = fields.Integer('Admin Charge')
    ### commission ###
    opening_sim = fields.Integer('Opening Sim Commission')
    opening_sim_up = fields.Integer('Opening Sim Commission up')
    unreturned_sim = fields.Integer('Unreturned Sim Commission')
    reissure_sim = fields.Integer('Reissure Sim Commission')
    change_plan = fields.Integer('Change Plan Commission')
    change_size = fields.Integer('Change Size Commission')
    redelivery_sim = fields.Integer('Redelivery Sim Commission')
    stop_sim = fields.Integer('Stop Sim Commission')
    delivery_sim = fields.Integer('Delivery Sim Commission')
    universal_service = fields.Integer('Universal Service Commission')
    cancel_charge_first = fields.Integer('Cancel Charge 1month')
    cancel_charge_year = fields.Integer('Cancel Charge Year')
    charge100 = fields.Integer('100MB')
    charge500 = fields.Integer('500MB')
    charge1000 = fields.Integer('1000MB')
    ip_month = fields.Integer('IP Charge')
    date_model = fields.Char('Date Model')

