# -*- coding: utf-8 -*-

{
    "name": "Product Pack",
    "summary": "Add some products to orderline.",
    "version": "1.0.0",
    "category": "Product",
    "website": "https://www.toyo-kiki.co.jp/",
    "author": "TOYOKIKI INC.",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "product","sale",
    ],
    "data": [
        "views/product_view.xml",
    ],
}
