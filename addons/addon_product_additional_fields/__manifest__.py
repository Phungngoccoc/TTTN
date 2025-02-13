{
    'name': 'Product Additional Fields',
    'version': '1.0',
    'summary': 'Thêm các trường bổ sung cho sản phẩm',
    'description': 'Module này thêm các trường như chất liệu, nguồn gốc, màu sắc, hướng dẫn chăm sóc, v.v. vào sản phẩm.',
    'category': 'Product',
    'author': 'Your Name',
    'depends': ['product'],
    'data': [
        'views/product_template_views.xml',
        'views/detail_product_view.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
