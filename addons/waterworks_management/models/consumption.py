from odoo import models, fields, api

class WaterConsumption(models.Model):
    _name = 'water.consumption'
    _description = 'Tiêu thụ nước'

    meter_id = fields.Many2one('water.meter')
    month = fields.Integer()
    year = fields.Integer()
    start_index = fields.Float()
    end_index = fields.Float()
    volume = fields.Float(compute='_compute_volume', store=True)
    unit_price = fields.Float(default=7500)
    total_price = fields.Float(compute='_compute_total', store=True)
    read_status = fields.Selection([
        ('pending', 'Chưa ghi'),
        ('done', 'Đã ghi'),
        ('error', 'Lỗi')
    ], default='pending')
    anomaly_code = fields.Selection([
        ('normal', 'Bình thường'),
        ('broken_meter', 'Hỏng'),
        ('missing', 'Mất'),
        ('suspect', 'Bất thường')
    ], default='normal')
    read_by = fields.Many2one('res.users')
    read_date = fields.Datetime()

    @api.depends('start_index', 'end_index')
    def _compute_volume(self):
        for rec in self:
            rec.volume = max(rec.end_index - rec.start_index, 0)

    @api.depends('volume', 'unit_price')
    def _compute_total(self):
        for rec in self:
            rec.total_price = rec.volume * rec.unit_price
