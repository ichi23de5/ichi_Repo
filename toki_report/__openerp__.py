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
                   "sale","property","base","account","purchase","report","toki_sale","toki_account","sale_layout",
                   ],
        "data": [
                "security/ir.model.access.csv", 
                "views/sale_view.xml",
                "views/res_partner_view.xml",
                "report/sale_order_template.xml",
                "report/sale_construction_template.xml",
                "report/outside_order_template.xml",
                "report/account_invoice_header.xml",
                "report/account_invoice_template.xml",
                "report/account_invoice_template2.xml",
                "report/sale_layout_add.xml",
                "views/custom_report.xml",
                ],
}
