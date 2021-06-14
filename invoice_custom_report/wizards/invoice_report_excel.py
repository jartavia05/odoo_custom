from odoo import models, fields, api 

class Report_Invoice_Excel(models.TransientModel):
    _name = 'invoice.report.excel.wizard'

    date_start = fields.Date(string='Fecha Inicio')
    date_end = fields.Date(string='Fecha Fin')

    print ("Hola Mundo")

    

class Generate_Report_excel(models.AbstractModel):
    _name = 'report.invoice_custom_report.invoice_report_excel'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet('Reporte Facturacion')
        title_format = workbook.add_format({'font_size': 18,'font_color': '#999999', 'bold':True})
        sheet.write(1,1, 'Reporte de Facturacion',title_format )
        #sheet.write(2,1, 'Reporte Generado por: '+ lines.company_name, title_format )
        
