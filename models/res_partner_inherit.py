# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    carwash_order_ids = fields.One2many(
        "carwash.order",
        "partner_id",
        string="Riwayat Pesanan",
    )
    kendaraan_ids = fields.One2many(
        "cdn.kendaraan",
        "customer_id",
        string="Daftar Kendaraan",
    )
