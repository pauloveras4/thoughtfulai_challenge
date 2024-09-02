from RPA.Excel.Application import Application
from RPA.Excel.Files import Files

class XLSXSerializer(object):
    
    def __init__(self, filename, sheet):
        self.filename = filename
        self.sheet = sheet
        
    excel_filesystem_lib = Files()
    
    def serialize_news_array_to_excel_file(self, results_array):
        # Prepare the environment
        self.excel_filesystem_lib.create_workbook(self.filename)
        self.excel_filesystem_lib.create_worksheet(self.sheet, content=None)
        self.excel_filesystem_lib.set_active_worksheet(self.sheet)

        # Add headers to the workbook
        self.excel_filesystem_lib.set_cell_value(row=1, column=1, value='Title')
        self.excel_filesystem_lib.set_cell_value(row=1, column=2, value='Date')
        self.excel_filesystem_lib.set_cell_value(row=1, column=3, value='Image Filename')
        self.excel_filesystem_lib.set_cell_value(row=1, column=4, value='Search Query Count')
        self.excel_filesystem_lib.set_cell_value(row=1, column=5, value='Contains Currency')
        
        # Iterate through array and insert values in cells
        for row_index, item in enumerate(results_array):
            for column_index, key in enumerate(item):
                self.excel_filesystem_lib.set_cell_value(row=row_index+2, column=column_index+1, value=item[key])
       
        # Autosize columns
        self.excel_filesystem_lib.auto_size_columns("A", width=80)
        self.excel_filesystem_lib.auto_size_columns("B", width=30)
        self.excel_filesystem_lib.auto_size_columns("C", width=80)
        self.excel_filesystem_lib.auto_size_columns("D", width=30)
        self.excel_filesystem_lib.auto_size_columns("E", width=20)
        
        # Style headers with bold and center content
        self.excel_filesystem_lib.set_styles("A1:E1", align_horizontal="center", align_vertical="center", bold=True, font_name="Calibri", size=12)
        
        # Save workbook
        self.excel_filesystem_lib.save_workbook(self.filename)
        return 0