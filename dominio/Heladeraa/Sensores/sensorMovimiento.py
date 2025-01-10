from dataclasses import dataclass, field
from typing import List

from dominio.Heladeraa.Sensores.sensor import Sensor

@dataclass
class SensorMovimiento(Sensor):
    hayIntentoRobo: bool

    def notificar(self):
        """Notifica a todas las heladeras monitoreadas para desactivarse si hay un intento de robo."""
        if self.hayIntentoRobo:
            for heladera in self.heladerasAMonitorear:
                if heladera.estaActiva():
                    heladera.agregarEstado(activo=False)
                    print(f"Heladera {heladera.modelo} desactivada debido a intento de robo.")
