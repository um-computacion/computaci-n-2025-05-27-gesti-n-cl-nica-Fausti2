class Especialidad:
    def __init__(self, tipo, dias):
        if not tipo or not dias:
            raise ValueError("Tipo de especialidad y días son obligatorios.")
        self.__tipo = tipo
        self.__dias = [d.lower() for d in dias]

    def obtener_especialidad(self):
        return self.__tipo

    def verificar_dia(self, dia):
        return dia.lower() in self.__dias

    def __str__(self):
        return f"{self.__tipo} (Días: {', '.join(self.__dias)})" 