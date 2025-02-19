from odoo import models, fields

class UserProfile(models.Model):
    _name = "user.profile"
    _description = "User Profile"

    user_id = fields.Many2one('res.users', string="User", required=True)
    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    avatar = fields.Binary(string="Avatar")
    bio = fields.Text(string="Bio")
