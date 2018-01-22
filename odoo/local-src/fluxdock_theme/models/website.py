# Copyright 2016 Simone Orsi (Camptocamp)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, api, SUPERUSER_ID, fields


def smart_truncate(text, length=100, suffix='...'):
    """Smart truncate text."""
    # http://stackoverflow.com/questions/250357/
    # truncate-a-string-without-ending-in-the-middle-of-a-word
    text = text or ''
    if len(text) <= length:
        return text
    else:
        return ' '.join(text[:length + 1].split(' ')[0:-1]) + suffix


class Website(models.Model):
    _inherit = 'website'

    @api.model
    def truncate_text(self, text, length=100, suffix='...'):
        """Truncate text."""
        return smart_truncate(text, length=length, suffix=suffix)

    @api.model
    def image_url(self, record, field, size=None):
        if record._name == 'res.partner':
            if field == 'image' and not record.image:
                return '/fluxdock_theme/static/img/member-placeholder.png'
        return super(Website, self).image_url(record, field, size=size)


class WebsiteMixin(models.AbstractModel):
    _inherit = 'website.published.mixin'

    @api.model
    def is_owner(self, uid):
        if not uid:
            return False
        if uid == SUPERUSER_ID:
            return True
        return self.create_uid.id == uid

    # placeholder fields to make image_url compute method happy
    image = fields.Binary('image')
    image_url = fields.Char(
        string='Main image URL',
        compute='_compute_image_url',
        default='',
        readonly=1,
    )

    @api.multi
    @api.depends('image')
    def _compute_image_url(self):
        ws_model = self.env['website']
        for item in self:
            image_url = ''
            if item.image:
                image_url = ws_model.image_url(item, 'image')
            item.image_url = image_url
