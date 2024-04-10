# -*- coding: utf-8 -*-

from odoo import models, fields, api
from cowsay import char_names,get_output_string

class cowsay(models.Model):
    _name = 'cowsay.cowsay'
    _description = 'cow'

    name = fields.Text(required=True, default="cow")
    message = fields.Text(required=True)
    description = fields.Text(required=True)
    cow = fields.Selection(selection=[(i,i) for i in char_names],default="cow",string="type")

    def get_output_string(self) -> str:
        return get_output_string(self.cow, self.message) or ""

    def display_popup(self) -> dict:
        id = self.env['message.wizard'].create({'message': self.get_output_string() }).id
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "message.wizard",
            "res_id": id,
            "target": "new"
        }

