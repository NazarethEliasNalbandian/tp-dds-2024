from dataclasses import dataclass

from dominio.Espacio.ubicacion import Ubicacion

@dataclass
class Zona:
    ubicacion: Ubicacion
    radio: int