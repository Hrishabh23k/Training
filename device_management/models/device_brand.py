from odoo import fields, models, api


class DeviceBrand(models.Model):
    _name = 'device.brand'

    name = fields.Char(string="Name")
    device_model_id = fields.One2many('device.model', 'device_brand_id', string='DeviceModelIds')

    _sql_constraints = [('unique_field', 'unique(name)', 'Field must be unique')]