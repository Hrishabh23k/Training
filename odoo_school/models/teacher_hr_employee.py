import contextlib
from odoo import fields, models, api, sql_db, SUPERUSER_ID
from datetime import date


class Teacher(models.Model):
    _inherit = 'hr.employee'
    _description = "Teacher model inherit hr_employee"

    class_line = fields.Many2many('teacher.class', 'class_teacher', 'cid', 'tid', string="ClassId")
    teacher_name = fields.Many2many('odoo.student', 'student_teacher', 'tid', 'sid', string="Teacher")
    subject_name = fields.Many2one('odoo.subject', string="Subject")

    def action_confirm(self):
        #res = super().action_confirm()
        connection = sql_db.db_connect('odoo_16_5')
        with contextlib.closing(connection.cursor()) as cr:
            cr.autocommit(True)
            env = api.Environment(cr, SUPERUSER_ID, {})
            env['hr.employee'].create({'name': self.name, 'work_email': self.work_email})

    def create_duplicate(self):
        self.env['hr.employee'].create({'name': self.name, 'work_email': self.work_email})

    def action_update(self):
        connection = sql_db.db_connect('odoo_16_4')
        with contextlib.closing(connection.cursor()) as cr:
            cr.autocommit(True)
            env = api.Environment(cr, SUPERUSER_ID, {})
            env['hr.employee'].write({'work_email': self.work_email})

