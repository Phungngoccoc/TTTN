from odoo import http
from odoo.http import request

class VoucherController(http.Controller):

    @http.route('/voucher', type='http', auth="public", website=True)
    def list_vouchers(self, **kwargs):
        vouchers = request.env['loyalty.card'].sudo().search([])
        return request.render('addon_list_voucher.voucher_page', {'vouchers': vouchers})
