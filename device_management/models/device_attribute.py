from odoo import fields, models, api


class DeviceAttribute(models.Model):
    _name = 'device.attribute'

    name = fields.Char(string="Name")
    device_type_id = fields.Many2one('device.type', string='DeviceTypeId')
    required = fields.Boolean(string="Required")
    device_attribute_value_id = fields.One2many('device.attribute.value', 'device_attribute_id', string='DeviceAttributeValueId')

    _sql_constraints = [('unique_field', 'unique(name)', 'Field must be unique')]