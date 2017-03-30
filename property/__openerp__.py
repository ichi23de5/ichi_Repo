# -*- coding: utf-8 -*-
{
    'name': "Property Management",
    'summary': "Manage Properties of TOKI Constractions ",
    'author': "ichi2",
    'website': "http://www.toyo-kiki.co.jp",
    'description': "Manage Properties of TKCLOUD or Constructions",
    # Categories can be used to filter modules in modules listing
    'installable': True,
    'category': "Property",
    'version': "9.0.0.1.1",
    'depends': ['base','sale','warranty','inspection'],
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        "views/property_view.xml",
    ],
    
}
