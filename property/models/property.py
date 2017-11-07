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

    warranty_ids = fields.One2many('product.warranty','property_war_id', 'Warranty')
    inspection_ids = fields.One2many('property.inspection','property_ins_id', 'Inspection')
    so_count = fields.Integer('Sale Order', compute='_compute_so_count')

    @api.multi
    def _compute_so_count(self):
        for count in self:
            so = self.env['sale.order'].search([('property_id', '=', self.name)])
            count.so_count = len(so)
