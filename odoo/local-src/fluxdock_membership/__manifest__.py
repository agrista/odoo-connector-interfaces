# © 2016 Denis Leemann (Camptocamp)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Fluxdock Membership specific development',
    'version': '11.0.1.0.0',
    'author': 'Camptocamp',
    'license': 'AGPL-3',
    'category': 'Reports',
    'website': 'http://www.camptocamp.com',
    'images': [],
    "external_dependencies": {
        "python": [
            "validate_email",
        ],
    },
    'depends': [
        'base',
        'l10n_ch',
        'membership',
        'membership_variable_period',
        'auth_signup',
        'auth_signup_verify_email',
        'website',
        'website_portal',
        'website_mass_mailing',
        'website_terms_of_use',
        'website_portal_sale',
        'website_partner',
        'website_membership',
        'partner_project_expertise',
        'cms_status_message',
        'cms_form',
        # flux
        'fluxdock_theme',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/partner_rules.xml',
        # views
        'views/partner_view.xml',
        # reports
        # TODO: move to a new module `fluxdock_reports`
        'reports/assets.xml',
        'reports/layout.xml',
        'reports/invoice.xml',
        # templates
        'templates/assets.xml',
        'templates/membership.xml',
        'templates/signup.xml',
        'templates/help_msgs.xml',
        'templates/profile/reset.xml',
        'templates/profile/profile-progress.xml',
        'templates/profile/widgets.xml',
        'templates/profile/my_home.xml',
        'templates/profile/upload.xml',
        'templates/membership/search_form.xml',
        'templates/membership/member_detail.xml',
        'templates/membership/payment.xml',
        # data
        'data/membership_data.xml',
        'data/group_data.xml',
        'data/email_data.xml',
        'data/website_menu.xml',
    ],
    'installable': False,
    'auto_install': False,
}
