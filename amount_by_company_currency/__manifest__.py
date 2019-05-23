# -*- coding: utf-8 -*-
# Copyright 2019 by Fogits International
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{'name': 'Total amount with company currency',
 'summary': 'Add total amount with company currency in invoice',

 'version': '12.0',
 'author': 'Fogits Solutions',
 'website': 'https://www.fogits.com/',
 'license': 'AGPL-3',
 'category': 'Invoicing Management',
 'images': ['static/description/image.jpg'],
 'depends': [
     'base',
     'account',
 ],
 'data': [
     'views/account_invoice_view.xml',
 ],

 }
