from odoo import _, models, fields, api
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
class PtdCanonicallinkinfo(models.Model):
    _name = "ptd.canonical.link.info"
    _description = "Canonical Link"

    implement = fields.Date(string="Ngày KĐ/HC *", required=True)
    val_date = fields.Date(string = "Ngày hiệu lực GCN", required=True)
    expiration_date = fields.Date(string = 'Ngày hết han GCN', required=True)
    result = fields.Selection(string = 'Kết quả',
                                     selection=[('pass', 'Đạt'),
                                                ('nopass', 'Không Đạt'),
                                                ],
                                     default = 'pass',
                                     tracking = True
                                     )
    name = fields.Selection(string = 'Loại liên kết chuẩn',
                                     selection=[('kiemdinh', 'Kiểm định'),
                                                ('hieuchinh', 'Hiệu chỉnh'),
                                                ('tinhtoan', 'Kiểm tra kỹ thuật đo lường')],
                                     default = 'kiemdinh',
                                     tracking = True
                                     )
    organization = fields.Char(string = 'Tổ chức' )
    reason_fail = fields.Char(string ='Lý do lỗi')
    active1 = fields.Boolean(string = "Active")
    number = fields.Integer(string='Số lượng giấy chứng nhận', required=True)
    certifi = fields.Binary(string="Giấy chứng nhận")
    canon_id = fields.Many2one(comodel_name='ptd.measuring.device',
                               string = 'Thông tin liên kết chuẩn *',
                               )
    test = fields.Many2one('ptd.measuring.device',string="Mã QLTS")
    @api.model
    def create(self,vals):

        if vals['name'] == False:
            raise UserError("Loại liên kết chuẩn không được để trống")
        else:
            result = super(PtdCanonicallinkinfo,self).create(vals)
            print(result)
        return result


    #     date1 = self.implement
    #     date2 = self.val_date
    #     date3 = self.expiration_date
    #     number_check = self.number
    #     if 'number' in vals:
    #         number_check =vals['number']
    #     if 'implement' in vals:
    #         date1 = vals['implement']
    #     if 'val_date' in vals:
    #         date2 = vals['val_date']
    #     if 'expiry_date' in vals:
    #         date3 = vals['expiry_date']
    #     if datetime.strptime(str(date1), "%Y-%m-%d").date() >= datetime.strptime(str(date2), "%Y-%m-%d").date():
    #         raise UserError("Ngày hiệu lực không hợp lệ")
    #     if datetime.strptime(str(date2), "%Y-%m-%d").date() >= datetime.strptime(str(date3), "%Y-%m-%d").date():
    #         raise UserError("Ngày hết hạn không hợp lệ")
    #


    #onchange chạy trước vì mình thay đổi number nó sẽ xử lý luôn
    # @api.onchange('number', 'name','implement','val_date','expiration_date')
    # def on_change_number_name(self):
    #     print("onchange_number")
    #     if self.number < 0:
    #         print(self.number)
    #         raise UserError("Số chứng chỉ không được để trống")
    #     if self.name == False:
    #         print("Không được để trống")
    #         raise UserError("Không được để trống")
    #     for rec in self:
    #         if self.implement > self.val_date and self.val_date > self.expiration_date:
    #             raise UserError("Loại liên kết chuẩn không được để trống")
    @api.constrains('implement','val_date','expiration_date','name')
    def _how_to_date (self):
        for rec in self:
            if rec.implement and rec.val_date and rec.expiration_date :
                print(rec.implement)
                if rec.implement > rec.val_date:
                    raise ValidationError("Ngày thực hiện không được lơn hơn ngày chứng nhận của GCN")
                if rec.val_date > rec.expiration_date:
                    raise ValidationError("Ngày bắt đầu giấu chứng nhận không được lớn hơn ngày hết hạn GCN")
                if rec.name == False:
                    raise ValidationError("Loại liên kết chuẩn không được để trống")











