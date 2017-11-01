# -*- coding: utf-8 -*-
from openerp import models, fields, api ,_
from dateutil.relativedelta import relativedelta
from openerp.exceptions import UserError

class ProductWarranty(models.Model):
    _name = 'product.warranty'
    _order = 'warranty_id desc'
    _rec_name = 'warranty_id'

    warranty_id = fields.Many2one('product.template', 'Name', required=True, domain="[('is_warranty','=',True)]")
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    action = fields.Boolean('Action')
    property_war_id = fields.Many2one('property', 'Property warranty ID', index=True, ondelete='cascade', oldname='property_id', readonly=True)

    warranty_sch_ids = fields.One2many('product.warranty.schedule','warranty_sch_id', 'Schedule')

    @api.onchange('start_date')
    def onchange_period(self):
        start = fields.Date.from_string(self.start_date)
        period = self.warranty_id.range_coverage
        if start:
            exp = start + relativedelta(years=period)
            self.update({'end_date': exp})
            return

class ProductWarrantySchedule(models.Model):
    _name = 'product.warranty.schedule'
    _order = 'type desc'
    _rec_name = 'warranty_id'

    warranty_id = fields.Many2one('product.template', 'Name', domain="[('is_warranty','=',True)]")
    date = fields.Date('Date', help='Tenken iku meyasu no hi.')
    type = fields.Selection([
        ('teiki', 'Teiki tenken'),
        ('end', 'Warranty End')],
        'Type')
    finish = fields.Boolean('Finish')
    property_id = fields.Many2one('property', 'Property Name', related='warranty_sch_id.property_war_id', readonly=True)

    warranty_sch_id = fields.Many2one('product.warranty', 'Property warranty ID', index=True, ondelete='cascade')





class Product(models.Model):
    _inherit = 'product.template'

    is_warranty = fields.Boolean('Warranty Flag')
    scope_of_coverage = fields.Char('Scope of Coverage')
    range_coverage = fields.Integer('range_coverage')
    count_inspection = fields.Integer('Inspection Count')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def test_button(self):
        val_set = {}
        if any(line.product_tmpl_id.is_warranty == 1 for line in self.order_line):
            start = fields.Date.from_string(self.completion_date)
            for line in self.order_line:
                if line.product_tmpl_id.is_warranty == 1:
                    period = line.product_id.range_coverage
                    exp = start + relativedelta(years=period)
                    self.env['product.warranty'].create({
                        'warranty_id' : line.product_id.id,
                        'range_coverage' : period,
                        'property_war_id' : line.order_id.property_id.id,
#                        'active' : True,
                        'start_date' : line.order_id.completion_date,
                        'end_date' : exp,
                })
        else:
            raise UserError("Warranty item ga arimasen!!")
        return
