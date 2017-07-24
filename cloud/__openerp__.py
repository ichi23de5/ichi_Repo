# -*- coding: utf-8 -*-
{
    'name': "CLOUD",

    'summary': "View[FIX]",
    'author': "ichi2",
    'website': "http://www.toyo-kiki.co.jp",
    'installable': True,
    'category': "Uncategorized",
    'version': "9.0.0.1.1",
    'depends': ['base','sale','product','property','toki_sale'],
    'data': [
#        'security/user_groups.xml',
#	'security/ir.model.access.csv',
	'views/cloud_view.xml',
        'views/sim_view.xml'
    ],
}
