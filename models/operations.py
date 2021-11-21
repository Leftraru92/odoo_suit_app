# -- coding: utf-8 --
from odoo import models, fields
from odoo.exceptions import ValidationError
from odoo.http import request


class Operaciones(models.Model):
    _name = 'operaciones'

    name = fields.Char('Operacion')
    numero_operacion = fields.Char('Nro Operacion')
    tipo_operacion = fields.Selection([('recarga', 'Recarga'), ('compra', 'Consumo'),
                                       ('transferencia', 'Transferencia'), ('devolucion', 'Devoluciones'),
                                       ('cancelacion', 'Cancelación'), ('otros', 'Otros')])
    estado_operacion = fields.Selection([('activo', 'Activo'), ('inactivo', 'Inactivo')])
    fecha = fields.Date('Fecha')
    hora = fields.Float(string='Hora')
    id_cliente = fields.Many2one('res.partner', string='Cliente')
    importe_total = fields.Float('Total')
