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

    total = fields.Float(string="Total", default=16000, readonly=True)
    pay = fields.Float(string="Pay", default=0)
    paid = fields.Float(string='Paid', readonly=True, compute='_compute_paid', store=True)
    remaining = fields.Float(string='Remaining', readonly=True, compute='_compute_remaining', store=True)
    student_id = fields.Many2one('odoo.student', string="student")

    @api.depends('pay')
    def _compute_paid(self):
        self.paid = self.paid + self.pay

    @api.depends('total','paid')
    def _compute_remaining(self):
        self.remaining = self.total - self.paid

    # @api.constrains('student_id')
    # def _check_month(self):
    #     month_list = []
    #     for m in self.student_id:
    #         month_list.append(m.month)
    #     print(month_list)
        # if self.fees_id.month in month_list:
        #     raise ValidationError("Month Cannot be repeat")
