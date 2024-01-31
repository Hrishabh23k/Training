from odoo import fields, models, api


class Employee(models.Model):
    _name = 'device.assignment'

    name = fields.Char(string="Code")
    device_id = fields.Many2one('device', string="Device")
    employee_id = fields.Many2one('hr.employee', string="EmployeeId")
    date_start = fields.Date(string="Start")
    date_expire = fields.Date(string="Expire")
    state = fields.Selection(string="State", selection=[('New', 'new'), ('Draft', 'draft'), ('Approved', 'approved'),
                                                        ('Returned', 'returned'), ('Rejected', 'rejected')])

    change_check = fields.Boolean(string="Change", compute='_compute_change')
    device_rating = fields.Integer('Rating')
    # Widget fields
    url = fields.Char('Url')
    email = fields.Char('Email')
    domain = fields.Char('Domain')
    color = fields.Char('Color')
    num = fields.Integer('Num', default=30)


    # _sql_constraints = [('unique_field', 'unique(name)', 'Field must be unique')]

    @api.depends('change_check')
    def _compute_change(self):
        res = self.env['ir.config_parameter'].get_param('xyz')
        self.change_check = res

    def button_click(self):
        self.state = 'Approved'
        # for i in self:
        #     print(i.id)
        #     # query = f"""
        #     #             UPDATE device_assignment SET state=('Approved') WHERE id=('{i.id}');
        #     #         """
        #     # self.env.cr.execute(query)
        # self.state = 'Approved'
        print("Button click")

