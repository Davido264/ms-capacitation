# -*- coding: utf-8 -*-

from odoo import models, fields, api


class route(models.Model):
    _name = "opti.route"
    _description = "A route"

    name = fields.Text(
        string="Nombre",
        help="Nombre de la ruta"
    )

    stops = fields.One2many(
        comodel_name="opti.stop",
        inverse_name="route",
        string="Paradas",
        help="Paradas pertenecientes a la ruta"
    )

    vehicles = fields.One2many(
        comodel_name="fleet.vehicle",
        inverse_name="route",
        string="Vehículos",
        help="Vehículos realizando este recorrido"
    )

    cstops = fields.Integer(
        compute="_cstops",
        string="# Paradas",
        help="Cantidad de Paradas existentes"
    )

    cvehicles = fields.Integer(
        compute="_cvehicles",
        string="# Vehículos",
        help="Cantidad de vehículos realizando este recorrido"
    )

    max_time = fields.Integer(
        compute="_max_time",
        string="Tiempo máximo (s)",
        help="Suma total del tiempo de las paradas"
    )

    @api.depends("stops")
    def _cstops(self):
        for entry in self:
            entry.cstops = len(entry.stops)

    @api.depends("stops")
    def _cvehicles(self):
        for entry in self:
            entry.cvehicles = len(entry.vehicles)


    @api.depends("stops.time")
    def _max_time(self):
        for entry in self:
            entry.max_time = sum(i.time for i in entry.stops) #type: ignore
