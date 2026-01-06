from odoo import models, fields, api

class Customer(models.Model):
    _name = 'cdn.customer'
    _description = 'Tabel Customer'
    
    name = fields.Char(string='Nama Customer', required=True)
    no_hp = fields.Char(string='No Hp')
    alamat = fields.Text(string='Alamat')
    nomor_kendaraan = fields.Char(string='Nomor Kendaraan')
    jenis_kendaraan = fields.Selection(string='Jenis Kendaraan', selection=[('mobil', 'Mobil'), ('motor', 'Motor'), ('bus', 'Bus')])
    
    
    


