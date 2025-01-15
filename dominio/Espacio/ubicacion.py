class Ubicacion:
    def __init__(self, latitud, longitud, direccion, descripcion):
        if not isinstance(latitud, (int, float)) or not (-90 <= latitud <= 90):
            raise ValueError("La latitud debe ser un número entre -90 y 90.")
        if not isinstance(longitud, (int, float)) or not (-180 <= longitud <= 180):
            raise ValueError("La longitud debe ser un número entre -180 y 180.")
        if not isinstance(direccion, str) or not direccion.strip():
            raise ValueError("La dirección debe ser una cadena no vacía.")
        if not isinstance(descripcion, str):
            raise ValueError("La descripción debe ser una cadena.")

        self.latitud = latitud
        self.longitud = longitud
        self.direccion = direccion
        self.descripcion = descripcion

    def __str__(self):
        return (f"Ubicación: [Latitud: {self.latitud}, Longitud: {self.longitud}, "
                f"Dirección: {self.direccion}, Descripción: {self.descripcion}]")