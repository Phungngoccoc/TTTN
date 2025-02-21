{
    'name': 'Custom Snippet',
    'summary': 'Thêm snippet tùy chỉnh cho website Odoo',
    'version': '1.0',
    'category': 'Website',
    'author': 'Your Name',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/snippets/s_custom_snippet.xml',
        'views/snippets/options.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_snippet/static/src/snippets/s_custom_snippet/000.scss',
            'custom_snippet/static/src/snippets/s_custom_snippet/000.js',
            'custom_snippet/static/src/snippets/s_custom_snippet/option.js',
            'custom_snippet/static/src/options.scss',
        ],
    },
    'installable': True,
    'application': False,
}
