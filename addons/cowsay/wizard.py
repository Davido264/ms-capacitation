# -*- coding: utf-8 -*-

from odoo import fields, models, api

class MessageWizard(models.TransientModel):
    _name = 'message.wizard'

    message = fields.Text('Message')
