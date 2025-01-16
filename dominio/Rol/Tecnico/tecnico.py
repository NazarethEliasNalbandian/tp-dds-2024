from dataclasses import dataclass

from dominio.Persona.PersonaHumana.Documento.documento import Documento
from dominio.Rol.rol import Rol

@dataclass
class Tecnico(Rol):
    documento: Documento
    cuil: str
    areaCobertura: str