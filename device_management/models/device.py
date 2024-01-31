from odoo import fields, models, api


class Employee(models.Model):
    _name = 'device'

    name = fields.Char(string="Serial")
    shared = fields.Boolean(string="Shared")
    device_type_id = fields.Many2one('device.type', string="DeviceTypeId")
    device_brand_id = fields.Many2one('device.brand', string="DeviceBrandId")
    device_model_id = fields.Many2one('device.model', string="DeviceModelId")
    attributes = fields.One2many('device.attribute.assignment', 'device_id', string="Attributes")

    _sql_constraints = [('unique_field', 'unique(name)', 'Field must be unique')]

    def check_rpc(self):
        print("...................")
