{
    'name': 'Odoo school',

    'summary': """ Odoo School""",

    'author': "Hrishabh Nagar",

    'category': 'Human Resources',

    'version': '16.0.1.0.0',
    'depends': ['base', 'hr'],

    'data': [
        'security/ir.model.access.csv',
        'security/odoo_school_security.xml',
        'report/exam_report.xml',
        'views/teacher_class.xml',
        'views/exam.xml',
        'wizard/exam_wizard.xml',
        'views/teacher.xml',
        'views/odoo_school_settings.xml',
        'views/fees.xml',
        'views/teacher_menu.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False
}
