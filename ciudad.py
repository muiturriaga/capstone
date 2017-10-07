import xlrd



wb = xlrd.open_workbook("Datos.xlsx")
ciudad = wb.sheet_by_name("Ciudad")

print("filas: {}, columas: {}".format(ciudad.nrows, ciudad.ncols))

max_basura = {}

for row_idx in range(3, ciudad.nrows):    # Iterate through rows
    numero_calle = ciudad.cell(row_idx, 1).value
    x1 = ciudad.cell(row_idx, 2).value
    y1 = ciudad.cell(row_idx, 3).value
    x2 = ciudad.cell(row_idx, 4).value
    y2 = ciudad.cell(row_idx, 5).value
    maxb = ciudad.cell(row_idx, 6).value
    max_basura[((x1, y1),(x2, y2))] = maxb
    max_basura[((x2, y2),(x1, y1))] = maxb

##################################################################################################################################
#ciudad[numero_calle] = {'arista1':((x1, y1), (x2, y2)), 'arista2':((x2, y2), (x1, y1)), 'basura_actual': 0, 'basura_max': maxb}#
##################################################################################################################################

# num_cols = historico.ncols   # Number of columns
# for row_idx in range(0, historico.nrows):    # Iterate through rows
#     print ('-'*40)
#     print ('Row: %s' % row_idx)   # Print row number
#     for col_idx in range(0, num_cols):  # Iterate through columns
#         cell_obj = historico.cell(row_idx, col_idx)  # Get cell object by row, col
#         print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
