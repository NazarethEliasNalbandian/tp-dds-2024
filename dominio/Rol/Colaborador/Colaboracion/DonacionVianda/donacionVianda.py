from datetime import datetime
from dominio.Heladera.Vianda.vianda import Vianda
from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion
from dominio.Rol.Colaborador.colaborador import Colaborador
    
class DonacionVianda(Colaboracion):
    def __init__(self, vianda, fecha_donacion, colaborador, disponible=True):
        super().__init__(disponible)
        if not isinstance(vianda, Vianda):
            raise ValueError("La vianda debe ser una instancia de la clase Vianda.")
        if not isinstance(fecha_donacion, str) or not fecha_donacion:
            raise ValueError("La fecha de donación debe ser una cadena no vacía.")
        if not isinstance(colaborador, Colaborador):
            raise ValueError("El colaborador debe ser una instancia de la clase Colaborador.")
        self.vianda = vianda
        self.fecha_donacion = fecha_donacion
        self.colaborador = colaborador

    @Colaboracion.verificar_disponibilidad
    def detalle(self):
        return f"Donación de Vianda: {self.vianda}, Fecha: {self.fecha_donacion}, Colaborador: {self.colaborador.descripcion()}"
    
    @Colaboracion.verificar_disponibilidad
    def ejecutar(self):
        return self.detalle()