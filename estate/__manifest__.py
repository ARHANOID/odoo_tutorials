# -*- coding: utf-8 -*-
{
    'name': "estate",
    'summary': """
        Starting module for "Master the Odoo web framework, chapter 0: Create a estate View"
    """,

    'description': """
        Starting module for "Master the Odoo web framework, chapter 0: Create a estate View"
    """,

    'version': '0.1',
    'application': True,
    'category': 'Tutorials/estate',
    'installable': True,
    'depends': ['web', 'base'],
    'data': ["security/ir.model.access.csv",
		"views/estate_views.xml",
	"views/menus.xml",

    ],
    'assets': {
        
    },
    'license': 'AGPL-3'
}
