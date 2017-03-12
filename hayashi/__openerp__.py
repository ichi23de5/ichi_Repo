
# -*- coding: utf-8 -*-


{
        "name": "Tabelog with Report",
        "summary": "mainichi tabelog kakuyo",
        "version": "9.0.0.1.1",
        "category": "Uncategorized",
        "website": "http://www.toyo-kiki.co.jp",
        "author": "ichi2",
        "license": "AGPL-3",
#        "application": False,
        "installable": True,
        "depends": ["base","sale","purchase","product","report",
        ],
        "data": [
                "views/lunch_view.xml",
                "views/hayashi.tabe_report.xml",
                "views/tabe_report.xml",

        ],
}
