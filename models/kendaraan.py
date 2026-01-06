from odoo import models, fields, api


class Kendaraan(models.Model):
    _name = "cdn.kendaraan"
    _description = "tabel kendaraan"

    customer_id = fields.Many2one(
        comodel_name="res.partner", string="Customer", required=True
    )
    jenis_kendaraan = fields.Selection(
        related="customer_id.jenis_kendaraan", string="Jenis Kendaraan", readonly=True
    )
    customer_name = fields.Char(
        related="customer_id.name", string="Nama Customer", readonly=True
    )
    customer_alamat = fields.Char(
        related="customer_id.street", string="Alamat Customer", readonly=True
    )
