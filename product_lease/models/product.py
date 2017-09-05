# -*- coding: utf-8 -*-

from openerp import api, fields ,models, _

class ProductTemplate(models.Model):
	_inherit = "product.template"

    lease_names = fields.Many2many("product.lease", string='Lease Name', copy=True)



class ProductLease(models.Model):
    _name = "product.lease"
    _rec_name = 'lease_num'

    name = fields.Char(string="NAME", required=True)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    active = fields.Boolean(string="Active")
    lease_num = fields.Char(string="Lease ID", required=True)

