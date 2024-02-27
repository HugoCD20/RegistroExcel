import openpyxl
from model import Estudiante
book=openpyxl.load_workbook('sample.xlsx')
sheet=book.active
filas=sheet.max_row

def Consulta(x,z):
    info=[]
    for i in range(1,filas+1):
        A="A"+str(i)
        B="B"+str(i)
        a=sheet[A]
        b=sheet[B]
        if x==a.value and z==b.value:
            info.append(i)
            for celda in sheet[i]:
                if celda.value==None:
                    info.append('VACIO')
                else:
                    info.append(celda.value)
    return info

def CrearObjeto(lista):
    estudiante=Estudiante(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9],lista[10])
    return estudiante

def insertar(apellidop):
    f=int(filas)+1
    fila='A'+str(f)
    print(fila)
    sheet[fila]=apellidop
    book.save("sample.xlsx")