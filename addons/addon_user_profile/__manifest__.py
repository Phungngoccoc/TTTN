{
    "name": "User Profile Page",
    "summary": "Cung cấp trang cá nhân hóa cho người dùng",
    "author": "Ngoc",
    "website": "http://localhost:8069",
    "version": "1.0",
    "depends": ["base", "website"],
    "data": [
        "views/profile_template.xml",
        'security/ir.model.access.csv'
    ],
    "installable": True,
    "application": True,
}