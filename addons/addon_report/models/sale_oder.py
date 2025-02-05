from odoo import api, models,fields,_ 

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    def my_custom_method(self):
        pass