# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models


class FluxdockSearchForm(models.AbstractModel):
    """Partner model search form."""

    _name = 'fluxdock.cms.form.search'
    _description = 'Fluxdock CMS search form'
    _inherit = 'cms.form.search'
    form_wrapper_template = 'theme_fluxdocs.search_form_wrapper'
    form_template = 'theme_fluxdocs.search_form'

    def listing_options(self):
        return {
            'show_preview': False,
            'show_create_date': False,
        }
