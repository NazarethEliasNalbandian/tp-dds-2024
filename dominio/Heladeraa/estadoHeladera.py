from dataclasses import dataclass
from datetime import datetime

@dataclass
class EstadoHeladera:
    activo: bool
    fecha: datetime
