from functions import ConsultaT,CambiarValores
def Correccion(datos):
    correctos=[]
    for i in datos:
        if i[1]!="VACIO":
            correctos.append([i[0],i[1],i[2],i[3],i[4],i[5]])
    return correctos

def Seleccionar(coincidencias):
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
            CambiarValores(coincidencias,seleccion)
            contador=False
            


def buscar(correctos):#hacer que los registros que conciden completamente no se agreguen al arreglo
    coincidencias=[]
    i=len(correctos)
    for x in range(i):
        for y in range(i):
            cont=0#aun esta el errror que se repite el campo para seleccionar el correcto
            if correctos[x][0] != correctos[y][0]:
                if correctos[x][1].upper()==correctos[y][1].upper():cont+=1
                if correctos[x][2].upper()==correctos[y][2].upper():cont+=1
                if correctos[x][3].upper()==correctos[y][3].upper():cont+=1
                if correctos[x][4].upper()==correctos[y][4].upper():cont+=1

                if cont>0 and cont<4:
                    coincidencias.append(correctos[y])#el error puede ser porque no actualizo la lista en donde estan listados los estudiantes
       
                    
        if coincidencias:
            coincidencias.append(correctos[x])        
            Seleccionar(coincidencias)
            coincidencias=[]
            datos=ConsultaT()
            correctos=Correccion(datos)


def ejecucion():
    datos=ConsultaT()
    correctos=Correccion(datos)
    buscar(correctos)