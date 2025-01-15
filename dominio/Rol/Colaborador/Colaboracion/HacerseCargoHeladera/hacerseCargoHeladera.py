from dataclasses import dataclass, field
from typing import List
from dominio.Espacio.ubicacion import Ubicacion
from dominio.Espacio.zona import Zona
from dominio.Heladeraa.heladera import Heladera
from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion

@dataclass
class HacerCargoHeladera(Colaboracion):
    tiempo: int
    puntosIdeales: List[Ubicacion] = field(default_factory=list)
    direccionElegida: str
    ubicacionDireccionElegida: Ubicacion
    zona: Zona
    heladera: Heladera
    disponible: bool = True

    def __post_init__(self):
        super().__init__(disponible=self.disponible)
        if not isinstance(self.tiempo, int) or self.tiempo <= 0:
            raise ValueError("El tiempo debe ser un número entero positivo representando días.")
        if not isinstance(self.heladera, Heladera):
            raise ValueError("El atributo heladera debe ser una instancia de la clase Heladera.")

    @Colaboracion.verificar_disponibilidad
    def detalle(self):
        heladera_info = f"{self.heladera.modelo} en {self.heladera.ubicacion.direccion}"
        return f"Uso de heladera {heladera_info} por {self.tiempo} días en {self.direccionElegida}, ubicada en {self.ubicacionDireccionElegida.direccion}. Zona de cobertura: {self.zona.ubicacion.direccion} con un radio de {self.zona.radio} metros."

    @Colaboracion.verificar_disponibilidad
    def ejecutar(self):
        return self.detalle()
