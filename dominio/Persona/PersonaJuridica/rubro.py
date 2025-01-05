class Rubro:
    def __init__(self, descripcion):
        if not descripcion or not isinstance(descripcion, str):
            raise ValueError("La descripción del rubro debe ser una cadena no vacía.")
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion