from odoo import http
from odoo.http import request

class QuyTrinhHopTacController(http.Controller):

    @http.route('/form-dat-hang-mau', auth='public', website=True)
    def show_quy_trinh(self, **kw):
        return request.render('addon_page_form_dat_hang_mau.form-dat-hang-mau', {})
