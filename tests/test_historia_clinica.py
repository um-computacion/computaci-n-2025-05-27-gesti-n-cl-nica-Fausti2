import unittest
from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.especialidad import Especialidad
from modelo.historia_clinica import HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.medico = Medico("Dra. López", "MAT4567")
        self.especialidad = Especialidad("Clínica", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad)
        self.turno = Turno(self.paciente, self.medico, datetime(2025, 6, 21, 15, 0), "Clínica")
        self.receta = Receta(self.paciente, self.medico, ["Ibuprofeno"])
        self.historia = HistoriaClinica(self.paciente)

    def test_agregar_turno(self):
        self.historia.agregar_turno(self.turno)
        self.assertEqual(len(self.historia.obtener_turnos()), 1)

    def test_agregar_receta(self):
        self.historia.agregar_receta(self.receta)
        self.assertEqual(len(self.historia.obtener_recetas()), 1)

    def test_str_contiene_datos(self):
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)
        s = str(self.historia)
        self.assertIn("Juan Pérez", s)
        self.assertIn("Ibuprofeno", s)
        self.assertIn("Clínica", s)

    def test_error_paciente(self):
        with self.assertRaises(TypeError):
            HistoriaClinica("no paciente")

    def test_error_turno(self):
        with self.assertRaises(TypeError):
            self.historia.agregar_turno("no turno")

    def test_error_receta(self):
        with self.assertRaises(TypeError):
            self.historia.agregar_receta("no receta")

if __name__ == "__main__":
    unittest.main() 