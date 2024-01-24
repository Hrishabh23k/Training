from odoo import fields, models, api


class DeviceType(models.Model):
    _name = 'device.type'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    sequence = fields.Many2one('ir.sequence', string="Sequence")
    device_attribute_ids = fields.One2many('device.attribute', 'device_type_id', string="DeviceAttributeIds")
    device_model_ids = fields.One2many('device.model', 'device_type_id', string="DeviceModelIds")
    device_ids = fields.One2many('device', 'device_type_id', string="DeviceIds")

    _sql_constraints = [('unique_field', 'unique(name,code)', 'Field must be unique')]