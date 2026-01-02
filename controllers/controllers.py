# -*- coding: utf-8 -*-
# from odoo import http


# class DsAutoClean(http.Controller):
#     @http.route('/ds_auto_clean/ds_auto_clean', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ds_auto_clean/ds_auto_clean/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ds_auto_clean.listing', {
#             'root': '/ds_auto_clean/ds_auto_clean',
#             'objects': http.request.env['ds_auto_clean.ds_auto_clean'].search([]),
#         })

#     @http.route('/ds_auto_clean/ds_auto_clean/objects/<model("ds_auto_clean.ds_auto_clean"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ds_auto_clean.object', {
#             'object': obj
#         })

