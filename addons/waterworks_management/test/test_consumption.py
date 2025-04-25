from odoo.tests.common import TransactionCase

class TestWaterConsumption(TransactionCase):
    def setUp(self):
        super().setUp()
        self.customer = self.env['water.customer'].create({
            'name': 'Test KH',
            'code': 'KH001',
            'customer_type': 'residential'
        })
        self.meter = self.env['water.meter'].create({
            'name': 'M001',
            'customer_id': self.customer.id
        })

    def test_volume_compute(self):
        c = self.env['water.consumption'].create({
            'meter_id': self.meter.id,
            'month': 4,
            'year': 2025,
            'start_index': 100,
            'end_index': 130
        })
        self.assertEqual(c.volume, 30)
        self.assertEqual(c.total_price, 30 * 7500)

    def test_ocr_mock(self):
        ocr = self.env['water.ocr'].create({
            'meter_id': self.meter.id,
            'image': b'dummy'
        })
        ocr.action_detect_ocr()
        self.assertTrue(ocr.detected_index > 0)
        self.assertIn('Mô phỏng', ocr.note)
from odoo import models, fields

class ReportWaterSummary(models.Model):
    _name = 'report.water.summary'
    _auto = False
    _description = 'Tổng hợp ghi chỉ số theo khu vực'

    zone = fields.Char()
    route = fields.Char()
    read_status = fields.Selection([
        ('pending', 'Chưa ghi'),
        ('done', 'Đã ghi'),
        ('error', 'Lỗi')
    ])
    total = fields.Integer()

    def init(self):
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW report_water_summary AS (
                SELECT row_number() OVER () as id,
                       z.name as zone,
                       r.name as route,
                       c.read_status,
                       COUNT(*) as total
                FROM water_consumption c
                JOIN water_meter m ON c.meter_id = m.id
                JOIN water_customer cu ON m.customer_id = cu.id
                LEFT JOIN water_route r ON cu.route_id = r.id
                LEFT JOIN water_zone z ON r.zone_id = z.id
                GROUP BY z.name, r.name, c.read_status
            )
        """)
