from modelo.clinica import Clinica, PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException, RecetaInvalidaException
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from datetime import datetime

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Clínica ---")
            print("1) Agregar paciente")
            print("2) Agregar médico")
            print("3) Agendar turno")
            print("4) Agregar especialidad a médico")
            print("5) Emitir receta")
            print("6) Ver historia clínica")
            print("7) Ver todos los turnos")
            print("8) Ver todos los pacientes")
            print("9) Ver todos los médicos")
            print("0) Salir")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.agregar_medico()
            elif opcion == "3":
                self.agendar_turno()
            elif opcion == "4":
                self.agregar_especialidad()
            elif opcion == "5":
                self.emitir_receta()
            elif opcion == "6":
                self.ver_historia_clinica()
            elif opcion == "7":
                self.ver_turnos()
            elif opcion == "8":
                self.ver_pacientes()
            elif opcion == "9":
                self.ver_medicos()
            elif opcion == "0":
                print("Saliendo...")
                break
            else:
                print("Opción inválida")

    def agregar_paciente(self):
        try:
            nombre = input("Nombre completo: ")
            dni = input("DNI: ")
            fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ")
            paciente = Paciente(nombre, dni, fecha_nac)
            self.clinica.agregar_paciente(paciente)
            print("Paciente agregado correctamente.")
        except Exception as e:
            print(f"Error: {e}")

    def agregar_medico(self):
        try:
            nombre = input("Nombre del médico: ")
            matricula = input("Matrícula: ")
            medico = Medico(nombre, matricula)
            self.clinica.agregar_medico(medico)
            print("Médico agregado correctamente.")
        except Exception as e:
            print(f"Error: {e}")

    def agregar_especialidad(self):
        try:
            matricula = input("Matrícula del médico: ")
            tipo = input("Especialidad: ")
            dias = input("Días de atención (separados por coma): ").split(",")
            especialidad = Especialidad(tipo, [d.strip().lower() for d in dias])
            medico = self.clinica.obtener_medico_por_matricula(matricula)
            medico.agregar_especialidad(especialidad)
            print("Especialidad agregada.")
        except Exception as e:
            print(f"Error: {e}")

    def agendar_turno(self):
        try:
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            especialidad = input("Especialidad: ")
            fecha_input = input("Fecha y hora (formato aaaa-mm-dd HH:MM): ")
            fecha_hora = datetime.strptime(fecha_input, "%Y-%m-%d %H:%M")
            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("Turno agendado correctamente.")
        except (PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException) as e:
            print(f"Error al agendar turno: {e}")
        except Exception as e:
            print(f"Error general: {e}")

    def emitir_receta(self):
        try:
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            medicamentos = input("Medicamentos (separados por coma): ").split(",")
            self.clinica.emitir_receta(dni, matricula, [m.strip() for m in medicamentos])
            print("Receta emitida correctamente.")
        except RecetaInvalidaException as e:
            print(f"Error de receta: {e}")
        except Exception as e:
            print(f"Error general: {e}")

    def ver_historia_clinica(self):
        dni = input("DNI del paciente: ")
        historia = self.clinica.obtener_historia_clinica_por_dni(dni)
        if historia:
            print(historia)
        else:
            print("Historia clínica no encontrada.")

    def ver_turnos(self):
        for turno in self.clinica.obtener_turnos():
            print(turno)

    def ver_pacientes(self):
        for paciente in self.clinica.obtener_pacientes():
            print(paciente)

    def ver_medicos(self):
        for medico in self.clinica.obtener_medicos():
            print(medico) 