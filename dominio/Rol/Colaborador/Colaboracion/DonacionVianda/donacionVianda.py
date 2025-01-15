from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from dominio.Heladeraa.Vianda.vianda import Vianda
from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion
from dominio.Rol.Colaborador.colaborador import Colaborador
    
@dataclass
class DonacionVianda(Colaboracion):
    viandas: List[Vianda] = field(default_factory=list)
    fecha_donacion: str
    colaborador: Colaborador
    disponible: bool = True

    def __post_init__(self):
        if not self.viandas:
            raise ValueError("Debe proporcionar al menos una vianda.")
        if not isinstance(self.fecha_donacion, str) or not self.fecha_donacion:
            raise ValueError("La fecha de donación debe ser una cadena no vacía.")
        if not isinstance(self.colaborador, Colaborador):
            raise ValueError("El colaborador debe ser una instancia de la clase Colaborador.")

    @Colaboracion.verificar_disponibilidad
    def detalle(self):
        viandas_detalle = ', '.join(vianda.nombre for vianda in self.viandas)
        return f"Donación de Viandas: {viandas_detalle}, Fecha: {self.fecha_donacion}, Colaborador: {self.colaborador.descripcion()}"
    
    @Colaboracion.verificar_disponibilidad
    def ejecutar(self):
        return self.detalle()