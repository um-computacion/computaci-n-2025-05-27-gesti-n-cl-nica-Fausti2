class Paciente:
    def __init__(self, nombre, dni, fecha_nacimiento):
        if not nombre or not dni or not fecha_nacimiento:
            raise ValueError("Todos los campos son obligatorios para el paciente.")
        self.__nombre = nombre
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self):
        return self.__dni

    def __str__(self):
        return f"{self.__nombre}, {self.__dni}, {self.__fecha_nacimiento}" 