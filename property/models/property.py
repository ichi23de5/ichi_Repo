# -*- coding: utf-8 -*-
from openerp import models, fields, api ,_


class Property(models.Model):
    _name = 'property'
    _order = 'name desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    ### property infomation ###
    name = fields.Char('Name', required=True, copy=False)
    phone = fields.Char('TEL', required=False, copy=False)
    address = fields.Char('ADDRESS', copy=False)    
    partner_id = fields.Many2one('res.partner', 'Partner', domain="[('customer','=',True), ('company_type','=','company')]")
    key = fields.Char('Key', help="Key or Auto lock number when locked")
    note = fields.Text('Note')

    ### warranty ###
    warranty_ids = fields.One2many('product.warranty','property_war_id', 'Warranty')
    ### inspection ###
    inspection_ids = fields.One2many('property.inspection','property_ins_id', 'Inspection')





class ProductWarranty(models.Model):
    _name = 'product.warranty'
    _order = 'warranty_id desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _rec_name = 'warranty_id'

    warranty_id = fields.Many2one('product.product', 'Name', required=True, domain="[('is_warranty','=',True)]")
    scope_of_coverage = fields.Char('Scope of Covaerage')
    range_coverage = fields.Integer('range_coverage', required=True)

    property_war_id = fields.Many2one('property', 'Property warranty ID', index=True, ondelete='cascade', oldname='property_id')

