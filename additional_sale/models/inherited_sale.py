from odoo import fields, models, api


class InheritedSale(models.Model):
    _inherit = "sale.order"

    character = fields.Char(string="Character")
    customer_order_line_id = fields.One2many('customer.order.line', 'so_line', string="Customer_order_line")
    total = fields.Float(compute='_compute_total', string="Total")

    def add_custom_bill(self):
        invoices = self.mapped('invoice_ids')
        invoices.custom_bill_id.unlink()
        for rec in self.customer_order_line_id:
            sale_bill = {
                'product': rec.product,
                'desc': rec.desc
            }
            invoices.custom_bill_id = [(0, 0, sale_bill)]

    @api.depends('customer_order_line_id.sub_total')
    def _compute_total(self):
        s = 0
        for price in self.customer_order_line_id:
            s += price.quantity * price.unit_pr
        self.total = s


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Float(string="DiscountAmount")


class CustomerOrderLine(models.Model):
    _name = 'customer.order.line'
    _description = "Customer Order Line"

    so_line = fields.Many2one('sale.order', string="Sale_Order_Line")
    customer_order_line_wizard_id = fields.One2many('customer.order.line.wizard', 'col_id', string="ColIdw")
    product = fields.Many2one('product.product', string='Product')
    desc = fields.Text(string="Description")
    quantity = fields.Float(string="Quantity", default=1)
    unit_pr = fields.Float(string="UnitPrice")
    sub_total = fields.Float(string="SubTotal")


