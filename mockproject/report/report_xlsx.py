# -*- coding: utf-8 -*-

import datetime

from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.mockproject.baocaochitietexcel'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet('Báo cáo chi tiết phương tiện đo lường trong tập đoàn Excel')
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#fffbed', 'border': True})
        title = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 20, 'bg_color': 'white', 'border': True})
        merge_format = workbook.add_format({'bold': True, 'align': 'center', 'border': True})

        format1 = workbook.add_format({'font_size': 10, 'align': 'center', })
        count = 0
        row = 5
        col = 0
        sheet.set_column('A:Y', 20)

        for obj in lines:
            # STT
            count = count + 1
            sheet.write(row, col, count, format1)

            # Tên phương tiện đo
            sheet.write(row, col + 1, obj.asset_code, format1)

            # Mã hàng hóa
            sheet.write(row, col + 2, obj.name, format1)

            # Part number bỏ
            sheet.write(row, col + 3, "x", format1)

            # Serial
            sheet.write(row, col + 4, obj.serial_number, format1)

            # Tình trạng
            sheet.write(row, col + 5, obj.quality_status, format1)

            # Thời gian đưa vào sử dụng
            year_use = obj.year_use.strftime('%Y-%m-%d')
            sheet.write(row, col + 6, year_use, format1)

            # Mã nhân viên
            # sheet.write(row, col + 7, obj.employee_id, format1)

            # Họ và tên
            sheet.write(row, col + 8, obj.direct_manager_id.name, format1)

            # Đơn vị quản lý
            sheet.write(row, col + 9, obj.direct_unit_manager_id.name, format1)

            # Cấp 1
            if obj.quality_level == "1":
                # print(type(obj.quality_level))
                sheet.write(row, col + 10, "x", format1)

            # Cấp 2
            if obj.quality_level == "2":
                sheet.write(row, col + 11, "x", format1)
            # Cấp 3
            if obj.quality_level == "3":
                sheet.write(row, col + 12, "x", format1)
            # Cấp 4
            if obj.quality_level == "4":
                sheet.write(row, col + 13, "x", format1)

            # Chu kỳ kiểm định hiệu chuẩn
            sheet.write(row, col + 14, obj.standard_link_cycle, format1)

            # Thời gian thực hiện KDHC gần nhất
            # sheet.write(row, col + 15, ', '.join(obj.canonical_ids.mapped('implement')))
            implement1 = obj.can_link_info_ids.implement.strftime('%Y-%m-%d')
            sheet.write(row, col + 15, implement1)
            print("imp",obj.can_link_info_ids.implement)


            # Đối tác thực hiện KDHC
            sheet.write(row, col + 16, ', '.join(obj.can_link_info_ids.mapped('organization')))

            # Ghi rõ KD hay HC
            # x1 = ','.join(obj.can_link_info_ids.mapped('stand_link_type'))
            # sheet.write(row, col + 17, x1, format1)

            # Đạt
            x2 = ','.join(obj.can_link_info_ids.mapped('result'))
            if x2 == "pass":
                sheet.write(row, col + 18, "x", format1)
            # Không đạt
            if x2 == "nopass":
                sheet.write(row, col + 19, "x", format1)

            # Nguyên nhân không đạt
            sheet.write(row, col + 20, ', '.join(obj.can_link_info_ids.mapped('reason_fail')), format1)

            # Công tác bảo trì bảo dưỡng/ Thời gian thực hiện gần nhất
            implement2 = obj.can_link_info_ids.implement.strftime('%Y-%m-%d')
            sheet.write(row, col + 21, implement2)

            # Thười gian hỏng gần nhất
            sheet.write(row, col + 22, obj.dmg_time, format1)

            # Nguyên nhân hỏng
            sheet.write(row, col + 23, obj.dmg_reason, format1)

            # Ghi chú
            sheet.write(row, col + 24, obj.des, format1)

            row += 1

        sheet.merge_range('A1:Y1', 'BÁO CÁO CHI TIẾT VỀ PHƯƠNG TIỆN ĐO LƯỜNG TRONG TOÀN TẬP ĐOÀN', title)

        # sheet.write(a,b,'c') : a_ row ; b_col, c_text(số thì k cần dấu ' ') (có thể tạo 1 cái)
        # sheet.merge_range(first_row, first_col, last_row, last_col, data [,merge_format]
        # sheet.set.column(first col, last_col, width [,cell_format])

        sheet.merge_range('A3:A5', 'STT', merge_format)
        sheet.merge_range('B3:B5', 'Tên phương tiện đo', merge_format)
        sheet.merge_range('C3:C5', 'Mã hàng hóa', merge_format)
        sheet.merge_range('D3:D5', 'Part Number', merge_format)
        sheet.merge_range('E3:E5', 'Serial', merge_format)
        sheet.merge_range('F3:F5', 'Tình trạng', merge_format)
        sheet.merge_range('G3:G5', 'Thời gian đưa vào sử dụng', merge_format)

        sheet.merge_range('H3:J3', 'Thông tin quản lý', merge_format)
        sheet.merge_range('K3:N3', 'Phân cấp chất lượng', merge_format)
        sheet.merge_range('O3:U3', 'Công tác kiểm định / Hiệu chuẩn (KĐHC)', merge_format)

        sheet.write('V3', 'Công tác bảo trì, bảo dưỡng', merge_format)
        sheet.merge_range('W3:X3', 'Công tác bảo hành sửa chữa', merge_format)
        sheet.merge_range('Y3:Y5', 'Ghi chú', merge_format)

        # Trong thông tin quản lý
        sheet.merge_range('H4:H5', 'Mã nhân viên', merge_format)
        sheet.merge_range('I4:I5', 'Họ và tên', merge_format)
        sheet.merge_range('J4:J5', 'Đơn vị quản lý', merge_format)

        # Trong phân cấp chất lượng
        sheet.merge_range('K4:K5', 'Cấp 1', merge_format)
        sheet.merge_range('L4:L5', 'Cấp 2', merge_format)
        sheet.merge_range('M4:M5', 'Cấp 3', merge_format)
        sheet.merge_range('N4:N5', 'Cấp 4', merge_format)

        # Trong công tác kiểm định / hiệu chuẩn (KĐHC)
        sheet.merge_range('O4:O5', 'Chu kỳ kiểm định, hiệu chuẩn', merge_format)
        sheet.merge_range('P4:P5', 'Thời gian thực hiện KĐ/HC', merge_format)
        sheet.merge_range('Q4:Q5', 'Đối tác thực hiện KĐHC', merge_format)
        sheet.merge_range('R4:R5', 'Ghi rõ KĐ hay HC', merge_format)
        sheet.merge_range('S4:U4', 'Kết quả kiểm định / hiệu chuẩn', merge_format)
        sheet.write('S5', 'Đạt', merge_format)
        sheet.write('T5', 'Không đạt', merge_format)
        sheet.write('U5', 'Nguyên nhân không đạt', merge_format)

        # Trong công tác bảo trì bảo dưỡng
        sheet.merge_range('V4:V5', 'Thời gian thực hiện gần nhất', merge_format)

        # Trong công tác bảo hành sửa chữa
        sheet.merge_range('W4:W5', 'Thời gian hỏng gần nhất', merge_format)
        sheet.merge_range('X4:X5', 'Nguyên nhân hỏng', merge_format)
