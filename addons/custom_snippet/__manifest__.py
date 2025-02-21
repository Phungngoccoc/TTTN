{
    "name": "Custom Snippet",
    "summary": "Thêm một snippet tùy chỉnh vào trình tạo trang Odoo",
    "version": "1.0",
    "author": "Your Name",
    "website": "https://yourwebsite.com",
    "category": "Website",
    "depends": ["website"],
    "data": [
        "views/snippets/s_custom_snippet.xml",
        "views/snippets/options.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            "custom_snippet/static/src/snippets/s_custom_snippet/000.js",
            "custom_snippet/static/src/snippets/s_custom_snippet/000.scss",
            "custom_snippet/static/src/snippets/s_custom_snippet/option.js",
            "custom_snippet/static/src/options.scss"
        ]
    },
    "installable": True,
    "application": False,
}