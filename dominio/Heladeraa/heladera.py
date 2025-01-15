from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from dominio.Espacio.ubicacion import Ubicacion
from dominio.Heladeraa.Sensores.sensorMovimiento import SensorMovimiento
from dominio.Heladeraa.Sensores.sensorTemperatura import SensorTemperatura
from dominio.Heladeraa.Temperatura.temperatura import Temperatura
from dominio.Heladeraa.Vianda.vianda import Vianda
from dominio.Heladeraa.estadoHeladera import EstadoHeladera

@dataclass
class Heladera:
    ubicacion: Ubicacion
    capacidad: int
    fechaFuncionamiento: str
    temperatura: Temperatura
    modelo: str
    estados: List[EstadoHeladera] = field(default_factory=list)
    sensorTemperatura: SensorTemperatura
    sensorMovimiento: SensorMovimiento
    viandas: List['Vianda'] = field(default_factory=list)

    def __post_init__(self):
        """Valida la fecha de funcionamiento, convierte a datetime y establece el estado inicial activo."""
        try:
            self.fechaFuncionamiento = datetime.strptime(self.fechaFuncionamiento, "%Y-%m-%d")
        except ValueError:
            raise ValueError("La fecha de funcionamiento debe estar en formato 'YYYY-MM-DD'.")

        self.agregarEstado(activo=True)
    def mesesActiva(self) -> int:
        """Calcula el total de meses completos que la heladera ha estado activa desde su fecha de funcionamiento."""
        if not self.estaActiva():
            return 0
        fecha_actual = datetime.now()
        return (fecha_actual.year - self.fechaFuncionamiento.year) * 12 + fecha_actual.month - self.fechaFuncionamiento.month

    def agregar_vianda(self, vianda: 'Vianda'):
        """Agrega una vianda a la heladera si hay capacidad."""
        if len(self.viandas) >= self.capacidad:
            raise ValueError("La heladera ha alcanzado su capacidad máxima de viandas.")
        self.viandas.append(vianda)

    def remover_vianda(self, vianda: 'Vianda'):
        """Remueve una vianda de la heladera."""
        try:
            self.viandas.remove(vianda)
        except ValueError:
            raise ValueError("La vianda especificada no está en la heladera.")
    
    def tieneTemperaturaAceptable(self) -> bool:
        """Delega la verificación de la temperatura a la instancia de Temperatura."""
        return self.temperatura.temperaturaEstaAceptable()
    
    def estaActiva(self) -> bool:
        """Devuelve el estado activo más reciente basado en la fecha de los estados registrados."""
        if not self.estados:
            return False
        
        # max(iterable, key= funcionQueSeAplicaACadaElemento)
        # En este a caso, a cada estado de la lista de estados se le aplica la funcion lambda que retorna la fecha de ese estado
        # Luego, devuelve el maximo de esos elementos segun esa funcion (fecha mas reciente)
        estado_mas_reciente = max(self.estados, key=lambda estado: estado.fecha)
        return estado_mas_reciente.activo
    
    def actualizarTemperatura(self):
        """Actualiza la temperatura registrada en la heladera según el sensor de temperatura."""
        # Asume que sensorTemperatura tiene un atributo temperaturaHeladera que refleja la última medición
        nueva_temperatura = self.sensorTemperatura.temperaturaHeladera
        self.temperatura.ultimaTemperaturaRegistrada = nueva_temperatura
        print(f"Temperatura actualizada a {nueva_temperatura}°C en la heladera modelo {self.modelo}.")
        
        if not self.tieneTemperaturaAceptable():
            print("La temperatura registrada no es aceptable. Desactivando heladera.")
            self.agregarEstado(activo=False)

    def agregarEstado(self, activo: bool):
        """Agrega un nuevo estado a la lista de estados de la heladera."""
        nuevo_estado = EstadoHeladera(activo=activo, fecha=datetime.now())
        self.estados.append(nuevo_estado)
        print(f"Estado actualizado: {'Activa' if activo else 'Inactiva'} en fecha {nuevo_estado.fecha}.")