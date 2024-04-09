# -*- coding: utf-8 -*-

from odoo import models, fields, api
from cowsay import char_names,get_output_string

class cowsay(models.Model):
    _name = 'cowsay.cowsay'
    _description = 'cow'

    name = fields.Text(required=True, default="cow")
    message = fields.Text(required=True)
    description = fields.Text(required=True)
    # cow = fields.Selection(selection=[(i) for i in char_names],default="cow")
    display = fields.Text(compute="_cowsay")

    @api.depends("message")
    def _cowsay(self):
        for record in self:
            record.display = get_output_string("cows", self.message)

