import xlsxwriter


class ExportExcelMixin:
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def get_c(self, col):

        result = []
        while col:
            col, rem = divmod(col-1, 26)
            result[:0] = self.LETTERS[rem]
        return ''.join(result)

    def __init__(self, file_path):
        self.workbook = xlsxwriter.Workbook(file_path)
        self.set_default_style()

    def set_default_style(self):
        self.style_dict = {
            'title': self.workbook.add_format({
                'bold': True,
                'font_size': 14,
                'align': 'center',
                'valign': 'vcenter'
            }),
            'header': self.workbook.add_format({
                'bg_color': '#59677e',
                'color': 'white',
                'align': 'left',
                'valign': 'vcenter',
                'border': 1,
                'bold': True,
                'font_size': 11,
            }),
            'normal_date': self.workbook.add_format({
                'color': 'black',
                'align': 'right',
                'valign': 'vcenter',
                'border': 1,
                'num_format': 'dd/mm/yy'
            }),
            'normal': self.workbook.add_format({
                'color': 'black',
                'align': 'right',
                'valign': 'vcenter',
                'border': 1,
            })
        }


class ExportarImpresiones(ExportExcelMixin):

    def generar_xlsx(self, data):
        worksheet_s_name = "Impresión de credenciales"
        worksheet_s = self.workbook.add_worksheet(worksheet_s_name)

        worksheet_s.merge_range('A2:F2', "IMPRESIÓN DE CREDENCIALES", self.style_dict["title"])
        row = 3

        # cabeceras izquerda
        worksheet_s.set_column(0, 9, 18)  # colum_ini, colun_fin, tamaño
        worksheet_s.set_column(10, 10, 13)  # colum_ini, colun_fin, tamaño
        worksheet_s.set_column(11, 11, 10)  # colum_ini, colun_fin, tamaño
        worksheet_s.set_column(12, 12, 36)  # colum_ini, colun_fin, tamaño
        worksheet_s.set_row(row, 25)
        worksheet_s.write_row(row, 0, ["NOMBRE", "APELLIDO", "FECHA NACIMIENTO", "LUGAR NACIMIENTO",
                                       "PROVINCIA", "N° DOC", "DOMICILIO", "FECHA INSCRIPCIÓN",
                                       "FECHA RENOVACIÓN", "FECHA IMPRESIÓN", "CLUB", "DIVISIÓN", "OBSERVACIONES"],
                               self.style_dict["header"])
        row += 1
        for line in data:
            worksheet_s.write(row, 0, line.nombre, self.style_dict["normal"])
            worksheet_s.write(row, 1, line.apellido, self.style_dict["normal"])
            worksheet_s.write(row, 2, line.fecha_nac, self.style_dict["normal_date"])
            worksheet_s.write(row, 3, line.lugar_nac, self.style_dict["normal"])
            worksheet_s.write(row, 4, line.provincia, self.style_dict["normal"])
            worksheet_s.write(row, 5, line.dni, self.style_dict["normal"])
            worksheet_s.write(row, 6, line.domicilio, self.style_dict["normal"])
            worksheet_s.write(row, 7, line.fecha_inscripcion, self.style_dict["normal_date"])
            worksheet_s.write(row, 8, line.fecha_renovacion, self.style_dict["normal_date"])
            worksheet_s.write(row, 9, line.fecha_impresion, self.style_dict["normal_date"])
            worksheet_s.write(row, 10, line.club.nombre, self.style_dict["normal"])
            worksheet_s.write(row, 11, line.division, self.style_dict["normal"])
            worksheet_s.write(row, 12, line.observaciones, self.style_dict["normal"])
            row += 1
        self.workbook.close()
        return True
