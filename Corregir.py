from functions import ConsultaT,CambiarValores
def Correccion(datos):
    correctos=[]
    for i in datos:
        if i[1]!="VACIO":
            correctos.append([i[0],i[1],i[2],i[3],i[4],i[5]])
    return correctos

def Seleccionar(coincidencias,indice):
    contador=True
    while contador:
        x=len(coincidencias)
        for i in range(x):
            print(f"coloca: {i} {coincidencias[i][1]} {coincidencias[i][2]} {coincidencias[i][3]} {coincidencias[i][4]}")

        decision=input("coloca: x para continuar\n-> ")
        if decision!="" and decision != "x":
            coincidencias.pop(int(decision))
        else:
            print("selecciona el nombre correcto: ")
            for i in range(x):
                print(f"coloca: {i} {coincidencias[i][1]} {coincidencias[i][2]} {coincidencias[i][3]} {coincidencias[i][4]}")
            seleccion=input("-> ")
            CambiarValores(coincidencias,seleccion,indice)
            contador=False
            


def buscar(correctos):
    coincidencias=[]
    indice=[]
    i=len(correctos)
    for x in range(i):
        cont=0
        if len(indice)==0:
            for y in range(i):
                if correctos[x][0] != correctos[y][0]:
                    if correctos[x][1].upper()==correctos[y][1].upper() or correctos[x][2].upper()==correctos[y][2].upper() or correctos[x][3].upper()==correctos[y][3].upper() or correctos[x][4].upper()==correctos[y][4].upper():
                        if correctos[x][1].upper()==correctos[y][1].upper() and correctos[x][2].upper()==correctos[y][2].upper() and correctos[x][3].upper()==correctos[y][3].upper() and correctos[x][4].upper()==correctos[y][4].upper():
                            cont+=1
                        coincidencias.append(correctos[y])
        else:
            validacion=True
            for j in indice:
                if int(x)==int(j):
                    validacion=False
            if validacion:
                 for y in range(i):
                    if correctos[x][0] != correctos[y][0]:
                        if correctos[x][1].upper()==correctos[y][1].upper() or correctos[x][2].upper()==correctos[y][2].upper() or correctos[x][3].upper()==correctos[y][3].upper() or correctos[x][4].upper()==correctos[y][4].upper():
                            if correctos[x][1].upper()==correctos[y][1].upper() and correctos[x][2].upper()==correctos[y][2].upper() and correctos[x][3].upper()==correctos[y][3].upper() and correctos[x][4].upper()==correctos[y][4].upper():
                                cont+=1
                            coincidencias.append(correctos[y])
                    
        if coincidencias and cont!=len(coincidencias):
            coincidencias.append(correctos[x])        
            Seleccionar(coincidencias,indice)
            coincidencias=[]
        else:
            coincidencias=[]


def ejecucion():
    datos=ConsultaT()
    correctos=Correccion(datos)
    buscar(correctos)