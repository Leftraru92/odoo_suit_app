# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class SuitApp(http.Controller):
     @http.route('/suit_app/vista/<int:tipo>', auth='public', website=True)
     def control(self, tipo):
        dataset = [
            ['titulo1', 10],
            ['titulo2', 20],
            ['titulo3', 30]
        ]

        jdato = {
            "dato": dataset
        }

        if tipo == 1:
            return request.render("suit_app.id_vista_tabla", jdato)
        elif tipo == 2:
             return request.render("suit_app.id_vista_grafico", jdato)
        else:
            return "<n1>Tipo no válido</n1>"