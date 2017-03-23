# -*- coding: utf-8 -*-

from openerp import api, fields ,models, _

class ResPartner(models.Model):
	_inherit = "res.partner"

        branch_id = fields.Char(string='Branch Office of Partner', readonly=False,)
        salesman_id = fields.Char(string='Business Partner Salesman', readonly=False, store=True,)

