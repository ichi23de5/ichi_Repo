# -*- coding: utf-8 -*-


{
	"name": " BALUS",
	"summary": "add bug in sale module by hayashi ..recite BALUS",
	"version": "9.0.0.1.1",
	"category": "Sales",
	"website": "http://www.toyo-kiki.co.jp",
	"author": "ichi2",
	"license": "AGPL-3",
	"application": False,
	"installable": True,
	"depends": [
		"sale","inspection","cloud","base","account","crm",
	],
	"data": [
		"views/sale_view.xml",
                "security/user_groups.xml",
                "security/ir.model.access.csv"
	],
}
