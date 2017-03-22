# -*- coding: utf-8 -*-

{
    "name": "Show sheets with full width",
    "version": "9.0.1.0.0",
    "author": "Therp BV,Sudokeys,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "summary": "Use the whole available screen width when displaying sheets",
    "description": """
Description
-----------
This addon displays sheets making use of the whole screen, thereby avoiding
to narrow columns in ie. sale orders or purchase orders.
Acknowledgements
----------------
Icon courtesy of http://www.picol.org/ (size_width.svg)
    """,
    "category": "Tools",
    "depends": [
        'web',
    ],
    "data": [
        "view/qweb.xml",
    ],
    "auto_install": False,
    'installable': True,
    "application": False,
}
