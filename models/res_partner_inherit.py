# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    jenis_kelamin = fields.Selection(
        [
            ("laki", "Laki-laki"),
            ("perempuan", "Perempuan"),
        ],
        string="Jenis Kelamin",
    )
