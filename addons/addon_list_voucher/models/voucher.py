from odoo import models, fields

class LoyaltyCard(models.Model):
    _name = "loyalty.card"
    _inherit = "loyalty.card"  # Kế thừa từ model hiện có
    _description = "Phiếu quà tặng"

    code = fields.Char(string="Mã voucher")
    amount = fields.Float(string="Giá trị")
    expiration_date = fields.Date(string="Ngày hết hạn")