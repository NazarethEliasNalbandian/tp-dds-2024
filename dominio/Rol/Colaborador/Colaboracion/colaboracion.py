from abc import ABC, abstractmethod
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Colaboracion(ABC):
    disponible: bool
    
    def puedeEjecutar(self):
        """Verifica si la colaboración está disponible para ejecutarse."""
        if not self.disponible:
            return False
        return True

    @abstractmethod
    def detalle(self):
        """Método abstracto para proporcionar detalles sobre la colaboración."""
        pass

    @abstractmethod
    def ejecutar(self):
        """Método abstracto para ejecutar la colaboración."""
        pass

    @staticmethod
    def verificar_disponibilidad(func):
        """Decorador estático que verifica si la colaboración está disponible antes de ejecutar un método."""
        def wrapper(self, *args, **kwargs):
            if self.puedeEjecutar():
                return func(self, *args, **kwargs)
            else:
                return "Operación no disponible"
        return wrapper
