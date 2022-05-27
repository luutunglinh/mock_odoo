# -*- coding: utf-8 -*-
from odoo import models, fields
class Ptdevicecategorymanager(models.Model):
    _name = "ptd.device.category.manager"
    _description = "Device category manager"

    # nối đến code many2one PTĐ
    name = fields.Char(string='Mã danh mục  thiết bị ', required=True)
    device_category_name = fields.Char(string='Tên danh mục thiết bị')
    type_id = fields.Many2one('ptd.type.equip',string="Loại thiết bị")
    is_sync = fields.Boolean(string='Đồng bộ')
    note = fields.Text(string="Ghi chú")





