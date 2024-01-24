from odoo import models, api, fields


class SaleOrderWizard(models.TransientModel):
    _name = "sale.order.wizard"
    _description = "Wizard for sale order"

    sale_id = fields.Many2one('sale.order', string="SaleId")
    c_line_id = fields.One2many('customer.order.line.wizard', 'so_line_wizard', string="Sale Line")


    @api.model
    def default_get(self, fields):
        res = super(SaleOrderWizard, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        sale_order = self.env['sale.order'].browse(active_id)
        custom_order_line = []

        for order_line in sale_order.order_line:
            custom_order_line.append((0, 0, {
                'product': order_line.product_id.name,
                'desc': order_line.name,
                'quantity': order_line.product_uom_qty,
                'unit_pr': order_line.price_unit
            }))

        res['sale_id'] = active_id
        res['c_line_id'] = custom_order_line
        return res

    def save_object(self):
        sale_order = self.sale_id
        sale_order.customer_order_line_id.unlink()
        for rec in self.c_line_id:
            val = {
                'product': rec.product,
                'desc': rec.desc,
                'quantity': rec.quantity,
                'unit_pr': rec.unit_pr
            }
            print(rec.product, rec.desc)
            sale_order.customer_order_line_id = [(0, 0, val)]


class CustomerOrderLineWizard(models.TransientModel):
    _name = 'customer.order.line.wizard'
    _description = "Customer Order Line"

    so_line_wizard = fields.Many2one('sale.order.wizard', string="Sale_Order_Line_wizard")
    col_id = fields.Many2one('customer.order.line', string="ColId")
    product = fields.Many2one('product.product', string='Product')
    desc = fields.Text(string="Description")
    quantity = fields.Float(string="Quantity")
    unit_pr = fields.Float(string="UnitPrice")
