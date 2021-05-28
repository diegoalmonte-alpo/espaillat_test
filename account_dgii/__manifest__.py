# -*- coding: utf-8 -*-

{
    'name' : 'Account DGII',
    'version' : '2.0',
    'summary': '',
    'sequence': 30,
    'description': """
    
    Modulo para el manejo de los NCF y los reportes de la DGII.

    """,
    'author': 'sisne, srl',
    'category': 'Account',
    'website': 'http://sisne.do/',
    'depends' : ['purchase','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_invoice_view.xml',
        'views/partner_view.xml',
        'views/account_tax.xml',
        'views/service_tax_view.xml',
        'wizard/report_wizard.xml',
        'views/account_dgii_menuitem.xml',
    ],
    'installable': True,
    'auto_install': False,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: