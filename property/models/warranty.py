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
    property_war_id = fields.Many2one('property', 'Property warranty ID', index=True, ondelete='cascade', oldname='property_id')

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
    date = fields.Date('Date')
    type = fields.Selection([
        ('teiki', 'Teiki tenken'),
        ('end', 'Warranty End')],
        'Type')
    finish = fields.Boolean('Finish')

    warranty_sch_id = fields.Many2one('product.warranty', 'Property warranty ID', index=True, ondelete='cascade', oldname='property_id')





class Product(models.Model):
    _inherit = 'product.template'

    is_warranty = fields.Boolean('Warranty Flag')
    scope_of_coverage = fields.Char('Scope of Coverage')
    range_coverage = fields.Integer('range_coverage')
    count_inspection = fields.Integer('Inspection Count')
