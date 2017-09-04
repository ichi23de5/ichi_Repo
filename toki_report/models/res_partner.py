# -*- coding: utf-8 -*-

from openerp import api, fields ,models

class PartnerTemplate(models.Model):
    _name = 'res.partner.quotation.template'
    _rec_name = 'name'

    name = fields.Char('Template Name', required=True)
    image = fields.Binary('Image')
    ### Display flag Quotation order ###
    maker_flag = fields.Boolean('Display Maker Name')
    code_flag = fields.Boolean('Display Code', help='Tansyukukataban wo hyouji sezu seishiki kataban wo dasu.')
    warranty_flag = fields.Boolean('Display Warranty period', help='Hosyokikan wo hyouji')

class ResPartner(models.Model):
    _inherit = "res.partner"

    quotation_template = fields.Many2one('res.partner.quotation.template', 'Quotation template')
