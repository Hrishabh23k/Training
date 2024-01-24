# -*- coding: utf-8 -*-
{
    'name': 'Custom Addons V16',
    'version': '1.0',
    'author': 'Hrishabh Nagar',
    'summary': 'Custom Addons V16',
    'sequence': -1,
    'description': """Custom Addons V16""",
    'category': 'OWL',
    'depends': ['base', 'web', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list.xml',
        'views/res_partner.xml',
    ],
    'demo': [
    ],
    'assets': {
        'web.assets_backend': [
            'custom-addons/static/src/components/*/*.js',
            'custom-addons/static/src/components/*/*.xml',
            'custom-addons/static/src/components/*/*.scss',
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
}
