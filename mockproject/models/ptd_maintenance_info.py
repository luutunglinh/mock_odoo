# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime, timedelta
import calendar
class PtdManitainInfor(models.Model):
    _name = "ptd.maintenance.info"
    _description = "Mantanance information"

    implement_date = fields.Date(string =" Ngày thực hiện",required = True)
    note = fields.Text(string="Ghi chú")
    attachment = fields.Binary(string="Đính kèm")
    #expiry_date = fields.Date(string="Expiration Date")
    main_info = fields.Many2one(
        comodel_name="ptd.measuring.device",
    )
    test = fields.Many2one('ptd.measuring.device',string="Mã QLTS")


        # def onchange_date(self):
    #     #measuring_device = self.env['ptd.measuring.device'].browse(self.maintain_cycle)
    #     measuring_device = self.env['ptd.measuring.device'].search([])
    #     print(measuring_device.maintain_cycle)
    #     for item in measuring_device:
    #         print(item.name)
    #         if item.name:
    #             print('maintain', item.maintain_cycle)
    #     print('expiry_date')
    #     for rec in self:
    #         if rec.implement_date == False:
    #             print("XXX")
    #         else:
    #             rec.expiry_date = rec.implement_date + timedelta(days=10)
    #             print('expri',rec.expiry_date)










