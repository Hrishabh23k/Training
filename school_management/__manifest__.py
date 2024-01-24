{
    'name': 'School Management',

    'summary': """ School Management Software""",

    'author': "Hrishabh Nagar",

    'category': 'Human Resources',

    'version': '16.0.1.0.0',
    'depends': ['base'],

    'data':[
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/school.xml',
        'views/subject.xml',
        'views/department.xml',
    ],

    'installable':True,
    'application':True,
    'auto_install':False
}