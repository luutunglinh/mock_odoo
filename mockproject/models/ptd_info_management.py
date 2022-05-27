# -*- coding: utf-8 -*-
from odoo import models, fields,api
class PtdInfomanagement(models.Model):
    _name = "ptd.info.management"
    _description = "Management Information"

    direct_unit_manager_id = fields.Many2one(
        comodel_name="ptd.direct.unit.manager",
        string="Tên quản lý",
        required="True"
    )
    direct_manager_id = fields.Char(string="Direct manager", required="True")
    user = fields.Many2one('res.users', string="User", required="True")
    level_one_manager = fields.Many2one(
        comodel_name="ptd.direct.unit.manager",
        string="Quản lý đơn vị cấp độ 1",
        required="True"

    )
    install_location = fields.Many2one(
        comodel_name="ptd.lab",
        string="Install location",
        required="True"
    )
    defence_ministry = fields.Boolean(string="Defence ministry")
    reports = fields.Text(string="investment TTR ")
    inves_project = fields.Text(string="Investment projects")
    inves_value = fields.Float(string="Investment value")
    handover_file = fields.Binary(string="Handover of equipment")
    lic_users = fields.Binary(string="License for users")

    measuring_device_id1 = fields.Many2one('ptd.measuring.device',string="Management infomation")




