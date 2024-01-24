from odoo import fields, models

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject Student'

    student_id = fields.Many2one('school.student', string='SubjectStudent')
    name = fields.Char(string="SubjectName")
    code = fields.Char(string="Subject Code")
    number = fields.Integer(string="Number")


