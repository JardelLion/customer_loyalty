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
        'base','sale_loyalty','website_sale_loyalty','website_sale', 'portal','sale_management'
    ],
    "data": [
        'security/security.xml',
        "security/ir.model.access.csv",
        'data/mail_template_data.xml',
        'data/cron_data.xml',
        'data/loyalty_data.xml',
        "views/res_partner_views.xml",
        'report/loyalty_report_template.xml',
        'wizard/loyalty_card_update_balance_views.xml'
    ],
    'demo': [
        'demo/demo_data.xml'
    ],
    'auto_install': False,
    'application': False,
    'assets': {
        'web.assets_backend': [
            'customer_loyalty/static/src/js/loyalty_widget.js',
            'customer_loyalty/static/src/xml/loyalty_widget.xml',
        ],
    }
}