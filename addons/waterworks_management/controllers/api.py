from odoo import http
from odoo.http import request

class WaterAPI(http.Controller):
    @http.route('/api/water/consumption', type='json', auth='user')
    def post_consumption(self, **kwargs):
        data = kwargs.get('data', [])
        results = []
        for entry in data:
            meter = request.env['water.meter'].sudo().search([('name', '=', entry.get('meter_code'))], limit=1)
            if meter:
                request.env['water.consumption'].sudo().create({
                    'meter_id': meter.id,
                    'month': entry.get('month'),
                    'year': entry.get('year'),
                    'start_index': entry.get('start'),
                    'end_index': entry.get('end'),
                    'read_status': 'done',
                    'read_date': entry.get('read_date'),
                    'read_by': request.env.user.id
                })
                results.append({'meter': meter.name, 'status': 'created'})
            else:
                results.append({'meter': entry.get('meter_code'), 'status': 'not_found'})
        return {'result': results}
