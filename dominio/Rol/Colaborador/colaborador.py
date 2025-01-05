from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion
from dominio.Rol.rol import Rol


class Colaborador(Rol):
    def __init__(self):
        self.colaboraciones = []

    def agregar_colaboracion(self, colaboracion):
        if not isinstance(colaboracion, Colaboracion):
            raise ValueError("La colaboración debe ser una instancia de la clase Colaboracion o sus derivados.")
        self.colaboraciones.append(colaboracion)

    def descripcion(self):
        return f"Colaborador en el área de {self.area}, con {len(self.colaboraciones)} colaboraciones"