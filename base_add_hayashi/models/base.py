# -*- coding: utf-8 -*-

from openerp import api, fields ,models



class ResPartner2(models.Model):
    _inherit = "res.partner"


#       = fields.('', string='', readonly=True, store=True, copy=False, required=True, related='')


    outside_order = fields.Boolean(string="Outside Flag")


