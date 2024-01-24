from odoo import fields, models, api


class DeviceSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hide_panel = fields.Boolean(string="HidePanel")
