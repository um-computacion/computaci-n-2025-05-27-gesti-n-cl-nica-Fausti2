import unittest
from modelo.receta import Receta
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Ana", "12345678", "02/02/1990")
        especialidad = Especialidad("Clínica", ["lunes"])
        self.medico = Medico("Dra. Rosa", "MAT001", [especialidad])
        self.medicamentos = ["Ibuprofeno", "Paracetamol"]

    def test_crear_receta_valida(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        self.assertIn("Ibuprofeno", str(receta))

    def test_receta_medicamentos_invalidos(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, [])

    def test_receta_paciente_invalido(self):
        with self.assertRaises(ValueError):
            Receta("no paciente", self.medico, self.medicamentos) 