from dominio.Persona.PersonaHumana.dni import DNI
from dominio.Rol.Vulnerable.Tarjeta.tarjeta import Tarjeta
from dominio.Rol.rol import Rol

from dataclasses import dataclass, field

@dataclass
class Vulnerable(Rol):
    fecha_nacimiento: str
    fecha_registro: str
    posee_domicilio: bool
    dni: DNI
    cantidad_hijos: int = 0
    tarjeta: Tarjeta = field(default=None)

    def __post_init__(self):
        if not self.fecha_nacimiento:
            raise ValueError("La fecha de nacimiento debe ser una cadena no vacía.")
        if not self.fecha_registro:
            raise ValueError("La fecha de registro debe ser una cadena no vacía.")
        if not isinstance(self.numero_documento, (int, str)):
            raise ValueError("El número de documento debe ser un valor válido.")
        if not self.tipo_documento:
            raise ValueError("El tipo de documento debe ser una cadena no vacía.")
        if not isinstance(self.cantidad_hijos, int) or self.cantidad_hijos < 0:
            raise ValueError("La cantidad de hijos debe ser un número entero no negativo.")

    def posee_hijos(self) -> bool:
        """Devuelve True si la persona tiene uno o más hijos."""
        return self.cantidad_hijos > 0

    def descripcion(self) -> str:
        """Devuelve una descripción detallada de la persona."""
        return (f"Vulnerable - Fecha de Nacimiento: {self.fecha_nacimiento}, Fecha de Registro: {self.fecha_registro}, "
                f"Posee Domicilio: {'Sí' if self.posee_domicilio else 'No'}, Número de Documento: {self.numero_documento}, "
                f"Tipo de Documento: {self.tipo_documento}, Cantidad de Hijos: {self.cantidad_hijos}, "
                f"Posee Hijos: {'Sí' if self.posee_hijos() else 'No'}")
    
    def usarTarjeta(self):
        """Utiliza la tarjeta asociada a la persona vulnerable."""
        if self.tarjeta:
            self.tarjeta.usar()
        else:
            print("No hay tarjeta asignada a esta persona.")
