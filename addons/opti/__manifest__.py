# -*- coding: utf-8 -*-
# type: ignore
{
    'name': "opti",

    'summary': "Optimization Module",

    'description': """
    Mivilsoft optimization module
    """,

    'author': "Mivilsoft",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','fleet'],
    'application': True,
    'installable': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/route_report.xml',
        'reports/route_report_template.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/routes.xml',
        'demo/stops.xml',
    ],
}
