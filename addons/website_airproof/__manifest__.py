{
    'name': 'Custom Theme Airproof',
    'description': 'Custom Theme',
    'category': 'Website/Theme',
    'version': '15.0.0',
    'depends': ['website'],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'website_airproof/static/src/scss/primary_variables.scss'),
        ],
    }
}
