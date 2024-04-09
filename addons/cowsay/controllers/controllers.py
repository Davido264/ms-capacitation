# -*- coding: utf-8 -*-
# from odoo import http


# class Cowsay(http.Controller):
#     @http.route('/cowsay/cowsay', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cowsay/cowsay/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cowsay.listing', {
#             'root': '/cowsay/cowsay',
#             'objects': http.request.env['cowsay.cowsay'].search([]),
#         })

#     @http.route('/cowsay/cowsay/objects/<model("cowsay.cowsay"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cowsay.object', {
#             'object': obj
#         })

