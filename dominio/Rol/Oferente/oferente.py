from dataclasses import dataclass

from dominio.Rol.Colaborador.Colaboracion.OfrecerProducto.ofrecerProducto import OfrecerProducto
from dominio.Rol.rol import Rol

@dataclass
class Oferente(Rol):
    ofrecedor: OfrecerProducto

    def descripcion(self):
        return f"Oferente que gestiona las siguientes ofertas: {self.ofrecedor.detalle()}"