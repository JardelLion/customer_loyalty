{
    'name': 'Customer Loyalty',
    'version': '1.0.0',
    'description': """
Módulo de fidelização de clientes que estende a funcionalidade
nativa do Odoo para permitir o cálculo personalizado de pontos
com base no valor total dos pedidos de venda.

    Atribui 1 ponto por cada 10 unidades monetárias do valor total
    do pedido, utilizando divisão inteira, e permite ativar esta
    regra através do campo use_order_total_for_points nos programas
    de fidelização.
""",
    'summary': 'Gestão de Fidelização de Clientes e Cálculo de Pontos',
    'author': 'Jardel Elias Bernardo',
    'website': 'https://github.com/JardelLion',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base','sale_loyalty','website_sale_loyalty','website_sale', 'portal','sale_management'
    ],
    "data": [
        "data/cron_data.xml",
        "data/mail_template_data.xml",
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/loyalty_program_views.xml",
        "views/res_partner_views.xml",
        "report/loyalty_report_template.xml",
        "wizard/loyalty_card_update_balance_views.xml"
    ],
    'demo': [
        'demo/demo_data.xml',
        "demo/loyalty_data.xml",
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