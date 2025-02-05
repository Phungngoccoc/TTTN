from odoo import models, fields, api

class ProductNoteWizard(models.TransientModel):
    _name = 'product.note.wizard'
    _description = 'Product Note Wizard'

    product_id = fields.Many2one('product.template', string="Product", required=True, readonly=True)
    note = fields.Text(string="Note")
    is_active = fields.Boolean(string="Active", default=True)  # Toggle button

    def save_note_action(self):
        """Hàm lưu ghi chú vào sản phẩm"""
        if self.product_id:
            self.product_id.write({'description_sale': self.note})
        return {'type': 'ir.actions.act_window_close'}
