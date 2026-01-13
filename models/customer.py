from odoo import models, fields, api


class Customer(models.Model):
    _name = "cdn.customer"
    _description = "Tabel Customer"
    _rec_name = "nama"
    _order = "id desc"
    partner_id = fields.Many2one(
        "res.partner",
        string="Partner",
        required=True,
        ondelete="cascade",
        domain="[('is_carwash_customer', '=', True)]",
    )
    nama = fields.Char(string="Nama Customer", required=True)

    no_hp = fields.Char(string="Nomor HP", required=True)
    alamat = fields.Text(string="Alamat")

    kendaraan_ids = fields.One2many(
        "cdn.kendaraan",
        "customer_id",
        string="Daftar Kendaraan",
    )

    carwash_order_ids = fields.One2many(
        "carwash.order",
        "customer_id",
        string="Riwayat Pesanan",
    )

    active = fields.Boolean(default=True)

    @api.constrains("no_hp")
    def _check_no_hp(self):
        for record in self:
            if record.no_hp and not record.no_hp.strip():
                raise models.ValidationError("Nomor HP tidak boleh kosong!")
