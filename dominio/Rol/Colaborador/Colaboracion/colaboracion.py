## Al Rol le vamos a agregar un tipo que representa el tipo de persona
## A la colaboracion le vamos a agregar una lista de tipos que contenga los tipos de roles que pueden hacer esa colaboracion

from abc import ABC, abstractmethod


class Colaboracion(ABC):
    def __init__(self, disponible):
        if not isinstance(disponible, bool):
            raise ValueError("El atributo disponible debe ser un booleano.")
        self.disponible = disponible
    
    def puedeEjecutar(self):
        if not self.disponible:
            return False
        return True

    @abstractmethod
    def detalle(self):
        pass
    
    @abstractmethod
    def ejecutar(self):
        pass
    
    # Al usar static, el metodo no puede utilizar las variables de clase ni a variables de self
    # Es como si el metodo se hiciera fuera de la clase
    @staticmethod
    def verificar_disponibilidad(func):
        # Decorador que verifica si la colaboración está disponible antes de ejecutar un método.
        # *args se utiliza para recibir N parametros posicionales/simples: nombreVariable. Estos son almacenados en una tupla 
        # **kwargs (kw = key words) se utiliza para recibir M parametros de palabras clave: (clave=valor). Estos son almacenados en un diccionario.
        def wrapper(self, *args, **kwargs):
            if self.puedeEjecutar():
                return func(self, *args, **kwargs)
            else:
                return "Operación no disponible"
        return wrapper