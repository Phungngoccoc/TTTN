from odoo import http
from odoo.http import request

class ProductController(http.Controller):

    @http.route('/voucher', auth='public', website=True, csrf=False)
    def list_voucher(self, **kwargs):
        search_query = kwargs.get('search', '').strip()
        category_id = kwargs.get('category')
        sort_order = kwargs.get('sort_order', 'asc')  # Sắp xếp mặc định: Giá tăng dần
        page = int(kwargs.get('page', 1))  # Trang mặc định: 1
        per_page = 3  # Số sản phẩm hiển thị mỗi trang

        domain = []

        # Lọc theo từ khóa tìm kiếm
        if search_query:
            domain.append(('name', 'ilike', search_query))

        # Lọc theo danh mục sản phẩm
        if category_id:
            try:
                category_id = int(category_id)
                domain.append(('categ_id', '=', category_id))
            except ValueError:
                pass  # Bỏ qua nếu category_id không hợp lệ

        # Sắp xếp theo giá
        order_by = 'list_price asc' if sort_order == 'asc' else 'list_price desc'

        # Tính offset (bỏ qua số lượng sản phẩm trước trang hiện tại)
        offset = (page - 1) * per_page

        # Truy vấn tổng số sản phẩm để tính số trang
        total_products = request.env['product.template'].sudo().search_count(domain)
        total_pages = (total_products // per_page) + (1 if total_products % per_page else 0)

        # Truy vấn sản phẩm theo phân trang
        products = request.env['product.template'].sudo().search(domain, order=order_by, limit=per_page, offset=offset)

        # Truy vấn danh mục sản phẩm
        categories = request.env['product.category'].sudo().search([])

        return request.render('addon_list_product.product_list_template', {
            'products': products,
            'categories': categories,
            'search_query': search_query,
            'category_id': category_id,
            'sort_order': sort_order,
            'page': page,
            'total_pages': total_pages
        })
