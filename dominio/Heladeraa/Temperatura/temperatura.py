from dataclasses import dataclass

@dataclass
class Temperatura:
    ultimaTemperaturaRegistrada: float
    temperaturaMaximaAceptable: float
    temperaturaMinimaAceptable: float

    def registrar_temperatura(self, nueva_temperatura: float):
        """Actualiza la última temperatura registrada."""
        self.ultimaTemperaturaRegistrada = nueva_temperatura
        self.verificar_temperatura()

    def verificar_temperatura(self):
        """Verifica si la temperatura actual está dentro del rango aceptable."""
        if self.ultimaTemperaturaRegistrada > self.temperaturaMaximaAceptable:
            print("Alerta: La temperatura ha superado el máximo aceptable.")
        elif self.ultimaTemperaturaRegistrada < self.temperaturaMinimaAceptable:
            print("Alerta: La temperatura ha caído por debajo del mínimo aceptable.")
        else:
            print("La temperatura está dentro del rango aceptable.")
    
    def temperaturaEstaAceptable(self) -> bool:
        """Determina si la temperatura está dentro del rango aceptable."""
        return (self.temperaturaMinimaAceptable <= self.ultimaTemperaturaRegistrada <= self.temperaturaMaximaAceptable)
