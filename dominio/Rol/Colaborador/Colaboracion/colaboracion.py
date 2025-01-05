## Al Rol le vamos a agregar un tipo que representa el tipo de persona
## A la colaboracion le vamos a agregar una lista de tipos que contenga los tipos de roles que pueden hacer esa colaboracion

from abc import ABC, abstractmethod


class Colaboracion(ABC):
    def __init__(self, disponible):
        if not isinstance(disponible, bool):
            raise ValueError("El atributo disponible debe ser un booleano.")
        self.disponible = disponible

    @abstractmethod
    def detalle(self):
        pass