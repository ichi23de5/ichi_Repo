# -*- coding: utf-8 -*-
{
    'name': "cloud",
    'summary': "this module is for cloud management2",
    'author': "ichi2",
    'website': "http://www.toyo-kiki.co.jp",

    # Categories can be used to filter modules in modules listing
    'installable': True,
    'category': "Uncategorized",
    'version': "9.0.0.1.1",
    'depends': ['base','report_aeroo','sale','product','project','account','sim',],
    'data': [
        "views/cloud_view.xml",
        "report/report.xml",
    ],
    
#    'demo': [
        #'demo.xml',
#    ],
}
