# -*- coding: utf-8 -*-
from openerp import models, fields, api
# Non-odoo library
# import random
# from random import randint
# import string

class Warranty(models.Model):
    _name = 'warranty'
    _order = 'name desc'

    name = fields.Many2one('product.product', string='Name', required=True)
#    name = fields.Char(string='Name', required=True)
    scope_of_covaerage = fields.Char(string='Scope of Covaerage')
    range_coverage = fields.Integer(string='range_coverage', required=True)
    active = fields.Boolean(string='Active')
#    user_id = fields.Many2one('res.users',string='User')
