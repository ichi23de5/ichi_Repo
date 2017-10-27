# -*- coding: utf-8 -*-
import openerp.addons.decimal_precision as dp
from openerp import api, fields ,models, _


class Product(models.Model):
    _inherit = 'product.template'

    _sql_constraints = [('unique_name', 'unique(name, default_code)', 'Product name or Default code must be unique'),
                        ('barcode_uniq', 'unique(barcode)', _("A barcode can only be assigned to one product !")),]

    open_price = fields.Float('Vender Price', copy=True, digits=dp.get_precision('Product Price'))
    open_price_type = fields.Selection([  
           ('open', 'OPEN'), 
           ('value', 'Value')],          
           string='Open Price Selection', help='"  ": service nado openprice ga naimono. "OPEN": OPEN. "Value": teika wo nyuroku site.') 
    maker_id = fields.Many2one('res.partner', 'maker', domain="[('maker','=',True)]", help='TEC no Quotation ni kaku maker wo toroku sitene. res.partner no maker field to default_code field wo kanarazu touroku sitene.')

