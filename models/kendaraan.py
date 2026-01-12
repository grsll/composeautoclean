# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Kendaraan(models.Model):
    _name = "cdn.kendaraan"
    _description = "Kendaraan Customer"
    _rec_name = "nomor_kendaraan"
    _order = "id desc"

    customer_id = fields.Many2one(
        "cdn.customer",
        string="Customer",
        required=True,
        ondelete="cascade",
    )

    nomor_kendaraan = fields.Char(string="Nomor Kendaraan", required=True)

    jenis_kendaraan = fields.Selection(
        [
            ("mobil", "Mobil"),
            ("motor", "Motor"),
            ("bus", "Bus"),
        ],
        required=True,
    )

    merk = fields.Char(string="Merk dan Tipe")
    warna = fields.Char(string="Warna")
    catatan = fields.Text(string="Catatan Kondisi")
    active = fields.Boolean(default=True)
