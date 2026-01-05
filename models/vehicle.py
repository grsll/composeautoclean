from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Vehicle(models.Model):
    _name = "compose_auto_clean.vehicle"
    _description = "Tabel Kendaraan"
    _order = "name asc"

    # --- Fields Dasar ---
    name = fields.Char(string="Plat Nomor", required=True, copy=False)
    vehicle_type = fields.Selection(
        [("mobil", "Mobil"), ("motor", "Motor")],
        string="Jenis Kendaraan",
        required=True,
        default="mobil",
    )
    brand = fields.Char(string="Merek/Tipe", help="Contoh: Honda Vario, Toyota Avanza")
    color = fields.Char(string="Warna")
    active = fields.Boolean(default=True, string="Aktif")

    # --- Relasi ---
    customer_id = fields.Many2one(
        "compose_auto_clean.customer",
        string="Pemilik",
        required=True,
        ondelete="cascade",
    )
    wash_order_ids = fields.One2many(
        "compose_auto_clean.carwash_order", 
        "vehicle_id", 
        string="Riwayat Cuci"
    )

    # --- Fields Compute (Statistik) ---
    wash_count = fields.Integer(
        string="Total Cuci", 
        compute="_compute_wash_stats", 
        store=True
    )
    last_wash_date = fields.Date(
        string="Cuci Terakhir", 
        compute="_compute_wash_stats", 
        store=True
    )

    # --- Constraints & Validasi ---
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Plat nomor ini sudah terdaftar di sistem!')
    ]

    @api.constrains('name')
    def _check_name_format(self):
        for rec in self:
            if rec.name and len(rec.name) < 3:
                raise ValidationError(_("Plat nomor terlalu pendek! Masukkan format yang benar."))

    # --- Logic Methods ---
    
    @api.depends('wash_order_ids.state', 'wash_order_ids.order_date')
    def _compute_wash_stats(self):
        for rec in self:
            # Menggunakan field 'state' untuk filter
            done_orders = rec.wash_order_ids.filtered(lambda x: x.state == 'done')
            rec.wash_count = len(done_orders)
            rec.last_wash_date = max(done_orders.mapped('order_date')) if done_orders else False

    @api.onchange('name')
    def _onchange_name_upper(self):
        """Otomatis membuat plat nomor menjadi huruf kapital"""
        if self.name:
            self.name = self.name.upper()

    def action_view_wash_orders(self):
        """Method untuk Stat Button: Membuka riwayat cuci kendaraan ini"""
        self.ensure_one()
        return {
            'name': _('Riwayat Cuci: %s') % self.name,
            'type': 'ir.actions.act_window',
            'res_model': 'compose_auto_clean.carwash_order',
            'view_mode': 'list,form',
            'domain': [('vehicle_id', '=', self.id)],
            'context': {'default_vehicle_id': self.id},
        }