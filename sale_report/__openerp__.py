# -*- coding: utf-8 -*-


{
        "name": " Sale report",
        "summary": "sale report",
        "version": "9.0.0.1.1",
        "category": "Sales",
        "website": "http://www.toyo-kiki.co.jp",
        "author": "ichi2",
        "license": "AGPL-3",
        "application": False,
        "installable": True,
        "depends": [
                "sale","property",
                "base","account","crm","product",
        ],
        "data": [
                "views/sale_view.xml",
                "security/user_groups.xml",
                "security/ir.model.access.csv",
        ],
}



