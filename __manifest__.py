{
    'name': 'Customer Loyalty',
    'version': '1.0.0',
    'description': 'customer Loyalty',
    'summary': 'Customer Loyalty',
    'author': 'Jardel Elias Bernardo',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base','sale_loyalty','website','sale_management'
    ],
    "data": [
        'security/security.xml',
        "security/ir.model.access.csv",
        'data/mail_template_data.xml',
        'data/cron_data.xml',
        "views/res_partner_views.xml",
        'report/loyalty_report_template.xml'
    ],
    'demo': [],
    'auto_install': False,
    'application': False,
    'assets': {
        'web.assets_backend': [
            'customer_loyalty/static/src/js/loyalty_widget.js',
            'customer_loyalty/static/src/xml/loyalty_widget.xml',
        ],
    }
}