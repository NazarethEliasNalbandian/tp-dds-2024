from dominio.Heladera.heladera import Heladera
from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion

class DistribucionVianda(Colaboracion):
    def __init__(self, heladera_origen, heladera_destino, cantidad_viandas, motivo, fecha, disponible=True):
        super().__init__(disponible)
        if not isinstance(heladera_origen, Heladera):
            raise ValueError("La heladera de origen debe ser una instancia de la clase Heladera.")
        if not isinstance(heladera_destino, Heladera):
            raise ValueError("La heladera de destino debe ser una instancia de la clase Heladera.")
        if not isinstance(cantidad_viandas, int) or cantidad_viandas <= 0:
            raise ValueError("La cantidad de viandas debe ser un número entero positivo.")
        if not isinstance(motivo, str) or not motivo:
            raise ValueError("El motivo debe ser una cadena no vacía.")
        if not isinstance(fecha, str) or not fecha:
            raise ValueError("La fecha debe ser una cadena no vacía.")
        
        self.heladera_origen = heladera_origen
        self.heladera_destino = heladera_destino
        self.cantidad_viandas = cantidad_viandas
        self.motivo = motivo
        self.fecha = fecha

    def detalle(self):
        if not self.disponible:
            return "Este colaborador no puede realizar esta tarea."
        return (f"Distribución de viandas: {self.cantidad_viandas} unidades\n"
                f"Heladera Origen: {self.heladera_origen}\n"
                f"Heladera Destino: {self.heladera_destino}\n"
                f"Motivo: {self.motivo}\n"
                f"Fecha: {self.fecha}")