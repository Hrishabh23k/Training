{
    'name': 'Additional Sale',

    'summary': """ Additional feature of Sale Order""",

    'author': "Hrishabh Nagar",

    'category': 'Sales',

    'version': '16.0.1.0.0',
    'depends': ['sale','purchase'],

    'data':[
        'security/ir.model.access.csv',
        # 'views/inherited_sale.xml',
        # 'views/custom_invoice.xml',
        'views/purchase.xml',
        'report/purchase.xml',
        'report/purchase_template.xml',
        'views/purchase_mail.xml',
        # 'wizard/sale_order_wizard.xml',
    ],

    'installable':True,
    'application':True,
    'auto_install':False
}