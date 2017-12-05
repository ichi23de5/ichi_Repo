# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'TOKI report pricelist hls',
    'summary': "module:'Sale product set' + toki original report system for HLS ",
    'version': '9.0.1.0.0',
    'category': 'Sales',
    "website": "https://odoo-community.org/",
    'author': 'Anybox, Odoo Community Association (OCA)',
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    'depends': [
        'sale','toki_report','sale_layout','toki_category',
    ],
    'data': [
        'views/product_set.xml',
        'wizard/product_set_add.xml',
        'views/sale_order.xml',
        'views/custom_report.xml',
        'report/sale_order_template.xml',
#        'security/ir.model.access.csv',
    ],
}
