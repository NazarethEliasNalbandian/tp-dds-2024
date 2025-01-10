from dataclasses import dataclass
from datetime import date

from dominio import Heladeraa

@dataclass
class Uso:
    heladera: Heladeraa
    fechaUso: date