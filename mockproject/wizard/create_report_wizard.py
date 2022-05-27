from odoo import models, fields, api
from odoo.exceptions import UserError

class OpenAcademyPDFReport(models.TransientModel):
    _name = 'create.pdf.report'
    _description = "create pdf report"


    type = fields.Selection(
        string='Loại báo cáo',
        selection=[('1', 'Báo cáo chi tiết'),
                   ('2', 'Sổ quản lí thiết bị đo lường'),
                   ('3', 'Báo cáo tổng hợp PTĐ cấp BQP'),
                   ('4', 'Báo cáo PTĐ có thông tin sai lệch')],
        tracking=True
    )
    record_id = fields.Many2many('ptd.measuring.device', string="Chọn thiết bị")

    def print_report(self):
        if not self.record_id:
            raise UserError('Chưa chọn thiết bị cần in')
        if not self.type:
            raise UserError('Chọn loại báo cáo muốn in')
        if self.type == '1':
            return self.env.ref('mockproject.print_report1').report_action(self.record_id)
        if self.type == '2':
            return self.env.ref('mockproject.print_report2').report_action(self.record_id)
        if self.type == '3':
            return self.env.ref('mockproject.print_report3').report_action(self.record_id)
        if self.type == '4':
            return self.env.ref('mockproject.print_report4').report_action(self.record_id)
        # return self.env.ref('Mock_odoo.account_test1_id').report_action(self)

    def print_report_excel(self):
        if not self.record_id:
            raise UserError('Chưa chọn thiết bị cần in')
        if not self.type:
            raise UserError('Chọn loại báo cáo muốn in')
        if self.type == '1':
            return self.env.ref('mockproject.print_report_ptd_xls').report_action(self.record_id)
        if self.type == '2':
            return self.env.ref('mockproject.print_report_ptd_xls2').report_action(self.record_id)
        if self.type == '3':
            return self.env.ref('mockproject.pprint_report_ptd_xls3').report_action(self.record_id)
        if self.type == '4':
            return self.env.ref('mockproject.print_reportprint_report_ptd_xls4').report_action(self.record_id)

