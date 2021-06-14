# -*- coding: utf-8 -*-

{
    "name": "Reporte Facturas para Odoo 12",
    "category": "Reporting",
    "author": "Venture Technology - @jartavia05",
    "summary": "Reporte de Facturacion",
    "version": "1.0",
    "description": """
Reporte Personalizado de Facturas para Odoo 12
        """,
    "depends": [
        "sale_management",
        "cr_electronic_invoice",
        "report_xlsx",
        ],
    "data": [
        'wizards/invoice_report_excel.xml',
    ],
    "installable": True,
}
