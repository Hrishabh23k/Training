from odoo import models, fields


class Teacher(models.Model):
    _name = 'school.teacher'

    name = fields.Char(string='Teacher')
    age = fields.Integer(string='Age')
