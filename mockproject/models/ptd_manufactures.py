# -*- coding: utf-8 -*-
from odoo import models, fields
class PtdManufactures(models.Model):
    _name = "ptd.manufactures"
    _description = "Manufactures information"

    name = fields.Char(string='Nhà sản xuất', required=True)
    producer_code = fields.Char(string="Mã nhà sản xuất")
    address_production = fields.Char(string="Địa chỉ nhà sản xuất")
    note = fields.Text(string='Ghi chú')





