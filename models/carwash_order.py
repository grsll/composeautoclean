# -*- coding: utf-8 -*-
from odoo import models, fields, api

# tes
class CarwashOrder(models.Model):
    _name = "carwash.order"
    _description = "Carwash Order"
    _order = "id desc"

    partner_id = fields.Many2one(
        "res.partner",
        string="Customer",
        required=True,
    )

    nomor_kendaraan = fields.Char(
        string="Nomor Kendaraan",
        compute="_compute_customer_info",
        store=True,
        readonly=True,
    )

    jenis_kendaraan = fields.Selection(
        [
            ("mobil", "Mobil"),
            ("motor", "Motor"),
            ("bus", "Bus"),
        ],
        string="Jenis Kendaraan",
        compute="_compute_customer_info",
        store=True,
        readonly=True,
    )

    product_id = fields.Many2one(
        "product.product",
        string="Varian Jasa",
        required=True,
    )

    price = fields.Float(
        string="Harga",
        compute="_compute_price",
        store=True,
        readonly=True,
    )

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

    @api.depends(
        "partner_id",
        "partner_id.name",
        "partner_id.nomor_kendaraan",
        "partner_id.jenis_kendaraan",
    )
    def _compute_customer_info(self):
        for rec in self:
            partner = rec.partner_id
            if partner:
                rec.nomor_kendaraan = partner.nomor_kendaraan
                rec.jenis_kendaraan = partner.jenis_kendaraan
            else:
                rec.nomor_kendaraan = False
                rec.jenis_kendaraan = False

    @api.depends("product_id")
    def _compute_price(self):
        for rec in self:
            rec.price = rec.product_id.lst_price if rec.product_id else 0.0

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        """
        Reset product ketika customer berubah
        """
        self.product_id = False

    def action_draft(self):
        self.state = "draft"

    def action_confirm(self):
        self.state = "confirmed"

    def action_invoice(self):
        self.state = "invoiced"
