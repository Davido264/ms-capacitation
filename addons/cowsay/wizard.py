# -*- coding: utf-8 -*-

from odoo import fields, models, api

class MessageWizard(model.TransientModel):
    _name = 'message.wizard'

    message = fields.Text('Message', required=True)

    @api.multi
    def action_ok(self):
        """ close wizard"""
        return {'type': 'ir.actions.act_window_close'}
    
