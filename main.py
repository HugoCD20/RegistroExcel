from functions import prueva,ConsultaT,insert_registros
from conexion import agregar_registros as registro

datos=ConsultaT()#recibimos los datos de la consulta
prueva(datos)
insert_registros(datos)
