from odoo import fields, models, api


class DeviceModel(models.Model):
    _name = 'device.model'

    name = fields.Char(string="Name")
    device_type_id = fields.Many2one('device.type', string='DeviceTypeId')
    device_brand_id = fields.Many2one('device.brand', string="DeviceBrandId")

    _sql_constraints = [('unique_field', 'unique(device_type_id,device_brand_id)', 'Field must be unique')]