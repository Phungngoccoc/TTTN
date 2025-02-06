from odoo import models, fields

class Tip(models.Model):
    _name = 'tip.and.trick.tip'
    _description = 'Tip'

    name = fields.Char('Tip Name')
    description = fields.Text('Description')


class Trick(models.Model):
    _name = 'tip.and.trick.trick'
    _description = 'Trick'

    name = fields.Char('Trick Name')
    description = fields.Text('Description')
