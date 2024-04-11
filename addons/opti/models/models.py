# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class opti(models.Model):
#     _name = 'opti.opti'
#     _description = 'opti.opti'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

