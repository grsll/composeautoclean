from odoo import models, fields, api


class CarwashOrder(models.Model):
    _name = "carwash.order"
    _description = "Carwash Order"

    partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    # Use computed stored Char fields (safe access) instead of related fields
    name = fields.Char(
        string="Customer Name",
        compute="_compute_customer_info",
        store=True,
        readonly=True,
    )
    nomor_kendaraan = fields.Char(
        string="Nomor Kendaraan",
        compute="_compute_customer_info",
        store=True,
        readonly=True,
    )
    product_id = fields.Many2one("product.product", string="Varian Jasa", required=True)

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("invoiced", "Invoiced"),
        ],
        string="Status",
        default="draft",
        readonly=True,
    )

    @api.depends("partner_id", "partner_id.name", "partner_id.nomor_kendaraan")
    def _compute_customer_info(self):
        for rec in self:
            pid = rec.partner_id
            try:
                # accessing pid.id may raise AttributeError if pid is an _unknown placeholder
                pid_id = pid.id
            except AttributeError:
                rec.name = False
                rec.nomor_kendaraan = False
                continue
            if pid_id:
                rec.name = getattr(pid, "name", False)
                rec.nomor_kendaraan = getattr(pid, "nomor_kendaraan", False)
            else:
                rec.name = False
                rec.nomor_kendaraan = False

    def action_draft(self):
        self.state = "draft"

    def action_confirm(self):
        self.state = "confirmed"

    def action_invoice(self):
        # Logic to create invoice
        self.state = "invoiced"
