# -*- coding: utf-8 -*-

from odoo import models, fields, api


class stop(models.Model):
    _name = 'opti.stop'
    _description = 'A stop in a route'

    name = fields.Text(
        string="Nombre",
        help="Nombre de la parada"
    )

    time = fields.Integer(
        string="Tiempo (s)",
        help="Tiempo en segundos en llegar a la parada partiendo de la anterior"
    )

    dtime = fields.Integer(
        string="Tiempo de retraso (s)",
        help="Tiempo adicional en caso de imprevistos"
    )

    lat = fields.Float(
        string="Latitud",
        help="Latitud de la ubiación de la parada"
    )

    lon = fields.Float(
        string="Longitud",
        help="Longitud de la ubiación de la parada"
    )

    route = fields.Many2one(
        comodel_name="opti.route",
        inverse_name="stops",
        string="Ruta",
        help="Ruta a la que pertenece"
    )
