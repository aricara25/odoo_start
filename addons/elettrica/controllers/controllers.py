# -*- coding: utf-8 -*-
# from odoo import http


# class Elettrica(http.Controller):
#     @http.route('/elettrica/elettrica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/elettrica/elettrica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('elettrica.listing', {
#             'root': '/elettrica/elettrica',
#             'objects': http.request.env['elettrica.elettrica'].search([]),
#         })

#     @http.route('/elettrica/elettrica/objects/<model("elettrica.elettrica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('elettrica.object', {
#             'object': obj
#         })
