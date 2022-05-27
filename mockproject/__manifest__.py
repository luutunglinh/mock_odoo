# -*- coding: utf-8 -*-
{
    'name': 'Phuong tien do',
    'summary': """
            Measuring Device Management Viettel Corporation
        """,
    'description': """
        TASYS
    """,
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'wizard/create_appointment.xml',
        'wizard/create_update_infor.xml',
        'wizard/create_report_wizard.xml',
        'views/ptd_type_equip.xml',
        'views/ptd_device_group.xml',
        'views/ptd_position_manager.xml',
        'views/ptd_unit_measure_manager.xml',
        'views/ptd_direct_unit_manager.xml',
        'views/ptd_system.xml',
        'views/ptd_measuring_device.xml',
        'views/ptd_manufactures.xml',
        'views/ptd_device_category_manager.xml',
        'views/ptd_lab.xml',
        'views/ptd_broken_equip.xml',
        'views/ptd_menu.xml',
        'views/ptd_automove.xml',
        'views/ptd_canonical_link_info.xml',
        'views/ptd_maintenance_info.xml',
        'views/ptd_spec_info.xml',
        'report/ptd_paper.xml',
        'views/template.xml',
    ],
    'qweb': [

    ],
    'version': '0.1',
    'author': 'TASYS',
    'category': 'Viettel Corporation',
    'license': 'LGPL-3',
    'sequence': 1,
    'depends': ['base','mail','report_xlsx'],
    'installable': True,
    'application': True,

    'auto_install': False
}