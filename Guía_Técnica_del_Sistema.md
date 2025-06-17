## Cómo ejecutar el sistema

Desde la terminal, ubicado en la carpeta del proyecto, ejecutá:

python3 main.py 

Cómo ejecutar los tests 
python3 -m unittest discover tests 

Para ejecutar un test específico, por ejemplo: 
python3 -m unittest tests.test_paciente 


Explicación del diseño general:
-modelo/: contiene las clases principales del sistema (Paciente, Medico, Especialidad, Turno, Receta, HistoriaClinica, Clinica). Cada clase valida su propia información internamente y lanza excepciones si hay errores.
-tests/: contiene las pruebas unitarias de cada clase usando unittest. Se validan tanto los casos correctos como los errores esperados.
-cli.py: representa la interfaz de consola para el usuario. Muestra un menú, recibe entradas y llama a los métodos de la clase Clinica.
-main.py: archivo de entrada del sistema. Ejecuta la clase CLI. 

Validaciones y excepciones
Todas las verificaciones de datos se hacen dentro de las clases del sistema (modelo).  
Por ejemplo, si un DNI está mal escrito o una receta no tiene medicamentos, el error se detecta dentro de esas clases.

En la interfaz de consola (CLI), no se hacen validaciones.  
La consola solo muestra opciones y recibe datos.

Si algo sale mal, el sistema usa errores especiales (excepciones personalizadas) que son capturados por el CLI.  
Así, en vez de que el programa se cierre con un error técnico, se muestra un mensaje claro para el usuario.

Esto permite que el sistema funcione de manera ordenada y segura.