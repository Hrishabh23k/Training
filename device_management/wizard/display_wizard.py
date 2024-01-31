from odoo import fields, models, api


class DisplayWizard(models.TransientModel):
    _name = 'display.wizard'

    name = fields.Char(string="Name")

    @api.model
    def default_get(self, fields):
        res = super(DisplayWizard, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        res['name'] = "Device Management"
        return res



