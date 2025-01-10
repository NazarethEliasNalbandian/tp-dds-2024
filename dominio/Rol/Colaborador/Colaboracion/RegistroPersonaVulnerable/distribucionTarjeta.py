from dataclasses import dataclass
from datetime import date

from dominio.Rol.Colaborador.colaborador import Colaborador
from dominio.Rol.Vulnerable.Tarjeta.tarjeta import Tarjeta
from dominio.Rol.Vulnerable.vulnerable import Vulnerable

@dataclass
class DistribucionTarjeta:
    colaborador: Colaborador
    fechaReparto: date
    vulnerable: Vulnerable
    tarjetaEntregada: Tarjeta