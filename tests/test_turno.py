import unittest
from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.turno import Turno

class TestTurno(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.medico = Medico("Dra. López", "MAT4567")
        self.especialidad = Especialidad("Clínica", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad)
        self.fecha = datetime(2025, 6, 20, 14, 0)
        self.turno = Turno(self.paciente, self.medico, self.fecha, "Clínica")

    def test_medico_asignado(self):
        self.assertEqual(self.turno.obtener_medico(), self.medico)

    def test_fecha_hora(self):
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha)

    def test_str(self):
        s = str(self.turno)
        self.assertIn("Juan Pérez", s)
        self.assertIn("Dra. López", s)
        self.assertIn("Clínica", s)

    def test_error_paciente(self):
        with self.assertRaises(TypeError):
            Turno("no paciente", self.medico, self.fecha, "Clínica")

    def test_error_medico(self):
        with self.assertRaises(TypeError):
            Turno(self.paciente, "no medico", self.fecha, "Clínica")

    def test_error_fecha(self):
        with self.assertRaises(TypeError):
            Turno(self.paciente, self.medico, "no fecha", "Clínica")

    def test_error_especialidad(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, self.fecha, "")

if __name__ == "__main__":
    unittest.main() 