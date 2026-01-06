from odoo import models, fields, api

class Kendaraan(models.Model):
    _name = 'cdn.kendaraan'
    _description = 'Tabel Kendaraan'

    name = fields.Char(string='Nama Kendaraan', required=True)
    jenis = fields.Selection([
        ('mobil', 'Mobil'),
        ('motor', 'Motor'),
        ('truck', 'Truck'),
    ], string='Jenis Kendaraan', required=True)
    nomor_polisi = fields.Char(string='Nomor Polisi', required=True)
    pemilik = fields.Char(string='Pemilik Kendaraan', required=True)