from odoo import api, models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    thong_tin_them = fields.Text(string="Thông tin bổ sung cho lead")
