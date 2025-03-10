{
    'name': 'Custom Boostrap',
    'description': 'Custom Theme',
    'category': 'Website/Theme',
    'version': '15.0.0',
    'depends': ['website'],
    'assets': {
        # 'web._assets_primary_variables': [
        #     ('prepend', 'website_airproof/static/src/scss/primary_variables.scss'),
        # ],
        'web.assets_frontend': [
            ('append', 'website_airproof/static/src/scss/bootstrap_overridden.scss'),
        ],
        # 'web._assets_frontend_helpers': [
        #     ('prepend', 'website_airproof/static/src/scss/bootstrap_overridden.scss'),
        #  ],
    }
}