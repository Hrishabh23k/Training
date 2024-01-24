from odoo import fields, api, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    custom_bill_id = fields.One2many('custom.bill', 'account_move_id', string="CustomBillId")


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    discount_amount = fields.Float(related='sale_line_ids.discount_amount', string="DiscountAmount")
    additional_price = fields.Float(related='purchase_line_id.additional_price', string="AdditionalPrice")
    purchase_order_line = fields.Many2one('purchase.order', string='AccountPurchase')

    # @api.depends('additional_price')
    # def _compute_additional_price(self):
    #     pli = self.mapped('purchase_line_id')
    #     self.additional_price = pli.additional_price
    #
    # @api.onchange('purchase_line_id.additional_price')

class CustomBill(models.Model):
    _name = 'custom.bill'

    account_move_id = fields.Many2one('account.move', string="AccountMoveId")
    product = fields.Char(string="Product")
    desc = fields.Text(string="Description")

