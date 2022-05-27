# -*- coding: utf-8 -*-
from odoo import models, fields
class PtdSpecInfo(models.Model):
    _name = "ptd.spec.info"
    _description = 'Specifications'

    para = fields.Char(string='Tham số *', required=True,
                       track_visibility='onchange')
    value = fields.Char(string='Giá trị *', required=True,
                        track_visibility='onchange')
    unit_id = fields.Many2one( comodel_name='ptd.unit.measure.manager',
                               string='Đơn vị đo *',
                               required=True)
    dis_resolution = fields.Char(string=' Độ phân giải*')
    error = fields.Float(string='Sai số *')
    measuring_device_id = fields.Many2one(comodel_name='ptd.measuring.device',
                                           string='Thông số kĩ thuật *')

    note = fields.Text(string="Ghi chú")