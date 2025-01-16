from dataclasses import dataclass
from dominio.Persona.PersonaHumana.Documento.tipoDocumento import TipoDocumento

@dataclass
class Documento:
    nroDocumento: str
    tipoDocumento: TipoDocumento