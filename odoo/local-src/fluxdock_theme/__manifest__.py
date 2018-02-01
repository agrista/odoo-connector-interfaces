{
    'name': 'Fluxdock Theme specific development',
    'description': 'Custom Theme for the fluxdock website.',
    'version': '11.0.1.0.0',
    'author': 'Camptocamp',
    'data': [
        'templates/layout.xml',
        'templates/login.xml',
        'templates/footer.xml',
        'templates/snippets.xml',
        'templates/options.xml',
        'templates/assets.xml',
        'templates/listing.xml',
        'templates/widgets.xml',
        'templates/mosaic.xml',
        'templates/status_msg.xml',
        'templates/search_form.xml',
        'templates/email.xml',
        'pages/homepage.xml',
    ],
    'category': 'Theme/Creative',
    'depends': [
        'cms_status_message',
        'cms_delete_content',
        'cms_form',
        'cms_notification',
        'http_routing',
        'mail_digest',
        'website',
        # need for personal menu content (see layout.xml)
        'website_partner',
    ],
}
