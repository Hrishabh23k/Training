from odoo import fields, models, api


class ExamWizard(models.TransientModel):
    _name = 'exam.wizard'

    s_wizard = fields.Many2one('odoo.student', string="Swizard")
    name = fields.Char(string="Name", readonly="True")
    sw = fields.One2many('subject.wizard', 'ws', string="SW")
    marks = fields.Integer(string="Marks")

    @api.model
    def default_get(self, fields):
        res = super(ExamWizard, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        student_rec = self.env['odoo.student'].browse(active_id)
        custom_order_line = []

        for order_line in student_rec.subject_id:
            custom_order_line.append((0, 0, {
                'subject': order_line.subject,
            }))

        res['name'] = student_rec.name
        res['sw'] = custom_order_line
        return res

    def save_result(self):
        active_id = self.env.context.get('active_id')
        s_rec = self.env['odoo.student'].browse(active_id)
        s_rec.exam_id.unlink()
        for rec in self.sw:
            val = {
                #'student_id': s_rec,
                'sub': rec.subject,
                'marks': rec.marks,
                'outof': rec.outof
            }
            print(s_rec, rec.subject, rec.marks, rec.outof)
            s_rec.exam_id = [(0, 0, val)]



class SubjectWizard(models.TransientModel):
    _name = 'subject.wizard'

    sub_id = fields.Many2one('odoo.subject', string="SubId")
    ws = fields.Many2one('exam.wizard', string="WS")
    subject = fields.Char(string="Subject")
    marks = fields.Integer(string="Marks")
    outof = fields.Integer(string="Out_of", default=100)
