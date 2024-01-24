from odoo import fields, models, api


class TeacherClass(models.Model):
    _name = 'teacher.class'
    _description = "Teacher class model"
    _rec_name = 'standard'

    standard = fields.Integer(string="Class")
    section = fields.Char(string="Section")
    student_line = fields.One2many('odoo.student', 'class_id', string="Class_student")
    teacher_id = fields.Many2many('hr.employee', 'class_teacher', 'tid', 'cid', string="TeacherId")
    fees_month = fields.Many2many('student.class.fees', 'class_fees', 'fid', 'cid', string="Month")

    _sql_constraints = [
        ('standard_uniq', 'unique (standard)', """Class should not repeated!"""),
    ]
