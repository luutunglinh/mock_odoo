# -*- coding: utf-8 -*-

import datetime

from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.mockproject.baocaochitietexcel3'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet('Báo cáo tổng hợp PTĐ cấp BQP Excel')
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#fffbed', 'border': True})
        title = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 20, 'bg_color': 'white', 'border': True})
        merge_format = workbook.add_format({'bold': True, 'align': 'center', 'border': True})

        format1 = workbook.add_format({'font_size': 10, 'align': 'center', })
        count = 0
        row = 4
        col = 0
        sheet.set_column('A:Y', 40)

        for o in lines:
            # STT
            count = count + 1
            sheet.write(row, col, count, format1)

            # Tên phương tiện đo
            sheet.write(row, col + 1, o.name, format1)

            # Mã hàng hóa
            sheet.write(row, col + 2, o.asset_code, format1)

            sheet.write(row, col + 3, o.model, format1)

            sheet.write(row, col + 4, o.serial_number, format1)

            sheet.write(row, col + 5, o.country_id.name, format1)

            sheet.write(row, col + 6, o.year_manufacture, format1)

            sheet.write(row, col + 7, o.spe_info_ids.para, format1)

            sheet.write(row, col + 8, o.spe_info_ids.value, format1)

            sheet.write(row, col + 9, o.spe_info_ids.error, format1)

            sheet.write(row, col + 10, o.quality_level, format1)

            sheet.write(row, col + 11, o.direct_unit_manager_id.name, format1)

            sheet.write(row, col + 12, ', '.join(o.can_link_info_ids.mapped('organization')))

            sheet.write(row, col + 13, o.des, format1)

            row += 1

        sheet.merge_range('A1:O2', 'Báo cáo tổng hợp PTĐ cấp BQP Excel', title)

        # sheet.write(a,b,'c') : a_ row ; b_col, c_text(số thì k cần dấu ' ') (có thể tạo 1 cái)
        # sheet.merge_range(first_row, first_col, last_row, last_col, data [,merge_format]
        # sheet.set.column(first col, last_col, width [,cell_format])

        sheet.merge_range('A3:A4', 'STT', merge_format)
        sheet.merge_range('B3:B4', 'Số quản lý', merge_format)
        sheet.merge_range('C3:C4', 'Tên trang bị ĐL-TN', merge_format)
        sheet.merge_range('D3:D4', 'Ký hiệu', merge_format)
        sheet.merge_range('E3:E4', 'Số hiệu', merge_format)
        sheet.merge_range('F3:F4', 'Nước(hãng) SX', merge_format)
        sheet.merge_range('G3:G4', 'Năm SX', merge_format)
        sheet.merge_range('H3:J3', 'Đặc tính đo lường chủ yếu', merge_format)
        sheet.write('H4','Tham số', format1)
        sheet.write('I4','Giá trị', format1)
        sheet.write('J4','Sai số', format1)
        sheet.merge_range('K3:K4', 'Cấp CL', merge_format)
        sheet.merge_range('L3:L4', 'Đơn vị quản lý', merge_format)
        sheet.merge_range('M3:M4', 'Chu kỳ KĐ/HC', merge_format)
        sheet.merge_range('N3:N4', 'Nơi KĐ/HC', merge_format)
        sheet.merge_range('O3:O4', 'Ghi chú', merge_format)
