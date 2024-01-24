from odoo import fields, models, api


class DeviceSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    panel = fields.Boolean(string="Panel")

    def set_values(self):
        super(DeviceSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('xyz', self.panel)

    @api.model
    def get_values(self):
        res = super(DeviceSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            panel=params.get_param('xyz')
        )
        return res
