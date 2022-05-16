# -*- coding: utf-8 -*-
{
    'name': "jt_webeditor_extras",

    'description': "Trying to add extra font sizes to the wysiwyg web editor",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [
    ],
    'assets' : {
        'web.assets_qweb': [
            'jt_webeditor_extras/static/src/xml/editor.xml',
        ],        
        'website.assets_wysiwyg': [
            'jt_webeditor_extras/static/src/js/editor.js',
        ],
    }
}
