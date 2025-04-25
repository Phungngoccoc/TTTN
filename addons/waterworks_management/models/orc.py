from odoo import models, fields
import base64

class WaterOCR(models.Model):
    _name = 'water.ocr'
    _description = 'OCR đồng hồ nước'

    image = fields.Binary(string='Ảnh')
    meter_id = fields.Many2one('water.meter')
    detected_index = fields.Float(string='Chỉ số AI')
    note = fields.Text()
    detected_at = fields.Datetime(auto_now_add=True)

    def action_detect_ocr(self):
        for rec in self:
            rec.detected_index = 123.45  # giả lập OCR result
            rec.note = "Mô phỏng AI đọc ảnh"
