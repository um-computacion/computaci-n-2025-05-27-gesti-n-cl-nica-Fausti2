import unittest
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class TestMedico(unittest.TestCase):

    def setUp(self):
        self.medico = Medico("Dr. Juan Pérez", "MAT1234")

    def test_matricula(self):
        self.assertEqual(self.medico.obtener_matricula(), "MAT1234")

    def test_agregar_especialidad_correcta(self):
        esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(esp)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("lunes"), "Cardiología")

    def test_especialidad_repetida(self):
        esp = Especialidad("Pediatría", ["martes"])
        self.medico.agregar_especialidad(esp)
        with self.assertRaises(ValueError):
            self.medico.agregar_especialidad(esp)

    def test_especialidad_inexistente_en_dia(self):
        esp = Especialidad("Clínica", ["jueves"])
        self.medico.agregar_especialidad(esp)
        self.assertIsNone(self.medico.obtener_especialidad_para_dia("lunes"))

    def test_error_tipo_especialidad(self):
        with self.assertRaises(TypeError):
            self.medico.agregar_especialidad("No es una especialidad")

if __name__ == "__main__":
    unittest.main() 