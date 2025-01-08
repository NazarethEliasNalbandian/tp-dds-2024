from datetime import datetime
from dominio.Ubicacion.ubicacion import Ubicacion

class Heladera:
    def __init__(self, ubicacion, capacidad, fechaFuncionamiento):
        if not isinstance(ubicacion, Ubicacion):
            raise ValueError("La ubicación debe ser una instancia de la clase Ubicacion.")
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un número entero positivo.")
        if not isinstance(fechaFuncionamiento, str):
            raise ValueError("La fecha de funcionamiento debe ser una cadena en formato 'YYYY-MM-DD'.")
        
        try:
            self.fechaFuncionamiento = datetime.strptime(fechaFuncionamiento, "%Y-%m-%d")
        except ValueError:
            raise ValueError("La fecha de funcionamiento debe estar en formato 'YYYY-MM-DD'.")

        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.puntoEstrategico = f"Heladera {self.ubicacion.direccion}"
        self.viandas = []

    def agregar_vianda(self, vianda):
        from dominio.Heladera.Vianda.vianda import Vianda
        if not isinstance(vianda, Vianda):
            raise ValueError("La vianda debe ser una instancia de la clase Vianda.")
        if len(self.viandas) >= self.capacidad:
            raise ValueError("La heladera ha alcanzado su capacidad máxima de viandas.")
        self.viandas.append(vianda)

    def __str__(self):
        viandas_str = f"[{', '.join(str(v) for v in self.viandas)}]" if self.viandas else "[Sin viandas]"
        return (f"Heladera: [Ubicación: {self.ubicacion}, Capacidad: {self.capacidad} viandas, "
                f"Fecha de funcionamiento: {self.fechaFuncionamiento.date()}, Punto estratégico: {self.puntoEstrategico}, "
                f"Viandas: {viandas_str}]")