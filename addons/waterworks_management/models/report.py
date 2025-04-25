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
