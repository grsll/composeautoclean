# -*- coding: utf-8 -*-
{
    "name": "Compose Auto Clean",
    "summary": "Modul manajemen cuci mobil otomatis",
    "description": """
Manajemen cuci mobil dengan fitur pendaftaran pelanggan, data kendaraan, dan riwayat pesanan.
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    "category": "Services",
    "version": "0.1",
    "depends": ["base", "mail"],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/vehicle.xml",
        "views/carwash_order.xml",
        "views/customer.xml",
        "views/views.xml",
        "views/templates.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
}
