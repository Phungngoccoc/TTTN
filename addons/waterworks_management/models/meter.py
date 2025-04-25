from odoo import models, fields

class WaterMeter(models.Model):
    _name = 'water.meter'
    _description = 'Đồng hồ nước'

    name = fields.Char(required=True)
    customer_id = fields.Many2one('water.customer')
    type = fields.Selection([
        ('main', 'Đồng hồ chính'),
        ('sub', 'Đồng hồ phụ')
    ], default='main')
    status = fields.Selection([
        ('working', 'Hoạt động'),
        ('broken', 'Hỏng')
    ], default='working')
