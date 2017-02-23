# -*- coding: utf-8 -*-
#    Odoo, Open Source Management Solution
#    Copyright TOYOKIKI INC.
#    <https://www.toyo-kiki.co.jp>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    plan_id = fields.Char(string='Plan Name',copy=True, help="Plan Name for Quotation")
    complete_date = fields.Date('Complete Date')
    assistant_id = fields.Many2one('res.users', string='Assistant')
    sim_id = fields.Char(string='Sim')
    complete2_date = fields.Date('Complete Date')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
