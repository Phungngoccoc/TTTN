from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_note = fields.Text(string="Product Note", readonly=True)
