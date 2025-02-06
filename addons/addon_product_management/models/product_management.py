from odoo import models, fields

class ProductManagement(models.Model): 
    _name = "product.management"
    _description = "Product Management"
    
    product_name = fields.Char(string="Product name")