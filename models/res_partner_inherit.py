from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_carwash_customer = fields.Boolean(string="Customer Cuci Mobil", default=False)
