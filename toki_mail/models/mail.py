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

    @api.multi
    def compute_mail(self):
        messages = self.env['mail.message']
        msg_count = messages.search_count(['message_type', '=', 'email'])    
#        msg_count = len('messages.id')
        name = "There are " + str(msg_count) + " messages in Box!"
        self.create({ "property" : name })
 
