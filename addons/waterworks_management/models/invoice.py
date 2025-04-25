from odoo import models, fields

class WaterInvoice(models.Model):
    _name = 'water.invoice'
    _description = 'Hóa đơn nước'

    name = fields.Char()
    customer_id = fields.Many2one('water.customer')
    date = fields.Date()
    amount = fields.Float()
    state = fields.Selection([
        ('unpaid', 'Chưa thu'),
        ('paid', 'Đã thu'),
        ('debt', 'Nợ')
    ], default='unpaid')

    def action_send_invoice(self):
        template = self.env.ref('waterworks_management.email_template_invoice')
        for rec in self:
            rec.message_post_with_template(template.id)
