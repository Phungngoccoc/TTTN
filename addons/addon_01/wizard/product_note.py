from odoo import models, fields

class ProductNoteWizard(models.TransientModel):
    _name = 'product.note.wizard'
    _description = 'Product Note Wizard'

    product_id = fields.Many2one('product.template', string='Product', required=True)
    note = fields.Text(string='Note')

    def save_note_action(self):
        self.product_id.write({'description': self.note})
        return {'type': 'ir.actions.act_window_close'}
