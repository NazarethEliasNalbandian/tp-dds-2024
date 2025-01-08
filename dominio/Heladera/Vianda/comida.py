from datetime import datetime

class Comida:
    def __init__(self, nombre, fechaCaducidad, calorias = None):
        # Validaciones básicas para los atributos
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(fechaCaducidad, str):
            raise ValueError("La fecha de caducidad debe ser una cadena en formato 'YYYY-MM-DD'.")
        
        try:
            self.fechaCaducidad = datetime.strptime(fechaCaducidad, "%Y-%m-%d")
        except ValueError:
            raise ValueError("La fecha de caducidad debe estar en formato 'YYYY-MM-DD'.")

        self.nombre = nombre
        self.calorias = calorias

    def es_caducado(self):
        """Verifica si la comida está caducada."""
        return datetime.now() > self.fechaCaducidad

    def __str__(self):
        """Representación en cadena de la clase."""
        estado = "Caducado" if self.es_caducado() else "No caducado"
        return f"Comida: {self.nombre}, Calorías: {self.calorias}, Fecha de caducidad: {self.fechaCaducidad.date()}, Estado: {estado}"