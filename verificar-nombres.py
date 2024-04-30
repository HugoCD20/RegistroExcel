from functions import ConsultaT
def prueva(datos):
    correctos=[]
    for i in datos:
        if i[1]!="VACIO":
            correctos.append([i[0],i[1].upper(),i[2].upper(),i[3].upper(),i[4].upper(),i[5]])
    return correctos

def buscar(correctos):
    coincidencias=[]
    i=len(correctos)
    for x in range(i):
        for y in range(i):
            if correctos[x][0] != correctos[y][0]:
                if correctos[x][1]==correctos[y][1] or correctos[x][2]==correctos[y][2] or correctos[x][3]==correctos[y][3] or correctos[x][4]==correctos[y][4]:
                    coincidencias.append(correctos[y])
    print(coincidencias)


datos=ConsultaT()
correctos=prueva(datos)
buscar(correctos)