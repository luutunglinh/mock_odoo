# -*- coding: utf-8 -*-
from odoo import models, fields
class Unitmeasuremanager(models.Model):
    _name = "ptd.unit.measure.manager"
    _description = "Unit measure manager"

    #quản lý đơn vị đo
    name = fields.Char(string='Mã đơn vị đo', required = True)
    unit_name = fields.Char(string ='Tên đơn vị đo', required = True)
    attachment = fields.Binary(string="Giấy chứng nhận đơn vị",required=True)
    note = fields.Text(string="Ghi chú")