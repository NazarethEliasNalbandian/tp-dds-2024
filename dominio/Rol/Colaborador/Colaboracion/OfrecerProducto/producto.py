from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Producto:
    nombre: str
    apellido: str
    imagen: Optional[str] = None
