import contextlib
from odoo import fields, models, api, sql_db, SUPERUSER_ID
from datetime import date
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = 'odoo.student'

    rollno = fields.Integer(string="ScholarNo", compute='_compute_roll')
    name = fields.Char(string="Name")
    date_of_birth = fields.Date(string="DOB", required=True)
    age = fields.Integer(string="Age", compute="_compute_age", tracking=True, readonly=True)
    gender = fields.Selection(string="Gender", selection=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                              required=True)
    exam_id = fields.One2many('odoo.exam', 'student_id', string="StudentExam")
    subject_id = fields.Many2many('odoo.subject', 'exam_subject', 'subid', 'exid', string="StudentSubject")
    e_wizard = fields.One2many('exam.wizard', 's_wizard', string="Ewizard")
    # Basic Details
    father = fields.Char(string="Father")
    mother = fields.Char(string="Mother")
    father_occupation = fields.Text(string="FatherOccupation")
    mother_occupation = fields.Text(string="MotherOccupation")
    sibling = fields.Boolean(string='Sibling', default=False)
    sibling_name = fields.Char(string='SiblingName')
    address = fields.Text(string="Address")
    # Student Class
    class_id = fields.Many2one('teacher.class', string="Class")
    # Student Teacher
    teacher_name = fields.Many2many('hr.employee', 'student_teacher', 'sid', 'tid', string="Teacher")
    # student fees
    fees_id = fields.One2many('student.class.fees', 'student_id', string="Fees")
    confirmation = fields.Boolean(string="Confirm", default=False, readonly=True)
    total = fields.Integer(string="Total")


    @api.depends('age')
    def _compute_age(self):
        today = date.today()
        self.age = today.year - self.date_of_birth.year

    @api.depends('age')
    def _compute_roll(self):
        self.rollno = 1000 + self.id


    def create_subject(self):
        query = """
                INSERT INTO odoo_subject(subject)
                VALUES('Zoology')
        """
        self.env.cr.execute(query)

    def create_student(self):
        query = f"""
            INSERT INTO odoo_student(name)
            VALUES('{self.name}')
        """
        self.env.cr.execute(query)

    def delete_student(self):
        query = f"""
            DELETE FROM odoo_student WHERE name = ('{self.name}')
        """
        self.env.cr.execute(query)

    def confirm_true(self):
        self.confirmation = True

    def confirm_false(self):
        self.confirmation = False

    def add_student(self):
        connection = sql_db.db_connect('odoo_16_5')
        with contextlib.closing(connection.cursor()) as cr:
            cr.autocommit(True)
            env = api.Environment(cr, SUPERUSER_ID, {})
            env['odoo.student'].create({'name': self.name, 'gender': self.gender, 'date_of_birth': self.date_of_birth})

    def update_student(self):
        connection = sql_db.db_connect('odoo_16_4')
        with contextlib.closing(connection.cursor()) as cr:
            cr.autocommit(True)
            env = api.Environment(cr, SUPERUSER_ID, {})
            env['odoo.student'].write({'name': self.name, 'gender': self.gender, 'date_of_birth': self.date_of_birth})


class Exam(models.Model):
    _name = 'odoo.exam'

    student_id = fields.Many2one('odoo.student', string='SubjectStudent')
    subject = fields.Many2one('odoo.subject', string="Subject")
    sub = fields.Char(string="Stream")
    marks = fields.Integer(string="Marks")
    outof = fields.Integer(string="Out_of", default=100)
