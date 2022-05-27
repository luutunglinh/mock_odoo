# -*- coding: utf-8 -*-

import datetime

from odoo import models


class ReportXlsx2(models.AbstractModel):
    _name = 'report.mockproject.baocaochitietexcel2'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet('Báo Cáo Chi tiết')
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#fffbed', 'border': True})
        title = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 20, 'bg_color': 'white', 'border': True})
        merge_format = workbook.add_format({'bold': True, 'align': 'center', 'border': True})

        format1 = workbook.add_format({'font_size': 10, 'align': 'center', })
        count = 0
        row = 3
        col = 0
        sheet.set_column('A:B', 5)
        sheet.set_column('B:Y', 20)


        for obj in lines:
            # STT
            count = count + 1
            sheet.write(row, col, count, format1)

            # Tên trang bị đồng bộ phụ tùng
            sheet.write(row, col + 1, obj.name, format1)

            # Ký hiệu
            sheet.write(row, col + 2, obj.model, format1)

            # Số hiệu
            sheet.write(row, col + 3, obj.serial_number, format1)

            # Nhóm PTĐ
            sheet.write(row, col + 4, obj.device_group_id.name, format1)

            # Chủng loại PTĐ
            sheet.write(row, col + 5, obj.type_equip_id.name, format1)

            # Đơn vị tính
            sheet.write(row, col + 6, obj.unit_measure_id.name, format1)

            # Số lượng
            sheet.write(row, col + 7, obj.count, format1)

            # Nơi (hãng) SX
            sheet.write(row, col + 8, obj.country_id.name, format1)

            # Năm SX
            # sheet.write(row, col + 9, obj.manufacture_year, format1)
            sheet.write(row, col + 9, obj.year_manufacture, format1)

            # Năm SD
            sheet.write(row, col + 10, obj.year_use.strftime('%Y-%m-%d'), format1)

            # Đặc tính kĩ thuật/đo lường
            # sheet.write(row, col + 11, "Đặc tính", format1)

            # Cấp CL
            sheet.write(row, col + 12, obj.quality_level, format1)

            # Chu kì KĐHC
            sheet.write(row, col + 13, obj.maintain_cycle, format1)

            # Hiệu lực KĐHC
            implement1 = obj.can_link_info_ids.implement.strftime('%Y-%m-%d')
            sheet.write(row, col + 14, implement1)

            # Số GCN KĐHC
            sheet.write(row, col + 15, obj.can_link_info_ids.number, format1)

            # Đơn vị KĐHC
            sheet.write(row, col + 16, obj.can_link_info_ids.organization, format1)

            # Cấp quản lí (TĐ hay BQP)
            sheet.write(row, col + 17, "Cấp quản lý", format1)

            # Ghi chú
            sheet.write(row, col + 18, obj.des, format1)

            row += 1

        sheet.merge_range('A1:S2', 'BÁO CÁO SỔ QUẢN LÝ THIẾT BỊ ĐO LƯỜNG', title)

        sheet.write('A3', 'STT', merge_format)
        sheet.write('B3', 'Tên trang bị đồng bộ phụ tùng', merge_format)
        sheet.write('C3', 'Ký hiệu', merge_format)
        sheet.write('D3', 'Số hiệu', merge_format)
        sheet.write('E3', 'Nhóm PTĐ', merge_format)
        sheet.write('F3', 'Chủng loại PTĐ', merge_format)
        sheet.write('G3', 'Đơn vị tính', merge_format)
        sheet.write('H3', 'Số lượng', merge_format)
        sheet.write('I3', 'Nơi (hãng) SX', merge_format)
        sheet.write('J3', 'Năm SX', merge_format)
        sheet.write('K3', 'Năm SD', merge_format)
        sheet.write('L3', 'Đặc tính kĩ thuật/đo lường', merge_format)
        sheet.write('M3', 'Cấp CL', merge_format)
        sheet.write('N3', 'Chu kì KĐHC', merge_format)
        sheet.write('O3', 'Hiệu lực KĐHC', merge_format)
        sheet.write('P3', 'Số GCN KĐHC', merge_format)
        sheet.write('Q3', 'Đơn vị KĐHC', merge_format)
        sheet.write('R3', 'Cấp quản lí (TĐ hay BQP)', merge_format)
        sheet.write('S3', 'Ghi chú', merge_format)
