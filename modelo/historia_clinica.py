from modelo.paciente import Paciente
from modelo.turno import Turno
from modelo.receta import Receta

class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        if not isinstance(paciente, Paciente):
            raise TypeError("Debe pasar un objeto Paciente.")
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

    def agregar_turno(self, turno: Turno):
        if not isinstance(turno, Turno):
            raise TypeError("Debe agregar un objeto de tipo Turno.")
        self.__turnos.append(turno)

    def agregar_receta(self, receta: Receta):
        if not isinstance(receta, Receta):
            raise TypeError("Debe agregar un objeto de tipo Receta.")
        self.__recetas.append(receta)

    def obtener_turnos(self):
        return list(self.__turnos)  # copia para no modificar original

    def obtener_recetas(self):
        return list(self.__recetas)

    def __str__(self):
        turnos_str = "\n  ".join(str(t) for t in self.__turnos)
        recetas_str = "\n  ".join(str(r) for r in self.__recetas)
        return (f"HistoriaClinica(\n  {self.__paciente},\n  Turnos:\n  {turnos_str}\n  Recetas:\n  {recetas_str}\n)") 