# -*- coding: utf-8 -*-
{
    'name': "issue_planned_time",

    'summary': 'Adds planned time for issues' """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Company",
    'website': "https://github.com/m3dbedb",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project_issue'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    "installable": True,
}