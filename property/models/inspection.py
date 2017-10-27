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
    date = fields.Date('Date', copy=False,)
#    requester_id = fields.Many2one('res.partner', 'partner_id', domain="[('customer','=',True), ('company_type','=','company')]")
#    requester_rep_id = fields.Many2one('res.partner', 'Rep Name', domain="[('company_type','=','person'), ('parent_id', '=', property_ins_id.partner_id)]")
    request_note = fields.Text('request_note',)
    responder_id = fields.Many2one('res.users', 'user_id', help='hosyu no irai wo uketahitoy')

 
#    state = fields.Selection([
#        ('ongoing', 'Taioutyu'),
#        ('arranging', 'Tehaityu'),
#        ('finishing', 'Kanryo'),],
#        string='state')
    property_ins_id = fields.Many2one('property', 'Property inspection ID', index=True, ondelete='cascade', oldname='property_id')


    ### TKCLOUD Mail Notification ###
    symptom = fields.Char('Symptom', help='Tsuchi shita mail no syojo wo sonomama kaku. Shinkihassei no tokidake touroku suru.')
    mail_comment = fields.Char('Remarks', help='Tsuchi shita mail no Bikou wo sonomama kaku.')   

