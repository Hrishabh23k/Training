from odoo import fields, models, api


class DeviceBrand(models.Model):
    _name = 'device.brand'

    name = fields.Char(string="Name")
    device_model_id = fields.One2many('device.model', 'device_brand_id', string='DeviceModelIds')

    # _sql_constraints = [('unique_field', 'unique(name)', 'Field must be unique')]

    def add_record(self):
        active_id = self.env.context.get('active_id')
        d_b = self.env['device.model'].browse(active_id)
        vals = {
            'name': self.name,
        }
        # d_b.create(vals)
        # self.create({'name': 'hp', 'device_model_id': [(0, 0, {'name': 'hp1'})]})
        self.write({'device_model_id': [(0, 0, {'name': self.name+" "+str(self.id+1)})]})
        print("Record add")

    def update_record(self):
        # self.write({'name': [(1, self.id, {'name': "New"})]})
        self.write({
             'device_model_id': [(1, 3, {'name': 'new'})],
         })

    def remove_record(self):
        self.write({
            'device_model_id': [(2, 7)],
        })

    def cut_record(self):
        self.write({
            'device_model_id': [(3, 7)],
        })

    def link_record(self):
        self.write({
            'device_model_id': [(4, 6)],
        })

    def unlink_record(self):
        self.write({'device_model_id': [(5, 0, 0)]})

    def replace_record(self):
         new_child_ids = [(0, 0, {'name': 'New Child 1'}),
                          (0, 0, {'name': 'New Child 2'}),
                          (0, 0, {'name': 'New Child 3'})]

         for rec in new_child_ids:
            res = self.env['device.model'].create(rec)

         self.write({'child_ids': [(6, 0, [3, 8, 9])]})
