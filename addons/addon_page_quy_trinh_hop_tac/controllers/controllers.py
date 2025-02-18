from odoo import http
from odoo.http import request

class QuyTrinhHopTacController(http.Controller):

    @http.route('/quy-trinh-hop-tac', auth='public', website=True)
    def show_quy_trinh(self, **kw):
        return request.render('addon_page_quy_trinh_hop_tac.quy_trinh_template', {})
