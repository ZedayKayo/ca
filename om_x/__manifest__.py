# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'X',
    'version': '1.3',
    'category': 'Hidden',
    'description': """
Extend Contact/Employee.
===================================================
""",
    'depends': [
        'base',
        'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/contact.xml',
        'views/employee.xml',
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