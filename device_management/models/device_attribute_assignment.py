from odoo import fields, models, api

class DeviceAttributeAssignment(models.Model):
    _name = 'device.attribute.assignment'

    device_id = fields.Many2one('device', string="DeviceId")
    device_attribute_id = fields.Many2one('device.attribute', string='DeviceAttributeId')
    device_attribute_value_id = fields.Many2one('device.attribute.value', string='DeviceAttributeValueId')

    _sql_constraints = [('unique_field', 'unique(name,device_attribute_id)', 'Field must be unique')]