from dataclasses import dataclass, field
import datetime
import sys
import os
from typing import List

from dominio.Rol.Colaborador.Colaboracion.DistribucionVianda.distribucionVianda import DistribucionVianda
from dominio.Rol.Colaborador.Colaboracion.DonacionDinero.donacionDinero import DonacionDinero
from dominio.Rol.Colaborador.Colaboracion.DonacionVianda.donacionVianda import DonacionVianda
from dominio.Rol.Colaborador.Colaboracion.RegistroPersonaVulnerable.registroPersonaVulnerable import RegistroPersonaVulnerable
from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import csv


def parse_fecha(fecha_str: str) -> datetime:
    """Convierte una cadena en formato 'dd/mm/yyyy' a un objeto datetime."""
    return datetime.strptime(fecha_str, "%d/%m/%Y")

@dataclass
class MigradorColaboraciones:
    colaboraciones: List[Colaboracion] = field(default_factory=list)

    def migrar_desde_csv(self, path: str):
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                forma_colaboracion = row['FormaColaboracion']
                fecha = parse_fecha(row['FechaColaboracion'])
                cantidad = int(row['Cantidad'])

                if forma_colaboracion == 'DINERO':
                    colaboracion = DonacionDinero(fechaColaboracion=fecha, monto=cantidad)
                elif forma_colaboracion == 'DONACION_VIANDAS':
                    colaboracion = DonacionVianda(fechaColaboracion=fecha, cantidadViandas=cantidad)
                elif forma_colaboracion == 'REDISTRIBUCION_VIANDAS':
                    colaboracion = DistribucionVianda(fechaColaboracion=fecha, cantidad_viandas=cantidad)
                elif forma_colaboracion == 'ENTREGA_TARJETAS':
                    # Asumimos que 'Cantidad' representa el número de tarjetas entregadas
                    colaboracion = RegistroPersonaVulnerable(fechaColaboracion=fecha, distribuciones=[cantidad for _ in range(cantidad)])

                self.colaboraciones.append(colaboracion)
