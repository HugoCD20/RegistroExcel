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
            info.append(i)
            for celda in sheet[i]:
                if celda.value==None:
                    info.append('VACIO')
                else:
                    info.append(celda.value)
            total.append(info)
            info=[]
    return total

def CambiarValores(arreglo,seleccion,indice):
    seleccion=int(seleccion)
    apellido1=arreglo[seleccion][1]
    apellido2=arreglo[seleccion][2]
    nombre1=arreglo[seleccion][3]
    nombre2=arreglo[seleccion][4]

    for i in arreglo:
         sheet["A"+str(i[0])]=apellido1
         sheet["B"+str(i[0])]=apellido2
         sheet["C"+str(i[0])]=nombre1
         sheet["D"+str(i[0])]=nombre2
         book.save('sample.xlsx')
         indice.append(i[0])

    return indice

def prueva(datos):
    for i in datos:
        if i[1]!="VACIO":
                inserta(i[1],i[2],i[3],i[4],i[5])

def insert_registros(datos):
    for i in datos:
        if i[1]!="VACIO":
            registro(i[1],i[2],i[3],i[4],i[6],i[7],i[8],i[9],i[11])
