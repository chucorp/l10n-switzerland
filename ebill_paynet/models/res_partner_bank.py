from odoo import models


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    def build_qr_code_base64(
        self,
        amount,
        free_communication,
        structured_communication,
        currency,
        debtor_partner,
        qr_method=None,
        silent_errors=True,
    ):
        # FIXME Workaround to bypass error None type of native update
        # ref: https://github.com/odoo/odoo/blob/bc8e2d67b5980bb963f0e663f3c3d761ca4af169/addons/account/models/res_bank.py#L57     # noqa: B950
        qr_code_vals = self.build_qr_code_vals(
            amount,
            free_communication,
            structured_communication,
            currency,
            debtor_partner,
            qr_method,
            silent_errors,
        )
        if qr_code_vals:
            return self._get_qr_code_base64(*qr_code_vals)
        return None
