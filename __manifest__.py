# -*- coding: utf-8 -*-
{
    "name": "Compose Auto Clean",
    "summary": "Modul manajemen cuci mobil otomatis",
    "description": """
Manajemen cuci mobil dengan fitur pendaftaran pelanggan, data kendaraan, dan riwayat pesanan.
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "product", "mail"],
    # always loaded
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/templates.xml",
        "views/menu.xml",
        "views/kendaraan.xml",
        "views/res_partner_views.xml",
        "views/carwash_order.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
