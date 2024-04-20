# -*- coding: utf-8 -*-
{
    'name': "Project Update Report",
    'summary': """Enable option to print and send a email with a PDF of projects updates""",
    'description': """Enable option to print and send a email with a PDF of projects updates""",
    'author': "Alfonso Gonzalez",
    'website': "https://ntropy.tech/odoo",
    'category': 'Customizations',
    'version': '1.7',
    'license': "LGPL-3",
    'sequence': "-75",
    'depends': ['base',
                'project'],
    'data': [
        # Security
        # 'security/ir.model.access.csv',
        # Wizard
        # Reports
        'report/project_update_report.xml',
        'report/report.xml',
        # Views
        'views/project_update_view_form.xml',
        # Data
        'data/project_update_email_template.xml',
        # Sequence
        # Sample
    ],
    'currency': "USD",
    'qweb': [''],
    'images': [''],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
