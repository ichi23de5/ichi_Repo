# -*- coding: utf-8 -*-


{
    'name': 'TOKI Category',
    'author': 'ichi2',
    'category': 'Product Management',
    'summary': 'Custom product category group.',
    'website': 'http://www.toki.com',
    'version': '9.0.1.0.0',
    'sequence': 1,
    'depends': ['sale_layout','sale','base','sale_product_set','property'],
    'data': [
#             'security/ir.model.access.csv',
             'views/category_view.xml',
             'views/sale_view.xml',
             'data/layout_data.xml',
            ],
    'installable': True,
}
