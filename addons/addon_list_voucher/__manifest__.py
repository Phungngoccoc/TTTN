{
    'name': 'Voucher List Page',
    'version': '1.0',
    'summary': 'Module hiển thị danh sách voucher',
    'category': 'Website',
    'author': 'Your Name',
    'depends': ['website'],
    'data': [
        'views/voucher_list_template.xml',
    ],
    'assets': {
    'web.assets_frontend': [
        'addon_list_voucher/static/src/scss/style.scss',
        'addon_list_voucher/static/src/img/logo.webp',  
    ],
    },
    'installable': True,
    'application': True,
}