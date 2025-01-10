from dataclasses import dataclass, field
from typing import List
from abc import ABC, abstractmethod

from dominio import Heladeraa
from dominio.Heladeraa.heladera import Heladera

@dataclass
class Sensor(ABC):
    heladerasAMonitorear: List[Heladera] = field(default_factory=list)

    def agregarHeladera(self, heladera: Heladeraa):
        """Agrega una heladera a la lista de heladeras a monitorear."""
        self.heladerasAMonitorear.append(heladera)
        print(f"Heladera agregada para monitoreo: {heladera.modelo}")

    def removerHeladera(self, heladera: Heladeraa):
        """Remueve una heladera de la lista de heladeras a monitorear."""
        try:
            self.heladerasAMonitorear.remove(heladera)
            print(f"Heladera removida del monitoreo: {heladera.modelo}")
        except ValueError:
            print("La heladera especificada no está en la lista de monitoreo.")

    @abstractmethod
    def notificar(self):
        """Método abstracto para notificar sobre cambios o alertas de las heladeras."""
        pass
