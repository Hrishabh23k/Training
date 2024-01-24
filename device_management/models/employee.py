from odoo import fields, models, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    device_ids = fields.One2many('device.assignment', 'employee_id', string="DeviceId")
