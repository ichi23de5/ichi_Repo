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
    warranty_ids = fields.One2many('product.warranty','property_war_id', string='Warranty')
    ### inspection ###
    inspection_ids = fields.One2many('property.inspection','property_ins_id', string='Inspection')





class ProductWarranty(models.Model):
    _name = 'product.warranty'
    _order = 'warranty_id desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _rec_name = 'warranty_id'

    warranty_id = fields.Many2one('product.product', 'Name', required=True, domain="[('is_warranty','=',True)]")
    scope_of_covaerage = fields.Char('Scope of Covaerage')
    range_coverage = fields.Integer('range_coverage', required=True)
    active = fields.Boolean('Active')

    property_war_id = fields.Many2one('property', 'Property warranty ID', index=True, ondelete='cascade', oldname='property_id')

