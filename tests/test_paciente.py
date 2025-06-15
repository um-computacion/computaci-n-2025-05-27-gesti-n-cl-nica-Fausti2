import unittest
from modelo.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_creacion_correcta(self):
        p = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.assertEqual(p.obtener_dni(), "12345678")

    def test_error_campos_vacios(self):
        with self.assertRaises(ValueError):
            Paciente("", "", "")

if __name__ == "__main__":
    unittest.main() 