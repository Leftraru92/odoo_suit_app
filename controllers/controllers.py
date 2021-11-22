# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class SuitApp(http.Controller):
     @http.route('/suit_app/vista/<int:tipo>', auth='public', website=True)
     def control(self, tipo):

        if tipo == 1:

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

            return request.render("suit_app.id_vista_tabla", jdato)
        elif tipo == 2:

            q = """
                     select sum(o.importe_total), 
                             r.name 
                     from operaciones o,
                          res_partner r
                     where o.id_cliente = r.id
                     group by r.name
                     order by 1;
                     """

            request.cr.execute(q)
            best_buyers = request.cr.fetchall()

            l = ""
            for b in best_buyers:
                l += '{ y: %s, label: "%s" },'%(b[0],b[1])

            l = '[' + l + ']'
            dp = 'dataPoints: ' + l

            js_grafico = """
                         <script>
                             window.onload = function () {

                             var chart = new CanvasJS.Chart("chartContainer", {
                                 animationEnabled: true,

                                 title:{
                                     text:"Mejores compradores"
                                 },
                                 axisX:{
                                     interval: 1
                                 },
                                 axisY2:{
                                     interlacedColor: "rgba(1,77,101,.2)",
                                     gridColor: "rgba(1,77,101,.1)"
                                 },
                                 data: [{
                                     type: "bar",
                                     name: "companies",
                                     axisYType: "secondary",
                                     color: "#014D65",
                                     dataPoints:
                                 }]
                             });
                             chart.render();

                             }
                             </script>
                     """
            js_grafico = js_grafico.replace('dataPoints:', dp)

            jgrafico = {
                "best_buyers": js_grafico
            }

            return request.render("suit_app.id_vista_grafico", jgrafico)
        else:
            return "<n1>Tipo no válido</n1>"