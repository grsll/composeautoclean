# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ds_auto_clean(models.Model):
#     _name = 'ds_auto_clean.ds_auto_clean'
#     _description = 'ds_auto_clean.ds_auto_clean'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

