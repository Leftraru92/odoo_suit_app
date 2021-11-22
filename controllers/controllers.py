# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class SuitApp(http.Controller):
     @http.route('/suit_app/vista/<int:tipo>', auth='public', website=True)
     def control(self, tipo):

        q = """ 
        select 	o.id, 
                o.tipo_operacion, 
                o.estado_operacion, 
                to_char(o.fecha, 'dd/mm/YY'), 
                to_char(to_timestamp((o.hora)*60), 'MI:SS'),
                r.name, 
                to_char(o.importe_total, 'FM9,999,999')
        from operaciones o,
             res_partner r
        where o.id_cliente = r.id
        order by o.fecha desc, o.hora desc;
        """

        request.cr.execute(q)
        operaciones = request.cr.fetchall()

        jdato = {
            "dato": operaciones
        }

        if tipo == 1:
            return request.render("suit_app.id_vista_tabla", jdato)
        elif tipo == 2:
             return request.render("suit_app.id_vista_grafico", jdato)
        else:
            return "<n1>Tipo no válido</n1>"