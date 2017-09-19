# -*- coding: utf-8 -*-

from openerp import api, fields ,models

class ResPartner(models.Model):
    _inherit = 'product.template'

    spec_note = fields.Text('Spec')
    spec_remarks = fields.Char('Remarks Column')
    video_system = fields.Many2one('product.video.system', 'Video System')



class ProductVideoSystem(models.Model):
    _name = 'product.video.system'
    _rec_name = 'name'

    name = fields.Char('Video System Name')
