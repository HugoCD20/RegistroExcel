class Estudiante:
    def __init__(self,fila,apellidop,apellidom,nombre1,nombre2,semestre,taller_curso,tipo_documento,duracion,hras_extras,lugar):
        self.fila=fila
        self.apellidop=apellidop
        self.apellidom=apellidom
        self.nombre1=nombre1
        self.nombre2=nombre2
        self.semestre=semestre
        self.taller_curso=taller_curso
        self.tipo_documento=tipo_documento
        self.duracion=duracion
        self.hras_extras=hras_extras
        self.lugar=lugar
    
    def Probar(self):
        return f"nombre: {self.nombre1}"