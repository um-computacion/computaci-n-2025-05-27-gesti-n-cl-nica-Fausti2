from modelo.especialidad import Especialidad

class Medico:
    def __init__(self, nombre, matricula, especialidades=None):
        if not nombre or not matricula:
            raise ValueError("El nombre y la matrícula del médico son obligatorios.")
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = especialidades if especialidades else []

    def agregar_especialidad(self, especialidad):
        if not isinstance(especialidad, Especialidad):
            raise TypeError("Debe agregarse un objeto de tipo Especialidad.")
        if especialidad.obtener_especialidad() in [e.obtener_especialidad() for e in self.__especialidades]:
            raise ValueError("Especialidad ya registrada para este médico.")
        self.__especialidades.append(especialidad)

    def obtener_matricula(self):
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia):
        dia = dia.lower()
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
        return None

    def __str__(self):
        especialidades_str = ", ".join(str(e) for e in self.__especialidades)
        return f"{self.__nombre}, {self.__matricula}, [{especialidades_str}]" g