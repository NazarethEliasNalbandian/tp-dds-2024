from dataclasses import dataclass, field
from typing import List

from dominio.Heladeraa.Sensores.sensor import Sensor

@dataclass
class SensorTemperatura(Sensor):
    temperaturaHeladera: float

    def notificar(self):
        """Llama al método actualizarTemperatura de todas las heladeras en heladerasAMonitorear."""
        for heladera in self.heladerasAMonitorear:
            heladera.actualizarTemperatura()
            print(f"Notificación enviada a {heladera.modelo}: temperatura actualizada a {self.temperaturaHeladera}°C.")
