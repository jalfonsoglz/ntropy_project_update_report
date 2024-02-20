# -*- coding: utf-8 -*-
{
    'name': "Project Update Report",
    'summary': """Project Update Report""",
    'description': """Project Update Report""",
    'author': "Alfonso Gonzalez",
    'website': "https://ntropy.tech/odoo",
    'category': 'Customizations',
    'version': '16.0.0.0.1',
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
    'application': True,
    'auto_install': False,
}
