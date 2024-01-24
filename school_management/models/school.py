from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class School(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    attachment = fields.Binary(string="Attachment")
    image = fields.Image(string="Image")
    name = fields.Many2one('res.partner', string="Student", required=True)
    date_of_birth = fields.Date(string="DOB", required=True)
    age = fields.Integer(string="Age", compute="_compute_age", tracking=True, readonly=True)
    gender = fields.Selection(string="Gender", selection=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                              required=True)
    department = fields.Many2one('school.department', string="Department", required=True)
    standard = fields.Integer(string="Standard")
    section = fields.Selection(string="Section", selection=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    subject_ids = fields.One2many('school.subject', 'student_id', string='Subject')
    status = fields.Selection(string="Status", selection=[('Draft', 'Draft'), ('Confirm', 'Confirm')], default='Draft')
    # Student Personal Information
    father = fields.Char(string="Father")
    mother = fields.Char(string="Mother")
    father_occupation = fields.Text(string="FatherOccupation")
    mother_occupation = fields.Text(string="MotherOccupation")
    sibling = fields.Boolean(string='Sibling', default=False)
    sibling_name = fields.Char(string='SiblingName')
    address = fields.Text(string="Address")
    # Result
    first_sem = fields.Float(string='FirstSem')
    second_sem = fields.Float(string='SecondSem')
    Third_sem = fields.Float(string='ThirdSem')
    percentage = fields.Float(compute="_calc_per", store=True, string='Average')
    sum = fields.Integer(string="Sum", compute="_compute_sum")
    assign = fields.Char(compute="assign_name", tracking=True, readonly=True)
    roll = fields.Integer(compute="_compute_roll", string="roll")


    @api.depends('subject_ids.number')
    def _compute_sum(self):
        s = 0
        for record in self:
            for rec in record.subject_ids:
                s += rec.number
        self.sum = s

    @api.depends('first_sem', 'second_sem', 'Third_sem')
    def _calc_per(self):
        self.percentage = (self.first_sem + self.second_sem + self.Third_sem) / 3

    @api.depends('age')
    def _compute_age(self):
        today = date.today()
        self.age = today.year - self.date_of_birth.year

    @api.depends('roll')
    def _compute_roll(self):
        increment = 1
        for record in self:
            for rec in record.name:
                increment += 1
        self.roll = increment

    @api.onchange('standard')
    def onchange_standard(self):
        self.section = "A"

    @api.constrains('date_of_birth')
    def check_date_of_birth(self):
        if self.date_of_birth.year >= 2021:
            raise ValidationError('Birth year should be less than 2021')

    @api.constrains('standard')
    def check_standard(self):
        if self.standard > 12 or self.standard < 1:
            raise ValidationError("Invalid standard")

    def confirm_status(self):
        self.status = 'Confirm'

    def cancel_status(self):
        self.status = 'Draft'

    def department_action(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'school.department',
            'res_id': self.department.id,
            'view_mode': 'form',
        }

    @api.model
    def default_get(self, fields):
        val = {'user_id': self.env.user.name}
        return val['user_id']

    def assign_name(self):
        self.assign = self.create_uid.name
