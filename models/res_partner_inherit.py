# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    cdn_customer_id = fields.Many2one(comodel_name='cdn.customer', string='Customer')
    nomor_kendaraan = fields.Char(related='cdn_customer_id.nomor_kendaraan', string='Nomor Kendaraan', readonly=False)
    jenis_kendaraan = fields.Selection(related='cdn_customer_id.jenis_kendaraan', string='Jenis Kendaraan', readonly=True)

    @api.onchange('cdn_customer_id')
    def _onchange_cdn_customer(self):
        for rec in self:
            if rec.cdn_customer_id:
                rec.name = rec.cdn_customer_id.name or rec.name
                rec.phone = rec.cdn_customer_id.no_hp or rec.phone
                rec.nomor_kendaraan = rec.cdn_customer_id.nomor_kendaraan or rec.nomor_kendaraan
