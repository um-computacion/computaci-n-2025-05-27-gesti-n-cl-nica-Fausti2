from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.historia_clinica import HistoriaClinica
from datetime import datetime

class PacienteNoEncontradoException(Exception): pass
class MedicoNoDisponibleException(Exception): pass
class TurnoOcupadoException(Exception): pass
class RecetaInvalidaException(Exception): pass

class Clinica:
    def __init__(self):
        self.__pacientes = {}  # dni -> Paciente
        self.__medicos = {}    # matricula -> Medico
        self.__turnos = []
        self.__historias_clinicas = {}  # dni -> HistoriaClinica

    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise ValueError("Paciente ya registrado.")
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise ValueError("Médico ya registrado.")
        self.__medicos[matricula] = medico

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException("Paciente no encontrado.")
        if matricula not in self.__medicos:
            raise MedicoNoDisponibleException("Médico no disponible.")
        if any(t.obtener_medico().obtener_matricula() == matricula and t.obtener_fecha_hora() == fecha_hora for t in self.__turnos):
            raise TurnoOcupadoException("Ese turno ya está ocupado.")
        
        medico = self.__medicos[matricula]
        dia = self.obtener_dia_semana_en_espanol(fecha_hora)
        if not self.validar_especialidad_en_dia(medico, especialidad, dia):
            raise MedicoNoDisponibleException("El médico no atiende esa especialidad ese día.")
        
        paciente = self.__pacientes[dni]
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException()
        if matricula not in self.__medicos:
            raise MedicoNoDisponibleException()
        if not medicamentos or not all(isinstance(m, str) for m in medicamentos):
            raise RecetaInvalidaException("Medicamentos inválidos.")
        
        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)

    def obtener_pacientes(self):
        return list(self.__pacientes.values())

    def obtener_medicos(self):
        return list(self.__medicos.values())

    def obtener_turnos(self):
        return list(self.__turnos)

    def obtener_historia_clinica_por_dni(self, dni: str):
        return self.__historias_clinicas.get(dni)

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime):
        dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        return dias[fecha_hora.weekday()]

    def validar_especialidad_en_dia(self, medico: Medico, especialidad: str, dia: str):
        return medico.obtener_especialidad_para_dia(dia) == especialidad 
    


    def obtener_medico_por_matricula(self, matricula: str):
        if matricula not in self.__medicos:
            raise ValueError("Médico no encontrado.")
        return self.__medicos[matricula] 