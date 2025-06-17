from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        if not isinstance(paciente, Paciente):
            raise TypeError("El paciente debe ser una instancia de Paciente.")
        if not isinstance(medico, Medico):
            raise TypeError("El médico debe ser una instancia de Medico.")
        if not medicamentos or not all(isinstance(m, str) and m.strip() for m in medicamentos):
            raise ValueError("Debe proporcionar al menos un medicamento válido.")

        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self):
        medicamentos_str = ", ".join(self.__medicamentos)
        return (f"Receta(\n  {self.__paciente},\n  {self.__medico},\n"
                f"  [{medicamentos_str}],\n  {self.__fecha.strftime('%Y-%m-%d %H:%M:%S')}\n)") 