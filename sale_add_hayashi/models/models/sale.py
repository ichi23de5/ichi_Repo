# -*- coding: utf-8 -*-

from openerp import api, fields ,models, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import openerp.addons.decimal_precision as dp



class SaleOrder(models.Model):
    _inherit = "sale.order"


#       = fields.('', string='', readonly=True, store=True, copy=False, required=True, related='')

    inspection_id = fields.Many2one('inspection', string='Inspection')
    construction_date = fields.Date(string='Constraction Date', store=True)
#    completion_date = fields.Date(string='Completion Date', store=True)
    property_id = fields.Many2one('property', string='Property Name')
    order_date = fields.Date(string='Order Date')
    assistant = fields.Many2one('res.users', string='Assistant')
    tkcloud_id = fields.Many2one('cloud', string='TKCLOUD')
    work_type = fields.Selection([
        ('new', 'New construction'),
        ('renewal', 'ReNewal'),
        ('add', 'Extention'),
        ('inspection', 'Inspection'),
        ('goods', 'Sale of Product'),
        ('other', 'Others')
        ], 
        string='Type', required=True, default='new')
    plan_id = fields.Char(string='Plan version')


    @api.onchange('create_date')
    def _date_exp(self):
        main = fields.Datetime.from_string(self.create_date)
        if main:
            exp = main + relativedelta(months=3)
            self.update({'validity_date': exp})
            return



    confirmation_date = fields.Datetime(string='Confirmation Date', readonly=True, index=True, help="Date on which the sale order is confirmed.", oldname="date_confirm")

    @api.multi 
    def action_confirm(self): 
        for order in self: 
            order.state = 'sale' 
            order.confirmation_date = fields.Datetime.now() 
            if self.env.context.get('send_email'): 
                self.force_quotation_send() 
            order.order_line._action_procurement_create() 
        if self.env['ir.values'].get_default('sale.config.settings', 'auto_done_setting'): 
            self.action_done() 
        return True 



    @api.multi
    def flag_a(self):
        pass




class SaleOrderLine(models.Model):
    _inherit = "sale.order.line" 

    open_price = fields.Char(string='Open Price', related='product_id.open_price', required=True)

