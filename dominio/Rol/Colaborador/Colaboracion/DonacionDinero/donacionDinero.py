from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion

class DonacionDinero(Colaboracion):
    def __init__(self, monto, fechaDonacion, disponible=True, frecuencia = None):
        super().__init__(disponible)
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("El monto debe ser un número positivo.")
        self.monto = monto
        self.fechaDonacion = fechaDonacion
        self.frecuencia = frecuencia

    @Colaboracion.verificar_disponibilidad
    def detalle(self):
        return f"Donación de dinero: ${self.monto:.2f}"
    
    @Colaboracion.verificar_disponibilidad
    def ejecutar(self):
        return self.detalle()