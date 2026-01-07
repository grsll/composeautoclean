# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    nomor_kendaraan = fields.Char(string="Nomor Kendaraan")
    jenis_kendaraan = fields.Selection(
        selection=[("mobil", "Mobil"), ("motor", "Motor"), ("bus", "Bus")],
        string="Jenis Kendaraan",
    )
    carwash_order_ids = fields.One2many(
        "carwash.order",
        "partner_id",
        string="Riwayat Pesanan",
    )
