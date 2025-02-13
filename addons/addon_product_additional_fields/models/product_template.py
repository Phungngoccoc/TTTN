from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    chat_lieu = fields.Text(string="Chất liệu")
    nguon_goc_chat_lieu = fields.Text(string="Nguồn gốc chất liệu")
    mau_sac = fields.Text(string="Màu sắc")
    nhuom_mau_tu_nhien = fields.Text(string="Nhuộm màu tự nhiên")
    hoa_tiet = fields.Text(string="Họa tiết")
    video_hinh_anh_lam_ra_san_pham = fields.Text(string="Video/Hình ảnh làm ra sản phẩm")
    uu_diem_chat_lieu = fields.Text(string="Ưu điểm chất liệu")
    nhuoc_diem_chat_lieu = fields.Text(string="Nhược điểm chất liệu")
    link_blog_tim_hieu_them_ve_chat_lieu = fields.Text(string="Link blog tìm hiểu thêm về chất liệu")
    huong_dan_cham_soc_san_pham = fields.Text(string="Hướng dẫn chăm sóc sản phẩm")
