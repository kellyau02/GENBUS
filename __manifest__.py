# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Inventario AO 6',
    'summary': 'Agrega campos número de parte y marca en producto',
    'category': 'Inventario',
    "sequence": 1,
    "author": "Boostech CR",
    'description': """
    Agrega los campos marca y número de parte a los módulos inventario y contabilidad
    """,
    'depends': ['account_accountant', 'stock'],
    'data': [
        'views/view_product.xml',
        'views/view_product_brand.xml',
        'security/ir.model.access.csv',
    ],
    'auto_install': False,
    'installable': True,
}
