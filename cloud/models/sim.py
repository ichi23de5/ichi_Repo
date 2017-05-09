# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


class Sim(models.Model):
    _name = 'sim'
    _order = 'date_sim desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _rec_name = 'user_number'

    user_number = fields.Char(string='SIM User Number', required=True, copy=False,)
    phone = fields.Char(string='SIM Tel Number', required=False, copy=False,)
    sim_id = fields.Many2one('sim.type', string='SIM Type ID')
    date_sim = fields.Datetime(string='Record Date', required=True, index=True, copy=False, default=fields.Datetime.now,)
    iccid_number = fields.Char(string='Iccid Number', copy=False,)

    reception_date = fields.Date(string='Reception Date', required=True, copy=False, store=True, index=True,)
    #### auto input ### with reception_date ### 
    arrival_date = fields.Date(string='Arrival Date', store=True)
    charge_date = fields.Date(string='Charge Date', store=True)
    min_month = fields.Date(string='Minimum Usage Date', store=True)
    expiration_date = fields.Date(string='Expiration Date', store=True)
    ip_address = fields.Char('IP Address')


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





class SimType(models.Model):
    _name = 'sim.type'
    _rec_name = 'sim_type_id' 

    sim_type_id = fields.Char(string='SIM Type ID', required=True, copy=False,)
    max_storage = fields.Char(string='Max Strage')
    business_number = fields.Char(string='Business Number')
    size_code = fields.Char(string='Size Code')
    deta_code = fields.Char(string='Kakinkaishibi')
    datermination = fields.Char(string='Sansyutuhouhou')
    pay_per_up = fields.Char(string='Juuryoukakin Up')
    pay_per_down = fields.Char(string='Juuryoukakin Down')
    min_use_time = fields.Char(string='Minimum Perion of Use')
    supplier_id = fields.Many2one('res.partner', string='Supplier', domain="[('supplier','=',True)]")


    ### charge ###
    basic_charge = fields.Integer(string='Basic Charge')
    cancel_charge = fields.Integer(string='Cancel Charge')
    admin_charge = fields.Integer(string='Admin Charge')
    ### commission ###
    opening_sim = fields.Integer(string='Opening Sim Commission')
    opening_sim_up = fields.Integer(string='Opening Sim Commission up')
    unreturned_sim = fields.Integer(string='Unreturned Sim Commission')
    reissure_sim = fields.Integer(string='Reissure Sim Commission')
    change_plan = fields.Integer(string='Change Plan Commission')
    change_size = fields.Integer(string='Change Size Commission')
    redelivery_sim = fields.Integer(string='Redelivery Sim Commission')
    stop_sim = fields.Integer(string='Stop Sim Commission')
    delivery_sim = fields.Integer(string='Delivery Sim Commission')
    universal_service = fields.Integer(string='Universal Service Commission')
    cancel_charge_first = fields.Integer(string='Cancel Charge 1month')
    cancel_charge_year = fields.Integer(string='Cancel Charge Year')
    charge100 = fields.Integer(string='100MB')
    charge500 = fields.Integer(string='500MB')
    charge1000 = fields.Integer(string='1000MB')
    ip_month = fields.Integer(string='IP Charge')
    date_model = fields.Char(string='Date Model')

