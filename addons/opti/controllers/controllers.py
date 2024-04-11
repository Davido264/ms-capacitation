# -*- coding: utf-8 -*-
# from odoo import http


# class Opti(http.Controller):
#     @http.route('/opti/opti', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/opti/opti/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('opti.listing', {
#             'root': '/opti/opti',
#             'objects': http.request.env['opti.opti'].search([]),
#         })

#     @http.route('/opti/opti/objects/<model("opti.opti"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('opti.object', {
#             'object': obj
#         })

