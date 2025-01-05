from abc import ABC, abstractmethod
from dominio.Rol.rol import Rol

class Persona(ABC):
    def __init__(self, nombre, rol, direccion=None):
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre es obligatorio y debe ser una cadena.")
        if not isinstance(rol, Rol):
            raise ValueError("El rol debe ser una instancia de la clase Rol o sus derivados.")
        self.nombre = nombre
        self.rol = rol
        self.direccion = direccion

    @abstractmethod
    def mostrar_informacion(self):
        pass