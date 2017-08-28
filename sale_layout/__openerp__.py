# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Layout TOKI',
    'version': '1.0',
    'sequence': 14,
    'summary': 'Sale Layout, page-break, subtotals, separators, report',
    'description': """ 
Sale layout wo TOKI kaizou!
    """,
    'depends': ['sale', 'report'],
    'category': 'Sales',
    'data': ['views/sale_layout_category_view.xml',
             'views/report_invoice_layouted.xml',
             'views/report_quotation_layouted.xml',
             'views/sale_layout_template.xml',
             'security/ir.model.access.csv'],
    'demo': ['data/sale_layout_category_data.xml'],
    'installable': True,
}
