# -*- coding: utf-8 -*-
# type: ignore [reportUnusedExpression]
{
    'name': "cowsay",

    'summary': "Simple cowsay",

    'description': """
 ________________________________________ 
/ This is a module that manage different \\
| cowsays and send it over mail at a     |
\\ given schedule                         /
 ---------------------------------------- 
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
    """,

    'author': "Davido264",
    'website': "https://github.com/Davido264",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    'application': True,
    'installable': True,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

