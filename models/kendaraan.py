from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Kendaraan(models.Model):
    _name = "cdn.kendaraan"
    _description = "Tabel Kendaraan Pelanggan"
    _rec_name = "nomor_kendaraan"
    _order = "id desc"

    customer_id = fields.Many2one(
        comodel_name="res.partner",
        string="Customer",
        required=True,
        ondelete="cascade",
    )

    nomor_kendaraan = fields.Char(
        string="Nomor Kendaraan",
        required=True,
    )

    jenis_kendaraan = fields.Selection(
        [
            ("mobil", "Mobil"),
            ("motor", "Motor"),
            ("bus", "Bus"),
        ],
        string="Jenis Kendaraan",
        required=True,
    )

    merk = fields.Char(string="Merk Dan TipeKendaraan")
    warna = fields.Char(string="Warna")

    customer_alamat = fields.Char(
        related="customer_id.street",
        string="Alamat Customer",
        readonly=True,
    )

    customer_telepon = fields.Char(
        related="customer_id.phone",
        string="No. Telepon",
        readonly=True,
    )

    kendaraan_ids = fields.One2many(
        comodel_name="cdn.kendaraan",
        inverse_name="customer_id",
        string="Daftar Kendaraan Customer",
        readonly=True,
        related="customer_id.kendaraan_ids",
    )

    catatan = fields.Text(string="Catatan Kondisi")
    active = fields.Boolean(string="Aktif", default=True)

    def name_get(self):
        result = []
        for rec in self:
            name = f"[{rec.nomor_kendaraan or '-'}] {rec.merk or ''} {rec.tipe or ''}"
            result.append((rec.id, name.strip()))
        return result


class JenisKendaraan(models.Model):
    _name = "cdn.jenis.kendaraan"
    _description = "Master Jenis Kendaraan"

    name = fields.Char(string="Jenis Kendaraan", required=True)
    color = fields.Integer(string="Color Index")
    description = fields.Text(string="Keterangan")
