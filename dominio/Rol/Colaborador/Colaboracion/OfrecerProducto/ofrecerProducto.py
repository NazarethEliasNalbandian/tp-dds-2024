from dataclasses import dataclass, field
from typing import List
from dominio.Rol.Colaborador.Colaboracion.OfrecerProducto.oferta import Oferta
from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion


@dataclass
class OfrecerProducto(Colaboracion):
    ofertas: List[Oferta] = field(default_factory=list)

    def agregarOferta(self, oferta: Oferta):
        """Agrega una nueva oferta a la lista de ofertas."""
        self.ofertas.append(oferta)

    def detalle(self):
        """Proporciona detalles sobre las ofertas disponibles."""
        if not self.ofertas:
            return "No hay ofertas disponibles."
        detalles = "\n".join(f"Producto: {oferta.producto.nombre}, Costo en Puntos: {oferta.costoEnPuntos}" for oferta in self.ofertas)
        return detalles