from odoo import http
from odoo.http import request

class ProductController(http.Controller):

    @http.route('/list-product', auth='public', website=True)
    def list_products(self, **post):
        products = request.env['product.template'].sudo().search([])
        return request.render('addon_list_product.product_list_template', {'products': products})
