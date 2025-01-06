from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion

class HacerCargoHeladera(Colaboracion):
    def __init__(self, tiempo, disponible=True):
        super().__init__(disponible)
        if not isinstance(tiempo, int) or tiempo <= 0:
            raise ValueError("El tiempo debe ser un número entero positivo representando días.")
        self.tiempo = tiempo

    def detalle(self):
        if not self.disponible:
            return "Este colaborador no puede realizar esta tarea."
        return f"Uso de heladera por {self.tiempo} días"
    
    def ejecutar(self):
        return self.detalle()