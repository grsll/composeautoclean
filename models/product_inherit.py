# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    jenis_kendaraan = fields.Selection(
        [
            ("mobil", "Mobil"),
            ("motor", "Motor"),
            ("bus", "Bus"),
        ],
        string="Jenis Kendaraan",
    )

    service_type = fields.Selection(
        [
            ("carwash", "Cuci"),
            ("detailing", "Detailing"),
            ("poles", "Poles"),
            ("other", "Lainnya"),
        ],
        string="Tipe Layanan",
        compute="_compute_service_type",
        store=True,
    )

    @api.depends("categ_id")
    def _compute_service_type(self):
        for record in self:
            if not record.categ_id:
                record.service_type = "other"
                continue

            category_name = record.categ_id.name.lower()
            if "cuci" in category_name or "wash" in category_name:
                record.service_type = "carwash"
            elif "detailing" in category_name:
                record.service_type = "detailing"
            elif "poles" in category_name:
                record.service_type = "poles"
            else:
                record.service_type = "other"
