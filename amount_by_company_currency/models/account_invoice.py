from odoo import api, fields, models, _


class AccountInvoiceTotalNewCurrency(models.Model):
    _inherit = "account.invoice"

    @api.one
    @api.depends('amount_total', 'currency_id')
    def _compute_amount_currency(self):
        if self.company_currency_id and self.company_currency_id != self.currency_id:
            self.amount_total_currency = self.amount_total * self.company_currency_id.rate
        else:
            self.amount_total_currency = self.amount_total

    amount_total_currency = fields.Monetary(string='Total currency', compute='_compute_amount_currency')
