{
    'name': 'Tips & Tricks',
    'version': '1.0',
    'summary': 'Addon for Tips and Tricks functionality',
    'description': 'A custom addon to manage Tips and Tricks.',
    'author': 'Your Name',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'views/tips_view.xml',
        'views/tricks_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
