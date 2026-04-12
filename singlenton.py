"""* EJERCICIO:
* Explora el patrón de diseño "singleton" y muestra cómo crearlo
* con un ejemplo genérico.
*
* DIFICULTAD EXTRA (opcional):
* Utiliza el patrón de diseño "singleton" para representar una clase que
* haga referencia a la sesión de usuario de una aplicación ficticia.
* La sesión debe permitir asignar un usuario (id, username, nombre y email),
* recuperar los datos del usuario y borrar los datos de la sesión."""

# Forma 1 la más basica usando el método __new__
from typing_extensions import Self


"""class Singlento(object):
    _instance = None

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = object.__new__(
                cls
            )  # si usamos object como parametro de la clase padre, podemos usar super()
        return cls._instance


object1 = Singleton()
object2 = Singleton()
print(object1 is object2)"""


# forma 2 usando el método __new__ y los parametros *args y **kwargs
class Singlenton2:
    _instance2 = None

    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance2 is None:
            cls._instance2 = super(Singlenton2, cls).__new__(
                cls, *args, **kwargs
            )  # podemos pasar el super() con y sin argumentos.
        return cls._instance2


obj1 = Singlenton2()
obj2 = Singlenton2()
print(obj1 is obj2)


# forma 3 creando un decorador, no usamos métodos nativos de py.
def singleton(cls):
    instancias = {}

    def get_instancias(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        return instancias[cls]

    return get_instancias


@singleton
class Logger:
    def __init__(self) -> None:
        self.logs = []

    def crear_log(self, mensaje):
        self.logs.append(mensaje)
        print(f"Log: {mensaje}")


log1 = Logger()
log2 = Logger()
log1.crear_log("Sigleton aplicando decorador")
print(log1 is log2)


# Punto extra
class UserSession:
    _instance = None
    id: int
    name: str
    user_name: str
    email: str

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(UserSession, cls).__new__(
                cls, *args, **kwargs
            )  # podemos pasar el super() con y sin argumentos y el __new__ sin y con- *,**.
        return cls._instance

    def set_user(self, id: int, name: str, user_name: str, email: str):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.email = email

    def get_user(self):
        return f"ID: {self.id}|Name: {self.name}|Email: {self.email}|User: {self.user_name}"

    def delete_user(self):
        self.id = 0
        self.name = "None"
        self.user_name = "None"
        self.email = "None"


user1 = UserSession()
user1.set_user(1, "Nando", "NAN2ELMANK", "nando023@algo.com")
print(user1.get_user())
user1.delete_user()
print(user1.get_user())
user2 = UserSession()
print(user1 == user2)
print(user1 is user2)
