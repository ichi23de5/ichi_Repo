# -*- coding: utf-8 -*-
from openerp import models, fields, api ,_
#from datetime import datetime, timedelta, date
#from dateutil.relativedelta import relativedelta


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

    ### need sale_balus module ###
#    primary_order = fields.Many2one('sale.order', string='Primary Order', store=True)
#    primary_order_date = fields.Date(related='property_order.completion_id', string='Primary Order Date', store=True)

    dvr1 = fields.Many2one('product.product', string='dvr1')
    dvr2 = fields.Many2one('product.product', string='dvr2')
    dvr3 = fields.Many2one('product.product', string='dvr3')
    dvr4 = fields.Many2one('product.product', string='dvr4')



    ### warranty ###
    warranty_ids = fields.One2many('warranty','name', string='Warranty', help='Hosyu ga attara nyuryoku')
    ### inspection ###
    inspection_ids = fields.One2many('property.inspection','property_id', string='property_id',)




    @api.model 
    def create(self, vals): 
        if vals.get('name', 'New') == 'New': 
            vals['name'] = self.env['ir.sequence'].next_by_code('property') or 'New' 
        result = super(Property, self).create(vals) 
        return result 






class Warranty(models.Model):
    _name = 'warranty'
    _order = 'name desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _rec_name = 'name'

    name = fields.Many2one('product.product', string='Name', required=True)
    scope_of_covaerage = fields.Char(string='Scope of Covaerage')
    range_coverage = fields.Integer(string='range_coverage', required=True)
    active = fields.Boolean(string='Active')

