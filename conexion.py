import sqlite3

conexion = sqlite3.connect("horasdb.db")
cursor= conexion.cursor()

def agregar_usuario(apellidos,nombres,semestre):
    usuario=(
        apellidos,
        nombres,
        semestre
    )
    sql=f"SELECT * FROM Estudiantes where Apellidos='{usuario[0]}' and Nombres='{usuario[1]}'"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    if not resultado:
        sql2= f"INSERT INTO Estudiantes (Apellidos,Nombres,Semestre) VALUES {usuario}"
        cursor.execute(sql2)

    conexion.commit()

def agregar_registros(apellidos,nombres,taller,documento,duracion,Hrs_extras,inf_recuperada):
    
    sql=f"SELECT * FROM Estudiantes where Apellidos='{apellidos}' and Nombres='{nombres}'"
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
