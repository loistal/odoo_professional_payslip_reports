# -*- coding: utf-8 -*-
from openerp import http

# class VctRapportPaie(http.Controller):
#     @http.route('/vct_rapport_paie/vct_rapport_paie/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vct_rapport_paie/vct_rapport_paie/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vct_rapport_paie.listing', {
#             'root': '/vct_rapport_paie/vct_rapport_paie',
#             'objects': http.request.env['vct_rapport_paie.vct_rapport_paie'].search([]),
#         })

#     @http.route('/vct_rapport_paie/vct_rapport_paie/objects/<model("vct_rapport_paie.vct_rapport_paie"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vct_rapport_paie.object', {
#             'object': obj
#         })