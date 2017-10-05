import xlrd




wb = xlrd.open_workbook("Datos.xlsx")
historico = wb.sheet_by_name("Histórico de basura")

print(historico.cell(3, 3).value)
print(historico.cell(2, 3).value)

# num_cols = historico.ncols   # Number of columns
# for row_idx in range(0, historico.nrows):    # Iterate through rows
#     print ('-'*40)
#     print ('Row: %s' % row_idx)   # Print row number
#     for col_idx in range(0, num_cols):  # Iterate through columns
#         cell_obj = historico.cell(row_idx, col_idx)  # Get cell object by row, col
#         print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
