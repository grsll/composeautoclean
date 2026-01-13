from odoo import models, fields


class CarwashOrder(models.Model):
    _inherit = "carwash.order"

    operational_state = fields.Selection(
        [
            ("antri", "Antrean"),
            ("cuci", "Sedang Dicuci"),
            ("kering", "Pengeringan/Vacuum"),
            ("selesai", "Selesai"),
        ],
        string="Status Pengerjaan",
        default="antri",
    )

    queue_no = fields.Char(string="Nomor Antrean", readonly=True, copy=False)
    estimation_time = fields.Char(string="Estimasi Selesai")

    def action_confirm(self):
        res = super(CarwashOrder, self).action_confirm()
        for rec in self:
            if not rec.queue_no:
                today_count = self.search_count(
                    [
                        ("create_date", ">=", fields.Date.today()),
                        ("state", "!=", "draft"),
                    ]
                )
                rec.queue_no = str(today_count).zfill(3)
        return res
