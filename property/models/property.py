# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


class Property(models.Model):
    _name = 'property'
    _order = 'name desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    ### property infomation ###
    name = fields.Char(string='Name', required=True, copy=False,)
    phone = fields.Char(string='TEL', required=False, copy=False,)
    address = fields.Char(string='ADDRESS', copy=False,)    
    partner_name = fields.Many2one('res.partner', string='Partner',)
#    rep_name = fields.Many2one('res.partner', string='Rep_Name',)
    key = fields.Char(string="Key", help="Key or Auto lock number when locked")
    note = fields.Text(string='NOTE',)

    ### warranty ###
    warranty_ids = fields.One2many('warranty','name', string='Warranty',)

    ### inspection ###
    inspection_ids = fields.One2many('inspection','order_id', string='property_id',)

    ### infomation of introduction ###
#    introduction_name = fields.Char(string='Introduction Name', related='inspection_line.sale.order.name',)
#    complection_date = fields.Date(string='Complection Date', related='inspection_line.sale.order.complection_date')



    @api.model 
    def create(self, vals): 
        if vals.get('name', 'New') == 'New': 
            vals['name'] = self.env['ir.sequence'].next_by_code('property') or 'New' 
        result = super(Property, self).create(vals) 
        return result 

