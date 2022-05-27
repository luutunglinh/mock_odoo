# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Ptdwarningdate(models.Model):
    _name = "ptd.warning.date"
    _description = "Warning date"

    ok = fields.Many2one('ptd.measuring.device',
                           string='Mã phương tiện'
                           )
    name_ptd = fields.Char(string="Tên phương tiện")
    serial_number = fields.Char(string="Serial cần tìm kiếm")
    status_KDHC = fields.Selection(
        string='Tình trạng KĐ/HC',
        selection=[('1', 'Quá hạn dưới 3 tháng'),
                   ('2', 'Quá hạn từ 3 đến 6 tháng'),
                   ('3', 'Quá hạn trên 6 tháng'),
                   ('4', 'Tất cả'),
                   ],
        tracking=True,
        default='4')

    note = fields.Text(string='Note')
    @api.onchange('ok')
    def change_func(self):
        ptd = self.env['ptd.measuring.device'].search([])
        values={}
        for rec in ptd:
            values['id'] = rec.name
            values['name_equip'] = rec.asset_code
        print(values)





















