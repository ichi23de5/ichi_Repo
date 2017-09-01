# -*- coding: utf-8 -*-

{
        "name": " TOKI Account",
        "summary": "add fields[FIX-1]",
        "version": "9.0.0.1.1",
        "category": "Account",
        "website": "http://www.toyo-kiki.co.jp",
        "author": "ichi2",
        "license": "AGPL-3",
        "application": False,
        "installable": True,
        "depends": [
                   "account","property","sale","toki_sale",
                   ],
        "data": [
                "views/account_invoice_view.xml",
#                "report/report.xml"
                ],
}


