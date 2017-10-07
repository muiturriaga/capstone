import xlrd


wb = xlrd.open_workbook("Datos.xlsx")
historico = wb.sheet_by_name("Historico_basura")
ciudad = wb.sheet_by_name("Ciudad")

basura_calles = {}
w_ij = {}
count = 1

## FORMA 2
for numero_calle in range(1,6111):
	basura_calles["Calle {}".format(numero_calle)] = {}

for row_idx in range(2, historico.nrows):    # Iterate through rows
    dia = historico.cell(row_idx, 1).value
    numero_calle = historico.cell(row_idx, 2).value
    basura = historico.cell(row_idx, 3).value
    basura_calles[numero_calle].update({"dia{}".format(dia).rstrip(".0"): basura})


## FORMA 1
for row_idx in range(3, ciudad.nrows):    # Iterate through rows
    numero_calle = ciudad.cell(row_idx, 1).value
    x1 = ciudad.cell(row_idx, 2).value
    y1 = ciudad.cell(row_idx, 3).value
    x2 = ciudad.cell(row_idx, 4).value
    y2 = ciudad.cell(row_idx, 5).value
    w_ij[((x1, y1),(x2, y2))] = basura_calles["Calle {}".format(count).rstrip(".0")]
    count += 1




#ejemplos
print(basura_calles["Calle 258"].items())
print(w_ij[((7,5),(8,5))].items())



#    print ('Row: %s' % row_idx)   # Print row number
#    for col_idx in range(0, num_cols):  # Iterate through columns
#        cell_obj = ciudad.cell(row_idx, col_idx)  # Get cell object by row, col
#        print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
#for item in max_basura.items():
#	print(item)             #Estan todas las calles
