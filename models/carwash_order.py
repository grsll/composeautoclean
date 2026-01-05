from odoo import models, fields, api


class CarwashOrder(models.Model):
    _name = "compose_auto_clean.carwash_order"
    _description = "Pesanan Cuci Mobil"

    customer_id = fields.Many2one(
        "compose_auto_clean.customer", string="Pelanggan", required=True
    )
    vehicle_id = fields.Many2one(
        "compose_auto_clean.vehicle",
        string="Kendaraan",
        required=True,
        domain="[('customer_id', '=', customer_id)]",
    )
    service_name = fields.Selection(
        [
            ("basic_wash", "Cuci Dasar"),
            ("premium_wash", "Cuci Premium"),
            ("deluxe_wash", "Cuci Mewah"),
        ],
        string="Nama Layanan",
        required=True,
    )
    price = fields.Float(string="Harga", compute="_compute_price", readonly=True)
    duration = fields.Float(
        string="Durasi (jam)", compute="_compute_duration", readonly=True
    )
    variant = fields.Selection(
        [
            ("basic", "Dasar"),
            ("premium", "Premium"),
            ("deluxe", "Mewah"),
        ],
        string="Varian",
        compute="_compute_variant",
        readonly=True,
    )
    payment_status = fields.Selection(
        [
            ("draft", "Draf"),
            ("belum bayar", "Belum Bayar"),
            ("lunas", "Lunas"),
        ],
        string="Status Pembayaran",
        default="draft",
    )
    order_date = fields.Datetime(string="Tanggal Pesanan", default=fields.Datetime.now)

    @api.depends("service_name")
    def _compute_price(self):
        for record in self:
            if record.service_name == "basic_wash":
                record.price = 50000
            elif record.service_name == "premium_wash":
                record.price = 75000
            elif record.service_name == "deluxe_wash":
                record.price = 100000
            else:
                record.price = 0

    @api.depends("service_name")
    def _compute_duration(self):
        for record in self:
            if record.service_name == "basic_wash":
                record.duration = 1
            elif record.service_name == "premium_wash":
                record.duration = 1.5
            elif record.service_name == "deluxe_wash":
                record.duration = 2
            else:
                record.duration = 0

    @api.depends("service_name")
    def _compute_variant(self):
        for record in self:
            if record.service_name == "basic_wash":
                record.variant = "basic"
            elif record.service_name == "premium_wash":
                record.variant = "premium"
            elif record.service_name == "deluxe_wash":
                record.variant = "deluxe"
            else:
                record.variant = False
