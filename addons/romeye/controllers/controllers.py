# -*- coding: utf-8 -*-
# from odoo import http


# class Romeye(http.Controller):
#     @http.route('/romeye/romeye/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/romeye/romeye/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('romeye.listing', {
#             'root': '/romeye/romeye',
#             'objects': http.request.env['romeye.romeye'].search([]),
#         })

#     @http.route('/romeye/romeye/objects/<model("romeye.romeye"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('romeye.object', {
#             'object': obj
#         })
