import unittest
from datetime import datetime
from modelo.turno import Turno
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "12345678", "01/01/2000")
        self.especialidad = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        self.medico = Medico("Dr. Juan", "MAT123", [self.especialidad])
        self.fecha_hora = datetime(2025, 12, 12, 12, 0)

    def test_crear_turno_correcto(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Pediatría")
        self.assertEqual(turno.obtener_medico(), self.medico)
        self.assertEqual(turno.obtener_fecha_hora(), self.fecha_hora)

    def test_error_paciente_invalido(self):
        with self.assertRaises(ValueError):
            Turno("no paciente", self.medico, self.fecha_hora, "Pediatría")

    def test_error_especialidad_vacia(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, self.fecha_hora, "") 