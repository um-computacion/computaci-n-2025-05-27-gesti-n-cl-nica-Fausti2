import unittest
from modelo.receta import Receta
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class TestReceta(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.medico = Medico("Dra. López", "MAT4567")
        especialidad = Especialidad("Clínica", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(especialidad)

    def test_creacion_correcta(self):
        receta = Receta(self.paciente, self.medico, ["Paracetamol", "Ibuprofeno"])
        self.assertIn("Paracetamol", str(receta))
        self.assertIn("Ibuprofeno", str(receta))

    def test_error_tipo_paciente(self):
        with self.assertRaises(TypeError):
            Receta("no paciente", self.medico, ["Paracetamol"])

    def test_error_tipo_medico(self):
        with self.assertRaises(TypeError):
            Receta(self.paciente, "no medico", ["Paracetamol"])

    def test_error_lista_vacia_medicamentos(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, [])

    def test_error_medicamento_no_string(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, [123])

if __name__ == "__main__":
    unittest.main() 