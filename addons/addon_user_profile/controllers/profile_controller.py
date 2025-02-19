from odoo import http
from odoo.http import request

class UserProfileController(http.Controller):

    @http.route('/profile', type='http', auth="user", website=True)
    def user_profile(self, **kwargs):
        user = request.env.user
        profile = request.env['user.profile'].search([('user_id', '=', user.id)], limit=1)

        return request.render('addon_user_profile.profile_page', {
            'profile': profile
        })

    @http.route('/profile/update', type='http', auth="user", website=True, methods=['POST'])
    def update_profile(self, **kwargs):
        user = request.env.user
        profile = request.env['user.profile'].search([('user_id', '=', user.id)], limit=1)

        # Update profile data
        profile.write({
            'name': kwargs.get('name'),
            'email': kwargs.get('email'),
            'phone': kwargs.get('phone'),
            'bio': kwargs.get('bio'),
        })

        # Update avatar if exists
        if 'avatar' in kwargs:
            profile.write({
                'avatar': kwargs['avatar'].read()
            })

        return request.redirect('/profile')
