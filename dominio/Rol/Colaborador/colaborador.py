from dataclasses import dataclass, field
from typing import List
from dominio.CalculadorPuntos.calculadorPuntos import CalculadorDePuntos
from dominio.Rol.Colaborador.Colaboracion.OfrecerProducto.oferta import Oferta
from dominio.Rol.Colaborador.Colaboracion.OfrecerProducto.producto import Producto
from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion
from dominio.Rol.rol import Rol

@dataclass
class Colaborador(Rol):
    colaboraciones: List[Colaboracion] = field(default_factory=list)
    puntosParaCanjear: int = 0
    productosCanjeados: List[Producto] = field(default_factory=list)
    calculadorDePuntos: CalculadorDePuntos

    def agregar_colaboracion(self, colaboracion: Colaboracion):
        if not isinstance(colaboracion, Colaboracion):
            raise ValueError("La colaboración debe ser una instancia de la clase Colaboracion o sus derivados.")
        self.colaboraciones.append(colaboracion)

    def remover_colaboracion(self, colaboracion):
        if isinstance(colaboracion, int):  # Si se pasa un índice
            if colaboracion < 0 or colaboracion >= len(self.colaboraciones):
                raise IndexError("Índice de colaboración fuera de rango.")
            del self.colaboraciones[colaboracion]
        elif isinstance(colaboracion, Colaboracion):  # Si se pasa una instancia
            try:
                self.colaboraciones.remove(colaboracion)
            except ValueError:
                raise ValueError("La colaboración especificada no se encuentra en la lista.")
        else:
            raise ValueError("Debe proporcionar un índice o una instancia de Colaboracion para eliminar.")

    def descripcion(self):
        return f"Colaborador con {len(self.colaboraciones)} colaboraciones y {self.puntosParaCanjear} puntos para canjear."

    def actuar(self):
        resultados = []
        for colaboracion in self.colaboraciones:
            resultado = colaboracion.ejecutar()
            resultados.append(resultado)
        self.puntosParaCanjear =  self.calculadorDePuntos.calcularResultados(self.colaboraciones)
        return resultados

    def canjear_oferta(self, oferta: Oferta):
        """Método para canjear puntos por productos."""
        if self.puntosParaCanjear >= oferta.costoEnPuntos:
            self.productosCanjeados.append(oferta.producto)
            self.puntosParaCanjear -= oferta.costoEnPuntos
        else:
            raise ValueError("Puntos insuficientes para canjear el producto.")