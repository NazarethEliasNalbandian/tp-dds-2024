from dataclasses import dataclass, field
from typing import List

from dominio.Rol.Colaborador.Colaboracion.RegistroPersonaVulnerable.distribucionTarjeta import DistribucionTarjeta
from dominio.Rol.Vulnerable.Tarjeta.tarjeta import Tarjeta

@dataclass
class RegistroPersonaVulnerable:
    tarjetasADistribuir: List[Tarjeta] = field(default_factory=list)
    distribuciones: List[DistribucionTarjeta] = field(default_factory=list)

    def agregarTarjeta(self, tarjeta: Tarjeta):
        """Agrega una tarjeta a la lista de tarjetas a distribuir."""
        self.tarjetasADistribuir.append(tarjeta)

    def removerTarjeta(self, tarjeta: Tarjeta):
        """Remueve una tarjeta de la lista de tarjetas a distribuir."""
        if tarjeta in self.tarjetasADistribuir:
            self.tarjetasADistribuir.remove(tarjeta)
        else:
            raise ValueError("La tarjeta no está en la lista de tarjetas a distribuir.")
    
    def distribuir(self, distribucion: DistribucionTarjeta):
        """Distribuye una tarjeta y actualiza los registros correspondientes."""
        
        if distribucion.tarjetaEntregada not in self.tarjetasADistribuir:
            raise ValueError("La tarjeta a distribuir no está en la lista de tarjetas a distribuir.")
        
        self.distribuciones.append(distribucion)
        
        self.removerTarjeta(distribucion.tarjetaEntregada)
        
        distribucion.vulnerable.tarjeta = distribucion.tarjetaEntregada
        distribucion.tarjetaEntregada.entregada = True
        distribucion.tarjetaEntregada.titular = distribucion.vulnerable