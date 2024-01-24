from odoo import fields, models, api


class DeviceAttributeValue(models.Model):
    _name = 'device.attribute.value'

    name = fields.Char(string="Name")
    device_attribute_id = fields.Many2one('device.attribute', string='DeviceAttributeId')

    _sql_constraints = [('unique_field', 'unique(name,device_attribute_id)', 'Field must be unique')]