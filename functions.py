import openpyxl
from model import Estudiante
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
            if i[3]!="VACIO":
                apellido=str(i[0]+" "+i[1])
                nombres=str(i[2]+" "+i[3])
                inserta(apellido,nombres,i[4])
            else:
                apellido=str(i[0]+" "+i[1])
                inserta(apellido,i[2],i[4])

def insert_registros(datos):
    for i in datos:
        if i[0]!="VACIO":
            if i[3]!="VACIO":
                apellido=str(i[0]+" "+i[1])
                nombres=str(i[2]+" "+i[3])
                registro(apellido,nombres,i[5],i[6],i[7],i[8],i[10])
            else:
                apellido=str(i[0]+" "+i[1])
                registro(apellido,i[2],i[5],i[6],i[7],i[8],i[10])
