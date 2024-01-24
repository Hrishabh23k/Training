from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    custom_purchase_id = fields.One2many('custom.purchase', 'purchase_order_id', string="CustomPurchase")
    total = fields.Float(string="Total", compute="_compute_total")
    account_move_line = fields.One2many('account.move.line', 'purchase_order_line', string="PurchaseAccount")

    def pass_value(self):
        self.custom_purchase_id.unlink()
        print("Hello")
        for rec in self.order_line:
            custom_purchase = {
                'product': rec.product_id.id,
                'desc': rec.name,
                'quantity': rec.product_qty,
                'unit_pr': rec.price_unit,
                'sub_total': rec.price_subtotal
            }
            self.custom_purchase_id = [(0, 0, custom_purchase)]

    @api.depends('custom_purchase_id.sub_total')
    def _compute_total(self):
        s = 0
        for price in self.custom_purchase_id:
            s += price.sub_total
        self.total = s

    def action_send_mail(self):
        print("mail sent")
        # mail_template = self.env.ref('additional_sale.email_template_name')
        # mail_template.send_mail(self.id, force_send=True)
        mail = self.env['mail.mail']
        values = {
            'email_from': 'hrishabh.nagar@ksolves.com',
            'email_to': 'hrishabhnagar9111@gmail.com',
            'body_html': 'Hello',
        }
        mail_rec = mail.create(values)
        mail_rec.send()



class CustomPurchase(models.Model):
    _name = 'custom.purchase'

    purchase_order_id = fields.Many2one('purchase.order', string="PurchaseOrder")
    product = fields.Many2one('product.product', string="Product")
    desc = fields.Text(string="Description")
    quantity = fields.Float(string="Quantity")
    unit_pr = fields.Float(string="UnitPrice")
    sub_total = fields.Float(string="SubTotal")



class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    additional_price = fields.Float(string="AdditionalPrice")
