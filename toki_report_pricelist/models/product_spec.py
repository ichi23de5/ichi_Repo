# -*- coding: utf-8 -*-

from openerp import api, fields ,models

class ResPartner(models.Model):
    _inherit = "product.template"

    spec_note = fields.Text('Spec')
    spec_remarks = fields.Char('Remarks Column')
