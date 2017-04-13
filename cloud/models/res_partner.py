# -*- coding: utf-8 -*-
from openerp import api, fields ,models, _


class Partner(models.Model):
    _inherit = "res.partner"

    prefix_code = fields.Char(string="Prefix Code", size=3) 
