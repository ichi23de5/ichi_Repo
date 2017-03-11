# -*- coding: utf-8 -*-

from openerp import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    relation_id  = fields.Many2one('hayashi', string='hayashi_lunch')
