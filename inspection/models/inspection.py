# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta, date

class Inspection(models.Model):
    _name = 'inspection'
    _order = 'date desc'

 
    property_id = fields.Many2one("property",string="Property", required=True, delegate=True, ondelete='cascade')
    date = fields.Date(string='date', required=True,)
    inspector_id = fields.Many2one("res.users", string="Inspector")
    act_type = fields.Selection([
        ('inspect', 'Tenken'),
        ('routine_inspection', 'Teikitenken'),
        ('change', 'Koukan'),
        ('repair', 'Syuri'),
        ('coordinate', 'Tyousei'),
        ('others', 'Other'),],
        string='Act type')
    inspection_note = fields.Text(string='inspection_note',)
    product_memo = fields.Char(string='product_memo',)
    request_id = fields.Many2one('inspection.request', string='Request')
    request_date = fields.Date(string='request_date', related='request_id.date', readonly=True)
    requester_name = fields.Char(string='requester_name', related='request_id.partner_id.name', readonly=True)
    request_note = fields.Text(string='request_note', related='request_id.request_note', readonly=True)
    responder_name = fields.Char(string='responder_name', related='request_id.user_id.name', readonly=True)
    state = fields.Selection([
        ('ongoing', 'Taioutyu'),
        ('arranging', 'Tehaityu'),
        ('finishing', 'Kanryo'),],
        string='state')


class InspectionRequest(models.Model):
    _name = 'inspection.request'
    _order = 'date desc'


    date = fields.Date(string='Date', required=True, copy=False,)
    partner_id = fields.Many2one('res.partner', string='partner_id',)
    request_note = fields.Text(string='request_note',)
    user_id = fields.Many2one('res.users', string='user_id', required=True,)
    name = fields.Char(string='Name')
    
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('inspection.request') or 'New'
        result = super(InspectionRequest, self).create(vals)
        return result

