# -*- coding: utf-8 -*-
{
        "name": " TEC report",
        "summary": "TEC report 2017-9",
        "version": "9.0.0.1.1",
        "category": "Sales",
        "website": "http://www.toyo-kiki.co.jp",
        "author": "ichi2",
        "license": "AGPL-3",
        "application": False,
        "installable": True,
        "depends": [
                   "sale","property","base","report","toki_sale","sale_layout",
                   ],
        "data": [
                "report/sale_order_template.xml",
                "report/sale_order_header.xml",
                "views/custom_report.xml",
                ],
}
