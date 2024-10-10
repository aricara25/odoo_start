# -*- coding: utf-8 -*-
# from odoo import http


# class Segnalazione(http.Controller):
#     @http.route('/segnalazione/segnalazione/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/segnalazione/segnalazione/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('segnalazione.listing', {
#             'root': '/segnalazione/segnalazione',
#             'objects': http.request.env['segnalazione.segnalazione'].search([]),
#         })

#     @http.route('/segnalazione/segnalazione/objects/<model("segnalazione.segnalazione"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('segnalazione.object', {
#             'object': obj
#         })
