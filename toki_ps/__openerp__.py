# -*- coding: utf-8 -*-

{
    'name': 'Outsourcing Button',
    'summary': "Add outsourcing button to SaleOrder Form. And Create PO automatically",
    'version': '9.0.1.0.0',
    'category': 'Sales',
    "website": "http://www.toyo-kiki.co.jp",
    'author': 'ichi2',
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    'depends': [
        'sale', 'purchase', 'report'
    ],
    'data': [
        'views/sale_view.xml',
#        'wizard/product_set_add.xml',
#        'views/sale_order.xml',
#        'security/ir.model.access.csv',
    ],
}

