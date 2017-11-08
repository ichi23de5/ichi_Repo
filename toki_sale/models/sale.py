# -*- coding: utf-8 -*-
import openerp.addons.decimal_precision as dp
from openerp import api, fields ,models,  _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from openerp.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    check_state = fields.Selection([
         ('stand', 'Check waiting'),
         ('ng', 'Check NG'),
         ('manager', 'Manager OK'),
         ('president', 'President OK'),
         ], 'State2', readonly=True, copy=False, index=True, default='ng')
    property_id = fields.Many2one('property', 'Property Name', readonly=True, index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    order_date = fields.Datetime('Create Date', default=fields.Datetime.now, required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    rep_partner_id = fields.Many2one('res.partner', string='Rep Name', required=False, domain="[('company_type','=','person'), ('parent_id', '=', partner_id)]", readonly=True, index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    assistant_id = fields.Many2one('res.users', 'Sub User', copy=False)
    work_type = fields.Selection([
        ('new', 'New construction'),
        ('renewal', 'ReNewal'),
        ('add', 'Extention'),
        ('building', 'Shinchiku'),
        ('inspection', 'Hosyu Tenken'),
        ('goods', 'Sale of Product'),
        ('other', 'Others')
        ],
        string='Type', required=True, default='new', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    version = fields.Char('Plan version', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    purchase_order = fields.Boolean('Purchase order', copy=False)
    inspection_id = fields.Many2one('property.inspection', 'Inspection', help='Kokokara hosyujouhou nyuryoku')

    ### construction field for (old) purchase order ###
    construction_type = fields.Selection([
        ('toki', 'TOKI'),
        ('outside', 'Gaichu'),
        ('both', 'Ryouhou')
        ], string='Work', default='toki')
    outside_order = fields.Boolean('Outside order', default=False)
    ### construction TOKI ###
    start_date = fields.Date('Kouji start')
    end_date = fields.Date('Kouji end')
    start_time = fields.Char('Start time')
    end_time = fields.Char('End time')
    construction_title = fields.Char('title', help='Kouzibu he order suru gaiyou. ex:Camera 3dai kouzi.')
    construction_ids = fields.One2many('sale.construction','order_id', string='yokutsukau tokkizikou model', store=True)
    construction_note = fields.Text('Others', help='Sonota tokkizikou')
    ### construction OUTSIDE ORDER ###
    outside_id = fields.Many2one('res.partner', 'Outside Supplier', domain="[('outside_order','=',True)]")
    amount_outside = fields.Integer('Gaityukingaku')
    start_date_o = fields.Date('Kouji start')
    end_date_o = fields.Date('Kouji end')
    start_time_o = fields.Char('Start time')
    end_time_o = fields.Char('End time')
    construction_title_o = fields.Char('title', help='Kouzibu he order suru gaiyou. ex:Camera 3dai kouzi.')
    construction_ids_o = fields.One2many('sale.construction','order_o_id', string='yokutsukau tokkizikou model', store=True)
    construction_note_o = fields.Text('Others', help='Sonota tokkizikou')
    memo = fields.Text('memo')

    direct_flag = fields.Boolean('Direct transaction')
    @api.onchange('partner_id')
    def _flag_direct_transaction(self):
        direct = self.partner_id.direct_transaction
        if direct:
            self.update({'direct_flag':True})
            return


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

    ### check_state move ###
    request_flag = fields.Boolean('request', copy=False)

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

    @api.multi 
    def action_cancel(self): 
        self.write({'state': 'cancel'}) 
        self.write({'request_flag': False})
        self.write({'check_state': 'ng'})


    ### onchange pricelist with partner_id  ###
    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        Update the following fields when the partner is changed:
        - Pricelist
        - Payment term
        - Invoice address
        - Delivery address
        """
        if not self.partner_id:
            self.update({
                'partner_invoice_id': False,
                'partner_shipping_id': False,
                'payment_term_id': False,
                'fiscal_position_id': False,
            })
            return

        addr = self.partner_id.address_get(['delivery', 'invoice'])
        values = {
            'pricelist_id': self.partner_id.property_product_pricelist and self.partner_id.property_product_pricelist.id or False,
            'payment_term_id': self.partner_id.property_payment_term_id and self.partner_id.property_payment_term_id.id or False,
            'partner_invoice_id': addr['invoice'],
            'partner_shipping_id': addr['delivery'],
        }
        if self.env.user.company_id.sale_note:
            values['note'] = self.with_context(lang=self.partner_id.lang).env.user.company_id.sale_note

        if self.partner_id.user_id:
            values['user_id'] = self.partner_id.user_id.id
        if self.partner_id.team_id:
            values['team_id'] = self.partner_id.team_id.id
        self.update(values)

        for line in self.order_line:
        
            if line.order_id.pricelist_id and line.order_id.partner_id:
                product = line.product_id.with_context(
                    lang=line.order_id.partner_id.lang,
                    partner=line.order_id.partner_id.id,
                    quantity=line.product_uom_qty,
                    date=line.order_id.date_order,
                    pricelist=line.order_id.pricelist_id.id,
                    uom=line.product_uom.id,
                    fiscal_position=line.env.context.get('fiscal_position')
                )

            product_price = self.env['account.tax']._fix_tax_included_price(product.price, product.taxes_id, line.tax_id)
            line.update({'price_unit': product_price})
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
            line.update({
                'price_tax': taxes['total_included'] - taxes['total_excluded'],
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })






class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    chr_open_price = fields.Float('Open Price', related='product_id.open_price', digits=dp.get_precision('Product Price'))
    open_price = fields.Char('Open Price', digits=dp.get_precision('Product Price'))
    maker = fields.Char('Maker', related='product_id.maker_id.default_code')
    description_sale = fields.Char('SO Explanation')

    ### Open price for display ###
    @api.onchange('product_id')
    def _compute_openprice(self):
        self.ensure_one()
        st = ""
        if not self.product_id.open_price_type:
            st = ""
        elif self.product_id.open_price_type == "open":
            st = "OPEN"
        elif self.product_id.open_price_type == "value":
            st = str(self.product_id.open_price)
        return self.update({"open_price": st })

    @api.onchange('product_id')
    def _onchange_description(self):
        ds = self.product_id.description_sale
        if ds:
            self.update({"description_sale": ds})
            return






class Construction(models.Model):
    _name = 'sale.construction'
    _rec_name = 'template_id'

    template_id = fields.Many2one('sale.construction.list', 'Template')

    order_id = fields.Many2one('sale.order', 'Order Reference', ondelete='cascade', copy=False, index=True)
    order_o_id = fields.Many2one('sale.order', 'Order Reference', ondelete='cascade', copy=False, index=True)
    


class ConstructionList(models.Model):
    _name = 'sale.construction.list'
    _rec_name = 'template'


    template = fields.Char(string='template', required=True)
    note = fields.Text(string='memo')
