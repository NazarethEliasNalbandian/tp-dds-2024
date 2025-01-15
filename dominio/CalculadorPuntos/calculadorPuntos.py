from dataclasses import dataclass
from typing import List

from dominio.Rol.Colaborador.Colaboracion.DistribucionVianda.distribucionVianda import DistribucionVianda
from dominio.Rol.Colaborador.Colaboracion.DonacionDinero.donacionDinero import DonacionDinero
from dominio.Rol.Colaborador.Colaboracion.DonacionVianda.donacionVianda import DonacionVianda
from dominio.Rol.Colaborador.Colaboracion.HacerseCargoHeladera.hacerseCargoHeladera import HacerCargoHeladera
from dominio.Rol.Colaborador.Colaboracion.RegistroPersonaVulnerable.registroPersonaVulnerable import RegistroPersonaVulnerable
from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion

@dataclass
class CalculadorDePuntos:
    coeficienteDonacionDinero: int
    coeficienteDistribucionVianda: int
    coeficienteDonacionVianda: int
    coeficienteRegistroPersonaVulnerable: int
    coeficienteHeladerasACargo: int

    def calcularResultados(self, colaboraciones: List['Colaboracion']) -> int:
        PESOS_DONADOS = sum(col.monto for col in colaboraciones if isinstance(col, DonacionDinero))
        VIANDAS_DISTRIBUIDAS = sum(col.cantidad_viandas for col in colaboraciones if isinstance(col, DistribucionVianda))
        VIANDAS_DONADAS = sum(len(col.viandas) for col in colaboraciones if isinstance(col, DonacionVianda))
        TARJETAS_REPARTIDAS = sum(len(col.distribuciones) for col in colaboraciones if isinstance(col, RegistroPersonaVulnerable))
        CANTIDAD_HELADERAS_ACTIVAS = sum(1 for col in colaboraciones if isinstance(col, HacerCargoHeladera))
        SUMATORIA_MESES_ACTIVAS = sum(col.heladera.mesesActiva() for col in colaboraciones if isinstance(col, HacerCargoHeladera))

        total_puntos = (PESOS_DONADOS * self.coeficienteDonacionDinero +
                        VIANDAS_DISTRIBUIDAS * self.coeficienteDistribucionVianda +
                        VIANDAS_DONADAS * self.coeficienteDonacionVianda +
                        TARJETAS_REPARTIDAS * self.coeficienteRegistroPersonaVulnerable +
                        CANTIDAD_HELADERAS_ACTIVAS * SUMATORIA_MESES_ACTIVAS * self.coeficienteHeladerasACargo)
        
        return total_puntos
