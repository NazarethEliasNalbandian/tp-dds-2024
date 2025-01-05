from abc import ABC, abstractmethod

class Rol(ABC):
    @abstractmethod
    def descripcion(self):
        pass