# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Dentist Management',
    'version': '1.3',
    'category': 'Hidden',
    'description': """
Dentist Management System
===================================================
""",
    'depends': [
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient_view.xml',
        'views/patient_adults_view.xml',
        'views/patient_juveniles_view.xml',
        'views/appointment_view.xml',
    ],
    'sequence':'-100',
    'demo': [
    ],
    'test': [],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3',
}