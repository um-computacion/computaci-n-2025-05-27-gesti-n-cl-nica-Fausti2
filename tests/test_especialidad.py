import unittest
from modelo.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):

    def test_creacion_correcta(self):
        esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.assertEqual(esp.obtener_especialidad(), "Cardiología")
        self.assertTrue(esp.verificar_dia("lunes"))
        self.assertTrue(esp.verificar_dia("MiÉrCoLeS"))  # prueba con mayúsculas
        self.assertFalse(esp.verificar_dia("viernes"))

    def test_error_si_campos_vacios(self):
        with self.assertRaises(ValueError):
            Especialidad("", [])

    def test_str(self):
        esp = Especialidad("Pediatría", ["martes", "jueves"])
        resultado = str(esp)
        self.assertIn("Pediatría", resultado)
        self.assertIn("martes", resultado)
        self.assertIn("jueves", resultado)

if __name__ == "__main__":
    unittest.main() 