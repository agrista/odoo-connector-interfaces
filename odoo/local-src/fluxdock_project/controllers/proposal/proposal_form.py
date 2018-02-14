
from odoo import http
from odoo.addons.cms_form.controllers.main import FormControllerMixin


class ProposalFormController(http.Controller, FormControllerMixin):
    """Proposal form controller."""

    @http.route([
        '/dock/proposals/add',
        '/dock/proposals/<model("project.proposal"):main_object>/edit',
    ], type='http', auth='user', website=True)
    def cms_form(self, main_object=None, **kw):
        """Handle a `form` route.
        """
        model = 'project.proposal'
        return self.make_response(
            model, model_id=main_object and main_object.id, **kw)
