# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


class Inspection(models.Model):
    _name = 'property.inspection'
    _order = 'date desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']


    property_id = fields.Many2one('property', string='Property ID', required=True, readonly=True)
    ### inspection ###
    date = fields.Date(string='Date', required=True,)
    inspector_id = fields.Many2one('res.users', string='Inspector')
    act_type = fields.Selection([
        ('inspect', 'Tenken'),
        ('routine_inspection', 'Teikitenken'),
        ('change', 'Koukan'),
        ('repair', 'Syuri'),
        ('coordinate', 'Tyousei'),
        ('others', 'Other'),],
        string='Act type')
    inspection_note = fields.Text(string='Note')
    product_memo = fields.Text(string='product_memo', help='Koukan sita kiki wo kaitene')
    ### request ###
    request_id = fields.Many2one('property.inspection.request', string='Request')
    requester_name = fields.Char(string='requester_name', related='request_id.partner_id.name', readonly=True)
    requester_rep_name = fields.Char(string='requester_name', related='request_id.rep_partner_id.name', readonly=True)
    request_note = fields.Text(string='request_note', related='request_id.request_note', readonly=True)
    responder_name = fields.Char(string='responder_name', related='request_id.user_id.name', readonly=True)
    ### ###
    state = fields.Selection([
        ('ongoing', 'Taioutyu'),
        ('arranging', 'Tehaityu'),
        ('finishing', 'Kanryo'),],
        string='state')



class InspectionRequest(models.Model):
    _name = 'property.inspection.request'
    _order = 'date desc'
    _rec_name = 'date'

    date = fields.Date(string='Date', required=True, copy=False,)
    partner_id = fields.Many2one('res.partner', string='partner_id', required=True, domain="[('customer','=',True), ('company_type','=','company')]")
    rep_partner_id = fields.Many2one('res.partner', string='Rep Name', required=True, domain="[('company_type','=','person'), ('parent_id', '=', partner_id)]")
    request_note = fields.Text(string='request_note',)
    user_id = fields.Many2one('res.users', string='user_id', required=True, help='hosyu no irai wo uketahitoy')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('inspection.request') or 'New'
        result = super(InspectionRequest, self).create(vals)
        return result

