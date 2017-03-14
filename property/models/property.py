# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


class Property(models.Model):
    _name = 'property'
    _order = 'property_name desc'


    property_name = fields.Char(string='Name', required=True, copy=False,)
    phone = fields.Char(string='TEL', required=False, copy=False,)
    zip = fields.Char(string='ZIP',)
    property_addr = fields.Char(string='ADDRESS', copy=False,)    
    partner_id = fields.Many2one('res.partner', string='Partner',)
    rep_name_id = fields.Many2one('res.partner', string='Rep_Name',)
    note = fields.Text(string='NOTE',)

