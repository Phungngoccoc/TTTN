from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class ProductNoteWizard(models.TransientModel):
    _name = 'product.note.wizard'
    _description = 'Product Note Wizard'

    product_id = fields.Many2one('product.template', string="Product", required=True)  
    note = fields.Text(string="Note", required=True)  # Trường ghi chú
    is_active = fields.Boolean(string="Active", default=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('note') or vals['note'].strip() == '':
                raise ValidationError("Ghi chú không được để trống hoặc chỉ chứa khoảng trắng!")
        return super(ProductNoteWizard, self).create(vals_list)

    def save_note_action(self):
        if not self.note or self.note.strip() == '':
            raise UserError("Ghi chú không được để trống hoặc chỉ chứa khoảng trắng!")

        if self.product_id:
            self.product_id.write({'product_note': self.note})  # Cập nhật ghi chú vào sản phẩm

        return {'type': 'ir.actions.act_window_close'}
