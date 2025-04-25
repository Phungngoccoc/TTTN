from odoo import models, fields

class WaterRoute(models.Model):
    _name = 'water.route'
    _description = 'Tuyến đọc đồng hồ nước'

    name = fields.Char(required=True)
    zone_id = fields.Many2one('water.zone')
    reader_id = fields.Many2one('res.users', string='Nhân viên đọc')
