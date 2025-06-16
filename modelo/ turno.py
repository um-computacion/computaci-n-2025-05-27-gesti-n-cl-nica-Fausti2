from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        if not isinstance(paciente, Paciente):
            raise ValueError("El paciente debe ser un objeto de la clase Paciente.")
        if not isinstance(medico, Medico):
            raise ValueError("El médico debe ser un objeto de la clase Medico.")
        if not isinstance(fecha_hora, datetime):
            raise ValueError("La fecha y hora deben ser un objeto datetime.")
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("La especialidad debe ser una cadena no vacía.")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def __str__(self) -> str:
        return (
            f"Turno(\n"
            f"  {self.__paciente},\n"
            f"  {self.__medico},\n"
            f"  {self.__fecha_hora.strftime('%Y-%m-%d %H:%M')},\n"
            f"  {self.__especialidad}\n"
            f")"
        ) 