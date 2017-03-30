# -*- coding: utf-8 -*-
{
    'name': "warranty_management",
    'summary': "this module is for warranty management",
    'author': "ichi2",
    'website': "http://www.toyo-kiki.co.jp",

    # Categories can be used to filter modules in modules listing
    'installable': True,
    'category': "Uncategorized",
    'version': "9.0.0.1.1",
    'depends': ['base','sale','product'],
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        "views/warranty_view.xml",
    ],
    
#    'demo': [
        #'demo.xml',
#    ],
}
