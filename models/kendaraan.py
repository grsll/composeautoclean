from odoo import models, fields, api



class Kendaraan(models.Model):
    _name = 'cdn.kendaraan'
    _description = 'tabel kendaraan'
    
    customer_id = fields.Many2one(comodel_name='cdn.customer', string='Customer', required=True)
    jenis_kendaraan = fields.Selection(related='customer_id.jenis_kendaraan', string='Jenis Kendaraan', readonly=True)
    customer_name = fields.Char(related='customer_id.name', string='Nama Customer', readonly=True)
    customer_alamat = fields.Text(related='customer_id.alamat', string='Alamat Customer', readonly=True)
    
    
