# -*- coding: utf-8 -*-

{
        "name": " TOKI report",
        "summary": "construction ",
        "version": "9.0.0.1.1",
        "category": "Sales",
        "website": "http://www.toyo-kiki.co.jp",
        "author": "ichi2",
        "license": "AGPL-3",
        "application": False,
        "installable": True,
        "depends": [
                   "sale","property","base","account","toki_sale",
                   ],
        "data": [
                "views/sale_report.xml", 
                "report/sale_construction_template.xml",
                ],
}
