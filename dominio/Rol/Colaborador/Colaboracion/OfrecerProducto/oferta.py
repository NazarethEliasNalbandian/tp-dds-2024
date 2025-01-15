from dataclasses import dataclass

from dominio.Rol.Colaborador.Colaboracion.OfrecerProducto.producto import Producto

@dataclass
class Oferta:
    producto: Producto
    costoEnPuntos: int