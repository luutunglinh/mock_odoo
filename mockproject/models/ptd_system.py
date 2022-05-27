# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
from openerp.exceptions import ValidationError
class Ptdsystem(models.Model):
    _name = "ptd.system"
    _description = "System"

    name = fields.Char(string='Tên hệ thống*', required=True)
    infor_code = fields.Char(string='Mã hệ thống*', required=True)
    note = fields.Text(string = "Ghi chú")

    _sql_constraints = [
        ('unique_infor_code','unique(infor_code)','Mã hệ thống đã tồn tại')
    ]










