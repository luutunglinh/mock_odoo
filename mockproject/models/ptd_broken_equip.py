# -*- coding: utf-8 -*-
from odoo import models, fields,api
class BrokenEquip(models.Model):
    _name = "ptd.broken.equip"
    _description = "Broken equipment"

    name = fields.Char(string="QLTS")
    # name_device = fields.Char(string="Name device")
    dmg_time = fields.Date(string="Damaged time", required=True)
    dmg_reason = fields.Text(string="Damaged reason", required=True)