"""* EJERCICIO:
* Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
* un ejemplo con cada nivel de "severidad" disponible.
*
* DIFICULTAD EXTRA (opcional):
* Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
* y listar dichas tareas.
* - Añadir: recibe nombre y descripción.
* - Eliminar: por nombre de la tarea.
* Implementa diferentes mensajes de log que muestren información según la
* tarea ejecutada (a tu elección).
* Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
"""

# nivel 1
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    filename="task.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="UTF-8",
)
logging.debug("Mensaje de depuración")
logging.info("Infomación general")
logging.warning("Advertencia")
logging.error("Erro detectado")
logging.critical("Error crítico")


# Dificultad extra
class Task:
    def __init__(self) -> None:
        self.tasks = {}

    def task_create(self, nombre: str, descripcion: str):
        logging.info("Creando una nueva tarea")
        self.tasks[nombre] = descripcion
        logging.info("Nueva tarea creada")

    def task_list(self):
        if self.tasks is None:
            logging.debug("No hay tareas registradas")
        logging.info("Lista de tareas registradas")
        for key, value in enumerate(self.tasks.items(), start=1):
            print(f"{key}-{value}")

    def task_delete(self, nombre: str):
        logging.warning("Vas a eliminar una tarea")
        if nombre in self.tasks:
            del self.tasks[nombre]
        logging.debug(f"Se ha eliminado la tarea %s {nombre}")


tasks = Task()

tasks.task_list()

tasks.task_create(
    "Estudiar", "Hacer ejercicios de practica de python, fastapi y base datos"
)
tasks.task_create(
    "Control", "Crear un cronograma para estudiar de manera mas eficiente"
)
tasks.task_create("Difrutar", "Recuerda que lo que sea que hagas debes desfrutarlo")

tasks.task_delete("Control")

tasks.task_list()
