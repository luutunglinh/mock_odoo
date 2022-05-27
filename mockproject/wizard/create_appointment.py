# -*- coding: utf-8 -*-
from odoo import models, fields,api
class CreateAppointment(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description="create appointment"

    name_device = fields.Many2one('ptd.measuring.device', string="Mã QLTS")
    dmg_time = fields.Date(string="Thời gian hỏng", required=True)
    dmg_reason = fields.Text(string="Nguyên nhân hỏng", required=True)

    # def default_get(self,fields):
    #     res = super(CreateAppointment,self).default_get(fields)
    #     print("context",self.env.context)
    #     if self.env.context.get('active_id'):
    #         res['asset_code'] = self.env.context.get('active_id')
    #     delta = self.env['ptd.broken.equip'].create(
    #                {'name': self.asset_code, 'dmg_time': self.dmg_time, 'dmg_reason': self.dmg_reason})
    #     return res,delta

    @api.model
    def default_get(self,fields):
        res = super(CreateAppointment,self).default_get(fields)
        print("context",self.env.context)
        res["name_device"] = self.env.context.get('active_id')
        print(res["name_device"])
        return res
        # if self.env.context.get('active_id'):
        #     res['asset_code'] = self.env.context.get('active_id')


    def mutil_appointment(self):
        ids = self.env.context['active_ids']  # selected record ids
        print(ids) #lấy id
        change = self.env["ptd.measuring.device"].browse(ids)
        #change_status = self.env["ptd.measuring.device"].search(id='button_create_appointment')
        print(change.asset_code) #lấy phần tử

        new_data = {}

        if change.status != 'wait_approve':
            change.status = 'wait_approve'
        if change.asset_code:
            new_data["asset_code"] = change.asset_code
            print('change_asset_code',new_data["asset_code"])
        # if change.name:
        #     new_data["name_device"] = change.name
        if self.dmg_time:
            new_data["dmg_time"] = self.dmg_time
            print(new_data)
        if self.dmg_reason:
            new_data["dmg_reason"] = self.dmg_reason
            #đổ dữ liệu qua model khác
        # delta = self.env['ptd.measuring.device'].create(
        #         {'name': change.name, 'dmg_time': self.dmg_time,
        #          'dmg_reason': self.dmg_reason})

        change.write(new_data)







