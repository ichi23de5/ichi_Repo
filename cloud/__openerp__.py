# -*- coding: utf-8 -*-
{
    'name': "cloud",

    'summary': "test user",
    'author': "ichi2",
    'website': "http://www.toyo-kiki.co.jp",


    'author': "Yenthe Van Ginneken",
    'website': "http://www.odoo.yenthevg.com",
    'installable': True,
    'category': "Uncategorized",
    'version': "9.0.0.1.1",
    'depends': ['base','sale','product','project','account','sim',],


    # always loaded
    'data': [
        'security/user_groups.xml',
	'security/ir.model.access.csv',
#	'views/cloud_view.xml'
    ],
}
