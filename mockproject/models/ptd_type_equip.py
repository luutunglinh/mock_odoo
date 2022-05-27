# -*- coding: utf-8 -*-
from odoo import fields, models
class TypeOfEquipment(models.Model):
    _name = "ptd.type.equip"
    _description = "type of equipment"

    name = fields.Char(string='Loại thiết bị', required = True)
    device_group_id = fields.Many2one(
        string="Nhóm thiết bị",
        comodel_name='ptd.device.group',
        required=True,
        ondelete='restrict'
    )
    note = fields.Text(string='Ghi chú')
