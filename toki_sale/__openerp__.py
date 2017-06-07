# -*- coding: utf-8 -*-

{
        "name": " TOKI sale",
        "summary": "res_partner[fix]",
        "version": "9.0.0.1.1",
        "category": "Sales",
        "website": "http://www.toyo-kiki.co.jp",
        "author": "ichi2",
        "license": "AGPL-3",
        "application": False,
        "installable": True,
        "depends": [
                   "sale","property","base","account","sale_margin","sale_stock","report_aeroo"
                   ],
        "data": [
                "views/sale_view.xml",
                "views/product_view.xml",
                "views/res_partner_view.xml",
                "report/construction_report.xml",
                ],
}
