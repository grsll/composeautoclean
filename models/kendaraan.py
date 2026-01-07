from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Kendaraan(models.Model):
    _name = "cdn.kendaraan"
    _description = "Tabel Kendaraan Pelanggan"
    # Mengatur agar nomor polisi muncul sebagai identitas utama di dropdown
    _rec_name = "nomor_polisi" 
    _order = "id desc"

    nomor_polisi = fields.Char(string="Nomor Polisi", required=True, index=True)
    merk = fields.Char(string="Merk Kendaraan", placeholder="Contoh: Toyota, Honda")
    tipe = fields.Char(string="Tipe/Model", placeholder="Contoh: Avanza, Vario")
    warna = fields.Char(string="Warna")
    customer_id = fields.Many2one(comodel_name="res.partner", string="Customer", required=True, ondelete="cascade")
    jenis_kendaraan_ids = fields.Many2many(
        comodel_name="cdn.jenis.kendaraan", 
        string="Kategori Kendaraan",
        help="Pilih jenis layanan/kendaraan yang diinginkan (bisa lebih dari 1)"
    )
    
    customer_alamat = fields.Char(related="customer_id.street", string="Alamat Customer", readonly=True)
    customer_telepon = fields.Char(related="customer_id.phone", string="No. Telepon", readonly=True)

    catatan = fields.Text(string="Catatan Kondisi")
    active = fields.Boolean(string="Aktif", default=True)

    # ---------------------------------------------------------
    # 1. Validasi (Python Constraints)
    # ---------------------------------------------------------
    
    @api.constrains('nomor_polisi')
    def _check_unique_nopol(self):
        """Mencegah input nomor polisi yang sama (duplikat)"""
        for rec in self:
            # Mencari nopol yang sama secara case-insensitive
            domain = [
                ('nomor_polisi', '=ilike', rec.nomor_polisi),
                ('id', '!=', rec.id)
            ]
            if self.search_count(domain) > 0:
                raise ValidationError(_("Nomor Polisi %s sudah terdaftar di sistem!") % rec.nomor_polisi.upper())

    # ---------------------------------------------------------
    # 2. Otomatisasi (Onchange & Compute)
    # ---------------------------------------------------------

    @api.onchange('nomor_polisi')
    def _onchange_nomor_polisi(self):
        """Otomatis mengubah nomor polisi menjadi huruf kapital saat diketik"""
        if self.nomor_polisi:
            self.nomor_polisi = self.nomor_polisi.upper()

    # ---------------------------------------------------------
    # 3. Custom Display Name (Formatting)
    # ---------------------------------------------------------

    def name_get(self):
        """Mengubah cara record ditampilkan di field Many2one modul lain"""
        result = []
        for rec in self:
            # Contoh hasil: [B 1234 ABC] Toyota Avanza
            display_name = f"[{rec.nomor_polisi}] {rec.merk or ''} {rec.tipe or ''}"
            result.append((rec.id, display_name.strip()))
        return result

class JenisKendaraan(models.Model):
    _name = "cdn.jenis.kendaraan"
    _description = "Master Jenis Kendaraan"

    name = fields.Char(string="Jenis Kendaraan", required=True)
    color = fields.Integer(string="Color Index")
    description = fields.Text(string="Keterangan")