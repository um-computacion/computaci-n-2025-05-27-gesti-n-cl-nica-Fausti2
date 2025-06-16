from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        if not isinstance(paciente, Paciente):
            raise ValueError("Paciente inválido.")
        if not isinstance(medico, Medico):
            raise ValueError("Médico inválido.")
        if not medicamentos or not all(isinstance(m, str) for m in medicamentos):
            raise ValueError("Lista de medicamentos inválida.")

        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self):
        return (
            f"Receta(\n"
            f"  {self.__paciente},\n"
            f"  {self.__medico},\n"
            f"  {self.__medicamentos},\n"
            f"  {self.__fecha.strftime('%Y-%m-%d %H:%M')}\n"
            f")"
        ) 