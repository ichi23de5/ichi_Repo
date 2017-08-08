# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


class Inspection(models.Model):
    _name = 'property.inspection'
    _order = 'date desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']


    ### inspection ###
    date = fields.Date('Date', required=True,)
    inspector_id = fields.Many2one('res.users', 'Inspector', help='Inspection zikkoushitahito. Fukusu iru baai ha daihyosya.')
    act_type = fields.Selection([
        ('inspect', 'Tenken'),
        ('routine_inspection', 'Teikitenken'),
        ('change', 'Koukan'),
        ('repair', 'Syuri'),
        ('coordinate', 'Tyousei'),
        ('others', 'Other'),
        ('mail', 'Mail Notification'),
        ], 'Act type')
    inspection_note = fields.Text('Note')
    product_memo = fields.Text('product_memo', help='Koukan sita kiki wo kaitene')
    ### request ###
    request_id = fields.Many2one('property.inspection.request', 'Request')
    requester_name = fields.Char('requester_name', related='request_id.partner_id.name', readonly=True)
    requester_rep_name = fields.Char('requester_name', related='request_id.rep_partner_id.name', readonly=True)
    request_note = fields.Text('request_note', related='request_id.request_note', readonly=True)
    responder_name = fields.Char('responder_name', related='request_id.user_id.name', readonly=True)
 
#    state = fields.Selection([
#        ('ongoing', 'Taioutyu'),
#        ('arranging', 'Tehaityu'),
#        ('finishing', 'Kanryo'),],
#        string='state')
    property_ins_id = fields.Many2one('property', 'Property inspection ID', index=True, ondelete='cascade', oldname='property_id')


    ### TKCLOUD Mail Notification ###
    symptom = fields.Char('Symptom', help='Tsuchi shita mail no syojo wo sonomama kaku. Shinkihassei no tokidake touroku suru.')
    mail_comment = fields.Char('Remarks', help='Tsuchi shita mail no Bikou wo sonomama kaku.')   

class InspectionRequest(models.Model):
    _name = 'property.inspection.request'
    _order = 'date desc'
    _rec_name = 'date'

    date = fields.Date('Date', required=True, copy=False,)
    partner_id = fields.Many2one('res.partner', 'partner_id', required=True, domain="[('customer','=',True), ('company_type','=','company')]")
    rep_partner_id = fields.Many2one('res.partner', 'Rep Name', required=True, domain="[('company_type','=','person'), ('parent_id', '=', partner_id)]")
    request_note = fields.Text('request_note',)
    user_id = fields.Many2one('res.users', 'user_id', required=True, help='hosyu no irai wo uketahitoy')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('inspection.request') or 'New'
        result = super(InspectionRequest, self).create(vals)
        return result

