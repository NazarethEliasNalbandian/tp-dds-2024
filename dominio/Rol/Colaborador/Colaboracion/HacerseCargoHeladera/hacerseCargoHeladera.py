from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion

class HacerCargoHeladera(Colaboracion):
    def __init__(self, tiempo, disponible=True):
        super().__init__(disponible)
        if not isinstance(tiempo, int) or tiempo <= 0:
            raise ValueError("El tiempo debe ser un número entero positivo representando días.")
        self.tiempo = tiempo

    @Colaboracion.verificar_disponibilidad
    def detalle(self):
        return f"Uso de heladera por {self.tiempo} días"
    
    @Colaboracion.verificar_disponibilidad
    def ejecutar(self):
        return self.detalle()