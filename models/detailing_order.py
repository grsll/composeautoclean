from odoo import models, fields, api


class DetailingOrder(models.Model):
    _name = "detailing.order"
    _inherit = ["mail.thread"]
    _description = "Detailing Order"
    _order = "id desc"

    customer_id = fields.Many2one(
        "cdn.customer",
        string="Customer",
        required=True,
        tracking=True,
    )
    vehicle_id = fields.Many2one(
        "cdn.kendaraan",
        string="Kendaraan",
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

    @api.onchange("vehicle_id")
    def _onchange_vehicle_id(self):
        if self.vehicle_id:
            self.jenis_kendaraan = self.vehicle_id.jenis_kendaraan
            self.product_id = False

    @api.onchange("jenis_kendaraan")
    def _onchange_jenis_kendaraan(self):
        if self.jenis_kendaraan:
            self.product_id = False

    product_id = fields.Many2one(
        "product.product",
        string="Varian Jasa",
        required=True,
        tracking=True,
        domain="[('service_type', '=', 'detailing'), '|', ('jenis_kendaraan', '=', False), ('jenis_kendaraan', '=', jenis_kendaraan)]",
    )

    price = fields.Float(
        string="Harga",
        compute="_compute_price",
        store=True,
        readonly=True,
    )

    invoice_id = fields.Many2one(
        "account.move",
        string="Invoice",
        readonly=False,
        tracking=True,
    )

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("invoiced", "Invoiced"),
        ],
        string="Status",
        default="draft",
    )

    @api.depends("product_id")
    def _compute_price(self):
        for rec in self:
            rec.price = rec.product_id.lst_price if rec.product_id else 0.0

    @api.onchange("customer_id")
    def _onchange_customer_id(self):
        """
        Reset fields when customer changes
        """
        self.vehicle_id = False
        self.product_id = False

    def action_draft(self):
        self.state = "draft"

    def action_confirm(self):
        self.state = "confirmed"

    def action_invoice(self):
        account = self.product_id._get_product_accounts()["income"]
        if not account:
            raise ValueError("Product does not have an income account set.")
        invoice_vals = {
            "move_type": "out_invoice",
            "partner_id": self.customer_id.partner_id.id,
            "invoice_date": fields.Date.today(),
            "invoice_line_ids": [
                (
                    0,
                    0,
                    {
                        "product_id": self.product_id.id,
                        "quantity": 1,
                        "price_unit": self.price,
                        "account_id": account.id,
                    },
                )
            ],
        }
        invoice = self.env["account.move"].create(invoice_vals)
        self.invoice_id = invoice.id
        self.state = "invoiced"
        return {
            "type": "ir.actions.act_window",
            "res_model": "account.move",
            "res_id": invoice.id,
            "view_mode": "form",
            "view_type": "form",
            "target": "current",
        }
