# -*- coding: utf-8 -*-
{
    'name': "Project Update Report",
    'summary': """Enable option to print a PDF of projects updates""",
    'description': """Enable option to print a PDF of projects updates""",
    'author': "Alfonso Gonzalez",
    'website': "https://ntropy.tech/odoo",
    'category': 'Customizations',
    'version': '1.2',
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
        # Data
        # Sequence
        # Sample
    ],
    'currency': "MXN",
    'qweb': [''],
    'images': [''],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
