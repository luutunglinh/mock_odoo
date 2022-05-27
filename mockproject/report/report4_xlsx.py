# -*- coding: utf-8 -*-

import datetime

from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.mockproject.baocaochitietexcel4'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet('Báo cáo PTĐ có thông tin sai lệch Excel')
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#fffbed', 'border': True})
        title = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 20, 'bg_color': 'white', 'border': True})
        merge_format = workbook.add_format({'bold': True, 'align': 'center', 'border': True})

        format1 = workbook.add_format({'font_size': 10, 'align': 'center', })
        count = 0
        row = 4
        col = 0
        sheet.set_column('A:Y', 20)

        for o in lines:
            # STT
            count = count + 1
            sheet.write(row, col, count, format1)

            # Tên phương tiện đo
            sheet.write(row, col + 1, o.asset_code, format1)

            # Mã hàng hóa
            sheet.write(row, col + 2, o.name, format1)

            sheet.write(row, col + 6, o.des, format1)
            row += 1

        sheet.merge_range('A1:G2', 'Báo cáo PTĐ có thông tin sai lệch Excel', title)

        # sheet.write(a,b,'c') : a_ row ; b_col, c_text(số thì k cần dấu ' ') (có thể tạo 1 cái)
        # sheet.merge_range(first_row, first_col, last_row, last_col, data [,merge_format]
        # sheet.set.column(first col, last_col, width [,cell_format])

        sheet.merge_range('A3:A4', 'STT', merge_format)
        sheet.merge_range('B3:B4', 'Tên thiết bị', merge_format)
        sheet.merge_range('C3:C4', 'Mã thiết bị', merge_format)
        sheet.merge_range('D3:F3', 'Thông tin sai lệch', merge_format)
        sheet.write('D4', 'Trường dữ liệu', merge_format)
        sheet.write('E4', 'Thông tin cũ ', merge_format)
        sheet.write('F4', 'Thông tin mới', merge_format)
        sheet.merge_range('G3:G4', 'Ghi chú', merge_format)
