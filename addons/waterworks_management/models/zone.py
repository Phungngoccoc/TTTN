from odoo import models, fields

class WaterZone(models.Model):
    _name = 'water.zone'
    _description = 'Khu vực cấp nước'

    name = fields.Char(required=True)
    note = fields.Text()
