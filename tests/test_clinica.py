import unittest
from modelo.clinica import Clinica, PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from datetime import datetime

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.medico = Medico("Dra. López", "MAT4567")
        self.especialidad = Especialidad("Clínica", ["miércoles"])
        self.medico.agregar_especialidad(self.especialidad)
        self.fecha = datetime(2025, 6, 18, 10, 0)  # miércoles

    def test_agregar_paciente_y_medico(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.assertEqual(len(self.clinica.obtener_pacientes()), 1)
        self.assertEqual(len(self.clinica.obtener_medicos()), 1)

    def test_agendar_turno_exitoso(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.clinica.agendar_turno("12345678", "MAT4567", "Clínica", self.fecha)
        self.assertEqual(len(self.clinica.obtener_turnos()), 1)

    def test_turno_duplicado(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.clinica.agendar_turno("12345678", "MAT4567", "Clínica", self.fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "MAT4567", "Clínica", self.fecha)

    def test_turno_especialidad_no_disponible(self):
        fecha_invalida = datetime(2025, 6, 17, 10, 0)  # martes
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "MAT4567", "Clínica", fecha_invalida)

if __name__ == "__main__":
    unittest.main() 