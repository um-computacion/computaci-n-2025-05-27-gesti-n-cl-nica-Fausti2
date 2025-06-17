from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        if not isinstance(paciente, Paciente):
            raise TypeError("El paciente debe ser una instancia de la clase Paciente.")
        if not isinstance(medico, Medico):
            raise TypeError("El médico debe ser una instancia de la clase Medico.")
        if not isinstance(fecha_hora, datetime):
            raise TypeError("La fecha y hora debe ser un objeto datetime.")
        if not isinstance(especialidad, str) or not especialidad:
            raise ValueError("La especialidad debe ser una cadena válida.")

        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad

    def obtener_medico(self):
        return self.__medico

    def obtener_fecha_hora(self):
        return self.__fecha_hora

    def __str__(self):
        return (f"Turno(\n  {self.__paciente},\n  {self.__medico},\n"
                f"  {self.__fecha_hora},\n  {self.__especialidad}\n)") 