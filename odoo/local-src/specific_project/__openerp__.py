# -*- coding: utf-8 -*-
# © 2016 Denis Leemann (Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{'name': 'Fluxdock Project specific development',
 'version': '9.0.1.0.0',
 'category': '',
 'author': 'Camptocamp',
 'maintainer': 'Camptocamp',
 'website': 'http://www.camptocamp.com/',
 'depends': [
     'project',
     'partner_project_expertise',
     'specific_membership',
     'specific_project_proposal',
 ],
 'data': [
     'security/ir.model.access.csv',
     'security/record_rules.xml',
     'views/project_reference.xml',
     'templates/reference.xml',
     'templates/reference_form.xml',
     'templates/reference_listing.xml',
     'templates/my_home.xml',
 ],
 'test': [],
 'installable': True,
 'auto_install': False,
 'application': True,
 }
