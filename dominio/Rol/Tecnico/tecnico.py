from dataclasses import dataclass

from dominio.Persona.PersonaHumana.dni import DNI
from dominio.Rol.rol import Rol

@dataclass
class Tecnico(Rol):
    dni: DNI
    cuil: str
    areaCobertura: str