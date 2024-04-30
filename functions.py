import openpyxl
from conexion import agregar_usuario as inserta
from conexion import agregar_registros as registro
book=openpyxl.load_workbook('sample.xlsx')
sheet=book.active
filas=sheet.max_row

def ConsultaT():
    info=[]
    total=[]
    for i in range(2,filas+1):
            for celda in sheet[i]:
                if celda.value==None:
                    info.append('VACIO')
                else:
                    info.append(celda.value)
            total.append(info)
            info=[]
    return total

def prueva(datos):
    for i in datos:
        if i[0]!="VACIO":
                inserta(i[0],i[1],i[2],i[3],i[4])

def insert_registros(datos):
    for i in datos:
        if i[0]!="VACIO":
            registro(i[0],i[1],i[2],i[3],i[5],i[6],i[7],i[8],i[10])
