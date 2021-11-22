# -- coding: utf-8 --
from odoo import models, fields
from odoo.exceptions import ValidationError
from odoo.http import request


class Operaciones(models.Model):
    _name = 'operaciones'

    tipo_operacion = fields.Selection([('recarga', 'Recarga'), ('compra', 'Consumo'),
                                       ('devolucion', 'Devoluciones')])
    estado_operacion = fields.Selection([('confirmado', 'Confirmado'), ('pendiente', 'Pendiente')])
    fecha = fields.Date('Fecha')
    hora = fields.Float(string='Hora')
    id_cliente = fields.Many2one('res.partner', string='Cliente')
    importe_total = fields.Float('Importe')
