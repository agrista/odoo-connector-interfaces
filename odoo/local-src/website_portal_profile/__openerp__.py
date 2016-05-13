{
    'name': 'Website Portal Profile',
    'author': 'Goran Sunjka',
    'category': 'Website',
    'summary': '',
    'version': '1.1',
    'description': """
    Enhanced Portal Profile
        """,
    'website': 'https://www.sunjka.de/',
    'depends': [
        'partner_area',
        'website',
        'website_portal',
        'website_partner',
        'website_membership',
        'website_crm_partner_assign'
    ],
    'data': [
        'views/templates.xml',
        'views/members.xml',
        'views/members2.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
