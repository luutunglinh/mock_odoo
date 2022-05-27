# -*- coding: utf-8 -*-
from odoo import models, fields,api
from odoo.exceptions import UserError
from openerp.exceptions import ValidationError
class CreateUpdateinfor(models.TransientModel):
    _name = 'create.update.infor.wizard'
    _description="create update infor"

    code_device = fields.Many2one('ptd.measuring.device', string="Mã QLTS")
    name_device = fields.Char(string="Tên thiết bị")
    unit_using = fields.Boolean(string="Đơn vị sửa dụng")


    status = fields.Selection(
        string='Tình trạng KĐ/HC',
        selection=[('2', 'Tất cả'),
                   ('1', 'Đã KĐ/HC'),
                   ('0', 'Chưa KĐ/HC')],
        tracking=True
    )

    maintain = fields.Selection(
        string='Tình trạng BD',
        selection=[('2', 'Tất cả'),
                   ('1', 'Đã BD'),
                   ('0', 'Chưa BD')],
        tracking=True
    )

    type_of = fields.Selection(
        string='Loại KĐ/HC',
        selection=[('2', 'Tất cả'),
                   ('1', 'Kiểm định'),
                   ('0', 'Hiệu chỉnh')],
        tracking=True
    )


    # create_info = fields.Many2one(comodel_name='ptd.measuring.device',string="Create infor")

    @api.onchange('code_device')
    def _onchange_name_device(self):
        ptd = self.env['ptd.measuring.device'].search([])
        for item in ptd:
            if item.asset_code:
                self.name_device = item.asset_code
                print(self.name_device)


    def mutil_update(self):
        # search = []
        # if self.name_device or self.code_device:
        #     search.append(('asset_code','ilike',self.name_device))
        #     search.append(('name', 'ilike', self.code_device.name))
        #     #search.append(('serial_number', 'ilike', self.serial_number))
        #     print(search)
        #     #('asset_code', '=', self.name_device)
        #     #('asset_code', '=', self.name_device)
        # else:
        #     raise UserError("Please Enter Empty Fields.")
        #
        # if search:
        #     partner = self.env['ptd.measuring.device'].search(search)
        #     if not partner:
        #         raise UserError("This device is not yet created. So, you can not see his details.")

        domain = [('asset_code', 'ilike', self.name_device),('name','ilike',self.code_device.name),
                       ]
        if self.status != '2':
            domain.append(('check', 'ilike', self.status))
        if self.maintain != '2':
            domain.append(('maintain_info', 'ilike', self.maintain))
        if self.type_of != '2':
            domain.append(('type_of', 'ilike', self.type_of))
        partner = self.env['ptd.measuring.device'].search(domain)
        if not partner:
            raise UserError('Không có thiết bị thỏa mãn')
        return {
            'name': ('Searching device '),
            'view_mode': 'tree',
            'views': [(self.env.ref('mockproject.action_ptd_measuring_device_tree').id, 'tree'),
                      (self.env.ref('mockproject.view_ptd_measuring_device_form').id, 'form')],
            'view_id': False,
            #'views': self.env.ref('mockproject.action_ptd_measuring_device_tree').id,
            # 'domain': [('asset_code', 'ilike', self.name_device),('name','ilike',self.code_device.name),
            #            ],
            'domain': domain,
            'res_model': 'ptd.measuring.device',
            # 'search_view_id': self.env.ref('mockproject.action_ptd_type_equip_tree').id,
            'type': 'ir.actions.act_window',
            #'context': {'no_breadcrumbs': True},
            'current': 'new',
        }


