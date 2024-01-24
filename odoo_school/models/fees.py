from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Fees(models.Model):
    _name = 'student.class.fees'
    _rec_name = 'month'

    month = fields.Selection(string="Month", selection=[
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ])

    total = fields.Float(string="Total")
    pay = fields.Float(string="Pay")
    remaining = fields.Float(string='Remaining')
    student_id = fields.Many2one('odoo.student', string="student")

    # @api.constrains('student_id')
    # def _check_month(self):
    #     month_list = []
    #     for m in self.student_id:
    #         month_list.append(m.month)
    #     print(month_list)
        # if self.fees_id.month in month_list:
        #     raise ValidationError("Month Cannot be repeat")
