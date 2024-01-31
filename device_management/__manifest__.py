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
        'wizard/display_wizard.xml',
        'views/menu.xml',
    ],

    'assets': {
        'web.assets_backend': [
            # 'device_management/static/src/scss/device_rating.scss',
            'device_management/static/src/js/device_rating.js',
            'device_management/static/src/js/device_extends.js',
            'device_management/static/src/xml/device_button.xml',
            'device_management/static/src/xml/device_rating.xml',
            'device_management/static/src/js/first.js',
            'device_management/static/src/js/activate_button.js',
            'device_management/static/src/xml/activate_button.xml',
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
}
