# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vehicle(models.Model):
    _name = "fleet.vehicle"
    _inherit = "fleet.vehicle"
    _description = "Vehicles"

    state = fields.Selection(
        selection=[
            ("available", "Disponible"),
            ("unavailable", "No Disponible"),
            ("dispached", "Despachado"),
        ],
        string="Disponibilidad",
        help="Disponibilidad del vehículo"
    )

    route = fields.Many2one(
        comodel_name="opti.route",
        string="Ruta",
        help="Ruta que recorre el vehículo"
    )
