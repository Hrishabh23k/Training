from odoo import fields, models, api


class Subject(models.Model):
    _name = 'odoo.subject'
    _rec_name = 'subject'

    subject = fields.Char(string="Subject")
    ss_id = fields.Many2many('odoo.student', 'exam_subject', 'exid', 'subid', string="SubjectStudent")
    swid = fields.One2many('subject.wizard', 'sub_id', string="SubWizard")

    _sql_constraints = [
        ('subject_uniq', 'unique (subject)', """subject should not repeated!"""),
    ]
