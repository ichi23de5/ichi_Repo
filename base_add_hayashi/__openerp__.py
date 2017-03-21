# -*- coding: utf-8 -*-


{
	"name": " Base Add Hayashi",
	"summary": "add field in res partner module by hayashi",
	"version": "9.0.0.1.1",
	"category": "Sales",
	"website": "http://www.toyo-kiki.co.jp",
	"author": "ichi2",
	"license": "AGPL-3",
	"application": False,
	"installable": True,
	"depends": [
		"sale","inspection","cloud",
	],
	"data": [
		"views/res_partner_view.xml",
#                "views/sale_view_add.xml",
	],
}
