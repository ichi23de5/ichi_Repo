# -*- coding: utf-8 -*-
from openerp import models, fields, api ,_


class Property(models.Model):
    _name = 'property'
    _order = 'name desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    ### property infomation ###
    name = fields.Char(string='Name', required=True, copy=False)
    phone = fields.Char(string='TEL', required=False, copy=False)
    address = fields.Char(string='ADDRESS', copy=False)    
    partner_name = fields.Many2one('res.partner', string='Partner', domain="[('customer','=',True), ('company_type','=','company')]")
    key = fields.Char(string="Key", help="Key or Auto lock number when locked")
    note = fields.Text(string='NOTE')



    ### warranty ###
    warranty_ids = fields.One2many('warranty','warranty_id', string='Warranty', help='Hosyu ga attara nyuryoku')
    ### inspection ###
    inspection_ids = fields.One2many('property.inspection','property_id', string='property_id')





class Warranty(models.Model):
    _name = 'warranty'
    _order = 'warranty_id desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _rec_name = 'warranty_id'

    warranty_id = fields.Many2one('product.product', string='Name', required=True)
    scope_of_covaerage = fields.Char(string='Scope of Covaerage')
    range_coverage = fields.Integer(string='range_coverage', required=True)
    active = fields.Boolean(string='Active')

