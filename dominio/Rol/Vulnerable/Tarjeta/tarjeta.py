from dataclasses import dataclass, field
from datetime import date
from typing import List

from dominio.Rol.Vulnerable.Tarjeta.uso import Uso
from dominio.Rol.Vulnerable.vulnerable import Vulnerable

@dataclass
class Tarjeta:
    codigo: str
    usosRealizados: List[Uso] = field(default_factory=list)
    entregada: bool
    titular: Vulnerable = None

    def cantidadUsosPorDia(self) -> int:
        return 4 + 2 * self.titular.cantidad_hijos

    def usar(self, nuevo_uso: Uso):
        # Suma Cada vez que se cumple la condicion en la iteracion se agarra la expresión Resultado y se va sumando
        # Luego, se retorna la suma de todo eso al completar la iteracion
        # sum(resultado for item in iterable if condicion)
        usos_en_fecha = sum(1 for uso in self.usosRealizados if uso.fechaUso == nuevo_uso.fechaUso) 
        
        if usos_en_fecha >= self.cantidadUsosPorDia():
            raise ValueError("No se pueden realizar más usos para este día.")
        
        self.usosRealizados.append(nuevo_uso)
