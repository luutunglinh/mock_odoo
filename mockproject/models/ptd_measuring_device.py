# -*- coding: utf-8 -*-

from odoo.exceptions import UserError
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta
from odoo import models, fields, api
import re


class Ptdmeasuringdevice(models.Model):
    _name = "ptd.measuring.device"
    _description = "Measure device"

    name = fields.Char("Mã QLTS *", required = "True")
    status = fields.Selection(
        string='Trạng thái sử dụng',
        selection=[('new', 'Đang sử dụng'),
                   ('wait', 'Đang sửa chữa'),
                   ('wait_approve', 'Hư hỏng'),
                   ('approved', 'Thanh lý'),
                   ],
        tracking=True,
        default='new')


    image_id = fields.Binary(attachment=True, string="Ảnh *")
    mer_id = fields.Many2one(
        comodel_name="ptd.device.category.manager",
        inverse_name="name",
        string="Mã chủng loại thiết bị ",
        required = "True"
    )
    asset_code = fields.Char(string="Tên thiết bị",required = "True")
    is_serial = fields.Selection(
        string='Có số hiệu *',
        selection=[('serial', 'Có số hiệu'), ('noserial', 'Không số hiệu')],
        default="serial",
        tracking=True,
        required="True"
    )
    classify = fields.Selection(
        string="Kiểu thiết bị *",
        selection=[('main', 'Thiết bị chính'), ('accessory', 'Thiết bị phụ')],
        default='main',
        tracking=True,
        required="True"
    )

    device_group_id = fields.Many2one(
        "ptd.device.group","Nhóm thiết bị *", ondelete = 'restrict',tracking = True,required = "True"
    )

    type_equip_id = fields.Many2one(
        comodel_name="ptd.type.equip",
        inverse_name="name",
        required="True",
        string="Loại thiết bị")
    system_id = fields.Many2one(
        comodel_name="ptd.system",
        inverse_name="name",
        string="Hệ thống",
        required="True"
    )
    producer_id = fields.Many2one(
        comodel_name="ptd.manufactures",
        inverse_name="name",
        string="Nhà sản xuất",
        required="True"

    )

    model = fields.Char(string="Kí hiệu",required = True)
    serial_number = fields.Char(string="Số sê-ri")

    unit_measure_id = fields.Many2one(
        comodel_name="ptd.unit.measure.manager",
        inverse_name="unit_name",
        string="Đơn vị đo",
        required="True"
    )
    is_standard_equipment = fields.Boolean(
        string='Thiết bị đo lường tiêu chuẩn',
        default=True, tracking=True
    )
    country_id = fields.Many2one("res.country", "Nước sản xuất")

    des = fields.Text(string="Mô tả",size=5,required = True)
    attach = fields.Binary(string ="Đính kèm")
    # quality_status = fields.Selection(
    #     string='Status *',
    #     selection=[('damaged', 'Damaged'), ('good', 'Good'),
    #                ('liquidated', 'Liquidated')],
    #     tracking=True
    # )
    count = fields.Integer(string="Số lượng thiết bị",required=True)
    #Management information
    management_id = fields.One2many(
        comodel_name='ptd.info.management',
        inverse_name='measuring_device_id1',
        string='Quản lý thông tin',
        track_visibility='onchange',
        required="True"
    )
    direct_unit_manager_id = fields.Many2one(
        comodel_name = "ptd.direct.unit.manager",
        string="Chi nhánh quản lý",
        required="True"
    )
    direct_manager_id = fields.Many2one('ptd.position.manager',string="Người quản lý chính",required = "True")
    user = fields.Many2one('res.users', string="Người dùng",required = "True")
    level_one_manager = fields.Many2one(
        comodel_name="ptd.direct.unit.manager",
        string="Quản lý cấp 1",
        required="True"

    )
    install_location = fields.Many2one(
        comodel_name = "ptd.lab",
        string="Vị trí lắp đặt",
        required="True"
    )
    defence_ministry = fields.Boolean(string="Tiêu chuẩn bộ quốc phòng")
    reports = fields.Text(string="TTR đầu tư ")
    inves_project = fields.Text(string="Dự án đầu tư")
    inves_value = fields.Float(string="Giá trị dầu tư")
    handover_file = fields.Binary(string="Bàn giao thiết bị")
    lic_users = fields.Binary(string="Giấy phép người dùng")
    spe_info_ids = fields.One2many(
        comodel_name='ptd.spec.info',
        inverse_name='measuring_device_id',
        string='Thông số kỹ thuật ',
        track_visibility='onchange',
        required="True"
        )

    #quality management
    quality_status = fields.Selection([('available', 'Đang sử dụng'),
                          ('occupied', 'Gần hết hạn'),
                          ('expiry_near','Hết hạn')], string="Trạng thái bảo dưỡng",
                            dafault='available'
                         , store=True)

    dmg_time = fields.Date(string="Thời gian hỏng", default="")
    dmg_reason = fields.Text(string="Lý do hỏng", default="")
    quality_level = fields.Selection(
        string='Mức chất lượng *',
        selection=[('1', 'Cấp 1'),
                   ('2', 'Cấp 2'),
                   ('3', 'Cấp 3'),
                   ('4', 'Cấp 4'),
                   ],
        default='1',
        tracking=True
    )



    transfer_day = fields.Date(string="Ngày chuyển cấp")
    transfer_reason = fields.Text(string="Lý do chuyển cấp")
    standard_link_id = fields.Many2one(
        comodel_name = "ptd.canonical.link.info",
        inverse_name = "name",
        string="Loại liên kết chuẩn"

    )
    cer_active = fields.Boolean(string="Giấy chứng nhận")

    #canonical link
    can_link_info_ids = fields.One2many(
        comodel_name='ptd.canonical.link.info',
        inverse_name='canon_id',
        string='Thông tin liên kế chuẩn',
        track_visibility='onchange',
    )
    #maintain information
    main_info_ids = fields.One2many(
        comodel_name='ptd.maintenance.info',
        inverse_name='main_info',
        string='Thông tin bảo dưỡng',
        track_visibility='onchange',

    )
    maintain_cycle = fields.Integer(string=" Chu kì bảo dưỡng (tháng)")
    standard_link_cycle = fields.Integer(string="Chu kì liên kết chuẩn (tháng)")
    expiry_date = fields.Date(string="Ngày hết hạn")





    # def _compute_count_lead_quotation(self):
    #     for rec in self:
    #         count_cus_quotation = self.env['ptd.maintenance.info'].search_count(
    #             [('id', '=', rec.id)])
    #         rec.maintain_cycle = count_cus_quotation
    #         print(count_cus_quotation)







    #sử lý button
    # create_update_infor_id = fields.One2many(
    #     comodel_name="create.update.infor",
    #     inverse_name = 'create_info',
    #     string="Create update infor",
    #     track_visibility='onchange'
    # )
    # xử lý status
    def button_using_func(self):
        if self.status != 'new':
            self.status = 'new'

    def button_fixing_func(self):
        if self.status != 'new':
            self.status = 'wait'

    def button_buying_func(self):
        if self.status != 'approved':
            self.status = 'approved'

    check = fields.Integer(string="Đã KĐ/HC")
    maintain_info = fields.Integer(string="Đã bảo dưỡng")
    type_of = fields.Integer(string="Loại liên kết")
    @api.onchange('main_info_ids')
    def _maintain_change(self):
        if len(self.main_info_ids):
            self.maintain_info = 1
        else:
            self.maintain_info = 0
    is_birthday = fields.Boolean(string="Gần bảo dưỡng", compute="update_state")
    is_birthday01 = fields.Boolean(string="Hết hạn bảo dưỡng", compute="update_state")

    def year_selection(self):
        year = 2000  # replace 2000 with your a start year
        # year = datetime.datetime.today().year
        # year_list = range(1950, year + 1)
        year_list = []
        while year != 2030:  # replace 2030 with your end year
            year_list.append((str(year), str(year)))
            #print(year_list)
            year += 1
        return year_list
    year_manufacture = fields.Selection(
        year_selection,
        string="Năm sản xuất",
        default="2019",  # as a default value it would be 2019
    )
    year_use = fields.Selection(
        year_selection,
        string="Năm sử dụng",
        default="2020",  # as a default value it would be 2019
    )
    @api.model
    def create(self,vals):
        if vals['name'] == False:
            raise UserError("Trường: mã QLTS trống ")
        else:
            if vals['name'].isalnum() == False:
                raise UserError("Mã QLTS: chỉ gồm ký tự chữ hoặc số")

        if vals['year_manufacture'] != False and vals['year_use'] != False:
            if int(vals['year_manufacture']) > int((vals['year_use'])[:4]):
                raise ValidationError("Năm đưa vào sử dụng không hợp lệ")

        if vals['maintain_cycle'] >= 0 | vals['standard_link_cycle'] >= 0 :
            result = super(Ptdmeasuringdevice, self).create(vals)
        elif vals['maintain_cycle'] < 0:
            raise UserError("Không được để trống chu kì liên kết chuẩn")
        elif vals['standard_link_cycle'] < 0:
            raise UserError("Chu kì liên kết chuẩn không được âm")
        elif vals['year_use'] < vals['year_manufacture']:
            raise UserError("Năm sử dụng phải lớn hơn năm sản xuất")
        result = super(Ptdmeasuringdevice, self).create(vals)
        return result



    @api.constrains('serial_number')
    def check_numval(self):
        for record in self:
            if record.is_serial == 'serial':
                # print("record.serial_number",record.serial_number)
                # print(type(record.serial_number))
                if (record.serial_number) == False :
                    raise UserError("Không được để trống mã sê-ri" )
                elif len(record.serial_number) > 6:
                    raise ValidationError("Phải nhỏ hơn 6 kí tự: %s" % record.serial_number)
                return True
            elif record.is_serial =='noserial':
                return True

    @api.model
    def create(self, vals):

        if type(vals['des']) is bool:
            result = super(Ptdmeasuringdevice, self).create(vals)
            return result
        elif (len(vals['des']) < 300):
            result = super(Ptdmeasuringdevice, self).create(vals)
            return result
        else:
            raise UserError("Mô tả không được quá 300 kí tự")

    def write(self, vals):
        # print(vals)
        if 'name' in vals:
            print(vals['name'], type(vals['name']))
            if vals['name'].isalnum()==False:
                raise UserError("Mã QLTS: chỉ gồm ký tự chữ hoặc số")
            else:
                if vals['name'] == ' ':
                    raise UserError("Trường: Mã QLTS trống ")




        if 'year_manufacture' in vals or 'year_use' in vals:
            date1 = self.year_manufacture
            date2 = str(self.year_use)
            if 'year_manufacture' in vals:
                date1 = int(vals['year_manufacture'])
                # print(date1)
            if 'year_use' in vals:
                date2 = vals['year_use']
            if int(date2[:4]) < int(date1):
                raise ValidationError("Năm sử dụng không hợpz lệ")

        if 'des' not in vals:
            result = super(Ptdmeasuringdevice, self).write(vals)
            return result
        else:
            if type(vals['des']) == bool:
                result = super(Ptdmeasuringdevice, self).write(vals)
                return result
            elif len(vals['des']) > 300:
                raise UserError("Mô tả không được quá 300 kí tự")
        result = super(Ptdmeasuringdevice, self).write(vals)
        return result

    @api.onchange('standard_link_cycle')
    def change_link_cycle(self):
        # print(self.standard_link_cycle)
        if self.standard_link_cycle < 0 :
            # print(self.standard_link_cycle)
            raise UserError(" Bạn đã nhập sai trường chu kì liên kế chuẩn")

    def unlink(self):
        result = super(Ptdmeasuringdevice, self).unlink()
        # print(result)

    @api.onchange('main_info_ids')
    def check_date(self):
        im_date = (len(self.main_info_ids))
        im_date_ids = []
        print(self.main_info_ids)
        if(len(im_date_ids)>= 0):
            pass
        for x in self.main_info_ids:
            print(x.implement_date)
            # if x.implement_date == False:
            #     print('ok')
            # else:
            # dữ liệu bị k bị False nếu field implement_date của ptd_maintenance_info ko để là required = True
            date_string=datetime.strptime(str(x.implement_date), "%Y-%m-%d").date()
            #print('date_string', date_string)
            im_date_ids.append(date_string)
        for i in range(0, len(im_date_ids) - 1):
            for j in range(i + 1, len(im_date_ids)):
                print('mảng', len(im_date_ids))
                # if(len(im_date_ids) == 1):
                #     rec.expiry_date = im_date_ids[i]
                if (im_date_ids[i] >= im_date_ids[j]):
                    print("XXXX")
                    im_date_ids.pop(len(im_date_ids) - 1)
                    raise UserError("Ngày bảo dưỡng sau phải lớn hơn ngày bảo dưỡng trước")
                else:
                    for rec in self:
                        # print('rec.maintain_cycle',rec.maintain_cycle)
                        # print('expiry_date', type(rec.expiry_date))
                        a = timedelta(days=rec.maintain_cycle * 4 * 7)
                        print('a',a)
                        rec.expiry_date = im_date_ids[j] + a
                        print(im_date_ids[j] + a)


    @api.onchange('expiry_date')
    def update_state(self):
        # print('ok')
        for rec in self:
            is_birthday = False
            is_birthday01 = False
            print(rec.maintain_cycle)
            if rec.expiry_date:
                today = datetime.today()
                today = today.date()
                # print('today',today)
                # print('ok', (rec.year_use - today))
                # print(type(rec.year_use))
                # print(type(today))
                if (rec.expiry_date - today) < timedelta(days=31):
                    print(rec.expiry_date - today) #ngày gần hết hạn
                    is_birthday = True
                    is_birthday01 = False
                    rec.quality_status ='occupied'
                if (rec.expiry_date - today) > timedelta(days=31):
                    is_birthday = False
                    is_birthday01 = False
                    rec.quality_status = "available"
                if (today > rec.expiry_date) : # ngày quá hạn
                    is_birthday = False
                    is_birthday01 = True
                    rec.quality_status = 'expiry_near'
            rec.is_birthday = is_birthday
            rec.is_birthday01 = is_birthday01

    def display_time(self):
        if not self.main_info_ids:
            return False
        else:
            return self.main_info_ids[len(self.main_info_ids) - 1]

    def display_kd_hc(self):
        if not self.can_link_info_ids:
            return False
        else:
            return self.can_link_info_ids[len(self.can_link_info_ids)-1]


    def display_thongtin(self):
        if not self.spe_info_ids:
            return False
        else:
            return self.spe_info_ids[len(self.spe_info_ids)-1]

    @api.constrains('quality_level')
    def check_quality(self):
        for record in self:
            # if record.quality_level == "1":
            #     print(record.quality_level)
            #     return True
            if record.quality_level != "1":
                if type(record.transfer_day) == bool:
                    raise UserError("Bắt buộc nhập ngày chuyển cấp")
                if record.transfer_reason == "":
                    print(record.transfer_reason)
                    raise UserError("Bắt buộc nhập nguyên nhân chuyển cấp")
                else:
                    return True

    @api.onchange('can_link_info_ids')
    def _onchange_can_link_info_ids(self):
        len_origin = len(self._origin.can_link_info_ids)
        if len_origin > 0:
            if len_origin < len(self.can_link_info_ids):
                if self.can_link_info_ids[len_origin].implement < self._origin.can_link_info_ids[len_origin - 1].implement:
                    raise UserError('Ngày KĐ/HC không hợp lệ')
                if self.can_link_info_ids[len_origin].val_date < self._origin.can_link_info_ids[
                    len_origin - 1].val_date:
                    raise UserError('Ngày KĐ/HC không hợp lệ')
            if len_origin == len(self.can_link_info_ids):
                if self.can_link_info_ids[0].implement < self._origin.can_link_info_ids[len_origin - 2].implement:
                    raise UserError('Ngày KĐ/HC không hợp lệ')
                if self.can_link_info_ids[0].val_date < self._origin.can_link_info_ids[len_origin - 2].val_date:
                    raise UserError('Ngày KĐ/HC không hợp lệ')
    # @api.onchange('year_use')
    # def update_state(self):
    #     today = datetime.today()
    #     print(today + timedelta(days=1))
    #     # date1 = datetime.strptime(str(today), "%Y-%m-%d").date()
    #     for rec in self:
    #         is_birthday = False
    #         if rec.year_use:
    #             if today == rec.year_use.day and today.month == rec.year:
    #                 is_birthday = True
    #         rec.is_birthday = is_birthday







    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Mã QLTS này đã tồn tại')
    ]




















