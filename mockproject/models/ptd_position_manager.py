# -*- coding: utf-8 -*-
from odoo import models, fields
class Ptdpositionmanager(models.Model):
    _name = "ptd.position.manager"
    _description = "Position manager"

    name = fields.Char(string=' Tên quản lý', required = True)
    location = fields.Char(string='Vị trí')
    code_name = fields.Char(string="Mã nhân viên")
    note = fields.Text(string='Ghi chú')


