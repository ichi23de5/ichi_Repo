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
                   "sale","property","base","account","sale_margin","sale_stock"
                   ],
        "data": [
                "views/sale_view.xml",
                "views/product_view.xml",
                "views/res_partner_view.xml",
                "security/toki_sale_security.xml",
#                "security/ir.model.access.csv",
                ],
}