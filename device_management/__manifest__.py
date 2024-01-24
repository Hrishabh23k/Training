{
    'name': 'Device_Management',
    'description': 'Device Management System',

    'author': "Hrishabh Nagar",

    'category': 'Services',

    'version': '16.0.1.0.0',
    'depends': ['base', 'hr'],

    'data': [
        'security/ir.model.access.csv',
        'security/device_record_rules.xml',
        'views/device.xml',
        'views/device_assignment.xml',
        'views/device_type.xml',
        'views/device_brand.xml',
        'views/device_model.xml',
        'views/device_attribute.xml',
        'views/device_attribute_value.xml',
        'views/employee.xml',
        'views/device_management_settings.xml',
        'views/menu.xml',
    ],

    'assets': {
        'web.assets_backend': [
            # 'device_management/static/src/scss/device_rating.scss',
            'device_management/static/src/js/device_rating.js',
            'device_management/static/src/xml/device_rating.xml',
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
}
