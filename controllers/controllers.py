# -*- coding: utf-8 -*-
# from odoo import http


# class ManaDashboardGauge(http.Controller):
#     @http.route('/mana_dashboard_gauge/mana_dashboard_gauge', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mana_dashboard_gauge/mana_dashboard_gauge/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mana_dashboard_gauge.listing', {
#             'root': '/mana_dashboard_gauge/mana_dashboard_gauge',
#             'objects': http.request.env['mana_dashboard_gauge.mana_dashboard_gauge'].search([]),
#         })

#     @http.route('/mana_dashboard_gauge/mana_dashboard_gauge/objects/<model("mana_dashboard_gauge.mana_dashboard_gauge"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mana_dashboard_gauge.object', {
#             'object': obj
#         })
