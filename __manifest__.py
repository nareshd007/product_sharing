
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Product Sharing',
    'version': '10.0',
    'author': 'Naresh',
    'category': 'Product Sharing',
    'sequence': 100,
    'summary': 'Product Sharing',
    'description': """
Product Sharing
====================
Product Sharing

    """,
    'website': 'www.odoo.com',
    'images': [
       
    ],
    'depends': ['base','website_sale'],
    'data': [
        'view/product_sharing.xml',
        
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
