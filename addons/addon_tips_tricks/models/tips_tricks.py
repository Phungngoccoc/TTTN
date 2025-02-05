from odoo import models, fields

class Tips(models.Model):
    _name = 'tips.tricks'
    _description = 'Tips'
    
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)