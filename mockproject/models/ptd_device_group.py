# -*- coding: utf-8 -*-
from odoo import models, fields, api
class PtdDeviceGroup(models.Model):
    _name = "ptd.device.group"
    _description = "Device group management"

    name = fields.Char(string='Nhóm thiết bị', required = True)
    code = fields.Char(string="Mã nhóm thiết bị")
    note = fields.Text(string='Ghi chú')


    #các trường id,create_uid, create_date, write_uid, write_date đã tự tạo sẵn khi tạo table