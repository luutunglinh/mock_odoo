# -*- coding: utf-8 -*-
from odoo import models, fields,api
class PTDdirectmanagermanagement(models.Model):
    _name = "ptd.direct.unit.manager"
    _description = "Direct unit manager management"
    group_id = fields.Integer(string='Nhóm ID*')
    name = fields.Char(string = 'Chi nhánh quản lý trực tiếp',required = True)
    path = fields.Char(string = 'Đường dẫn*', required = True)
    # status = fields.Integer(string = 'Trạng thái', required = True)
    #parent_ID = fields.Integer(string="ParentID*",required=True)
    direct_manager_fullname = fields.Char(string = 'Tên người quản lý trục tiếp')
    level = fields.Integer(string = 'Các cấp',requried = True)

