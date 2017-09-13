# -*- coding: utf-8 -*-

{
    "name": "TOKI report Pricelist",
    "summary": "Print price list from menu option, product templates, "
               "products variants or price lists",
    "version": "9.0.1.0.0",
    "category": "Product",
    "website": "http://www.tecnativa.com",
    "author": "ichi2",
    "license": "AGPL-3",
    "depends": [
        "product","toki_sale",
    ],
    "data": [
        "views/product_spec_views.xml",
        "views/paperformat.xml",
        "views/report_product_pricelist.xml",
        "wizards/product_pricelist_print_view.xml",
    ],
}
