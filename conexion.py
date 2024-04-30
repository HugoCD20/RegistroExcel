import sqlite3

conexion = sqlite3.connect("horasdb.db")
cursor= conexion.cursor()

def agregar_usuario(apellidop,apellidom,nombre1,nombre2,semestre):
    matricula=000000
    usuario=(
        apellidop,
        apellidom,
        nombre1,
        nombre2,
        semestre,
        matricula        
    )
    sql=f"SELECT * FROM Estudiantes where apellidop='{usuario[0]}' and apellidom='{usuario[1]}' and nombre1='{usuario[2]}' and nombres='{usuario[3]}'"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    if not resultado:
        sql2= f"INSERT INTO Estudiantes (apellidop,apellidom,nombre1,nombres,semestre,matricula) VALUES {usuario}"
        cursor.execute(sql2)

    conexion.commit()

def agregar_registros(apellidop,apellidom,nombre1,nombres,taller,documento,duracion,Hrs_extras,inf_recuperada):
    #falta modificar esta parte apellidos y nombres van a estar dividida
    sql=f"SELECT * FROM Estudiantes where apellidop='{apellidop}' and apellidom='{apellidom}' and nombre1='{nombre1}' and nombres='{nombres}'"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    if resultado:
            id=resultado[0][0]
            registro=(
                    id,taller,
                    documento,duracion,
                    Hrs_extras,inf_recuperada
                )
            sql2=f"INSERT INTO Registro (id_estudiante,Taller,Documento,Duracion,Hrs_extras,inf_recuperada) VALUES {registro}"
            cursor.execute(sql2)
            conexion.commit()
