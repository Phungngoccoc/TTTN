from odoo import models, fields

class WaterCustomer(models.Model):
    _name = 'water.customer'
    _description = 'Khách hàng cấp nước'

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    address = fields.Char()
    phone = fields.Char()
    customer_type = fields.Selection([
        ('residential', 'Hộ dân'),
        ('business', 'Doanh nghiệp'),
        ('government', 'Cơ quan')
    ], required=True)
    status = fields.Selection([
        ('active', 'Đang sử dụng'),
        ('inactive', 'Ngừng sử dụng')
    ], default='active')
    route_id = fields.Many2one('water.route')
