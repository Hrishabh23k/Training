from odoo import models, fields, api


class Department(models.Model):
    _name = 'school.department'
    _description = 'School Department'

    name = fields.Char(string="DepartmentName", required=True)
    staff = fields.Integer(string="Staff", compute="_calculate_staff")
    branch = fields.Char(string="Branch", required=True)
    address = fields.Text(string="Address")
    staff_ids = fields.One2many('school.staff', 'dep', string='StaffId')
    status = fields.Selection(string="Status", selection=[('Draft', 'Holding'), ('Confirm', 'Done')], default='Draft', readonly=True)

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Department must be unique'),
    ]

    @api.depends('staff_ids', 'staff')
    def _calculate_staff(self):
        c = 0
        for record in self:
            for rec in record.staff_ids:
                c += 1
        self.staff = c

    def confirm_status(self):
        self.status = 'Confirm'

    def cancel_status(self):
        self.status = 'Draft'


class Staff(models.Model):
    _name = 'school.staff'
    _description = 'School Staff'

    name = fields.Char(string="StaffName", required=True)
    dep = fields.Many2one('school.department', string="Department")
    age = fields.Integer(string="Age", required=True)
    experience = fields.Integer(string="Experience", required=True)
    phd = fields.Char(string="PHD")
