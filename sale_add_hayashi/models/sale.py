# -*- coding: utf-8 -*-

from openerp import api, fields ,models,  _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'



    check_state = fields.Selection([
         ('stand', 'Check waiting'),
         ('ng', 'Check NG'),
         ('manager', 'Manager OK'),
         ('president', 'President OK'),
         ], string='State2', readonly=True, copy=False, index=True, track_visibility='onchange', default='ng')
    property_id = fields.Many2one('property', string='Property Name', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    order_date = fields.Datetime(string='Create Date', default=fields.Datetime.now, required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    rep_partner_id = fields.Many2one('res.partner', string='Rep Name', required=True, domain="[('company_type','=','person')]")
    assistant_id = fields.Many2one('res.users', string='Assistant', copy=False)
    work_type = fields.Selection([
        ('new', 'New construction'),
        ('renewal', 'ReNewal'),
        ('add', 'Extention'),
        ('building', 'Shinchiku'),
        ('inspection', 'Inspection'),
        ('goods', 'Sale of Product'),
        ('other', 'Others')
        ],
        string='Type', required=True, default='new', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    version = fields.Char(string='Plan version', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    completion_date = fields.Date(string='Syunkoubi', states={'draft': [('invisible', True)], 'sent': [('invisible', True)]})


    ### construction field for (old) purchase order ###
    construction_type = fields.Selection([
        ('toki', 'TOKI'),
        ('outside', 'Gaichu'),
        ('both', 'Ryouhou')
        ], string='Work', default='toki')
    outside_order = fields.Boolean('Outside order', default=False)
    ### construction TOKI ###
    start_date = fields.Date(string='Kouji start')
    end_date = fields.Date(string='Kouji end')
    start_time = fields.Char(string='Start time')
    end_time = fields.Char(string='End time')
    construction_title = fields.Char('title', help='Kouzibu he order suru gaiyou. ex:Camera 3dai kouzi.')
    construction_ids = fields.One2many('sale.construction','list_id', string='yokutsukau tokkizikou model', store=True)
    construction_note = fields.Text(string='Others', help='Sonota tokkizikou')
    ### construction OUTSIDE ORDER ###
    outside_id = fields.Many2one('res.partner', string='Outside Supplier', domain="[('outside_order','=',True)]")
    amount_outside = fields.Monetary(string='Gaityukingaku')
    start_date_o = fields.Date(string='Kouji start')
    end_date_o = fields.Date(string='Kouji end')
    start_time_o = fields.Char(string='Start time')
    end_time_o = fields.Char(string='End time')
    construction_title_o = fields.Char('title', help='Kouzibu he order suru gaiyou. ex:Camera 3dai kouzi.')
    construction_ids_o = fields.One2many('sale.construction','list_id', string='yokutsukau tokkizikou model', store=True)
    construction_note_o = fields.Text(string='Others', help='Sonota tokkizikou')





    @api.onchange('construction_type') 
    def onchange_construction_type(self): 
        self.outside_order = (self.construction_type == 'outside' or self.construction_type == 'both')



    @api.onchange('order_date')
    def _date_exp(self):
        main = fields.Datetime.from_string(self.order_date)
        if main:
            exp = main + relativedelta(months=3)
            self.update({'validity_date': exp})
            return




    confirmation_date = fields.Datetime(string='Confirmation Date',
                                        readonly=True,
                                        index=True, help="Date on which the sale order is confirmed.",
                                        oldname="date_confirm")


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


    request_flag = fields.Boolean('request')

    @api.multi
    def request(self):
        self.write({'check_state': 'stand'})
        self.write({'request_flag': True})

    @api.multi
    def manager_ok(self):
        self.write({'check_state': 'manager'})


    @api.multi
    def manager_ng(self):
        self.write({'check_state': 'ng'})

    @api.multi
    def president(self):
        self.write({'check_state': 'president'})



class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    open_price = fields.Char(string='Open Price', related='product_id.open_price', required=True, store=True)
    maker = fields.Char(string='Maker', related='product_id.maker_id.default_code', store=True)


class Construction(models.Model):
    _name = 'sale.construction'
    _rec_name = 'list_id'

    list_id = fields.Many2one('sale.construction.list', string='template')


class ConstructionList(models.Model):
    _name = 'sale.construction.list'
    _rec_name = 'list_id'


    list_id = fields.Char(string='template', required=True)
    note = fields.Text(string='memo')

