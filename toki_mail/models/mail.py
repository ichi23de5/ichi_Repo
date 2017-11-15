# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta

class MailMessage(models.Model):
    _inherit = 'mail.message'

    mail_agg_id = fields.Many2one('mail.aggregate', 'Mail Aggregate', ondelete='cascade',)



class MailAggregate(models.Model):
    _name = 'mail.aggregate'

    mail_message_ids = fields.One2many('mail.message','mail_agg_id', 'Mail Message')

#    property_id = fields.Many2one('property', 'Property')
    property = fields.Char('Property')
    
