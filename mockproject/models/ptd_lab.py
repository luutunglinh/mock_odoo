# -*- coding: utf-8 -*-
from odoo import models, fields
class Ptdlab(models.Model):
    _name = "ptd.lab"
    _description = "Lab"

    name = fields.Char(string = "Nơi lắp đặt")
    address = fields.Char(string="Vị trí ")
    user = fields.Char(string="Khách hàng sử dụng")
    note = fields.Text(string="Ghi chú")




