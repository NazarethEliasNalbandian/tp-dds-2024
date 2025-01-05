from dominio.Persona.MedioContacto.tipoMedioContacto import TipoMedioDeContacto

class MedioDeContacto:
    def __init__(self, tipo, descripcion):
        if not isinstance(tipo, TipoMedioDeContacto):
            raise ValueError(f"El tipo debe ser una instancia de TipoMedioDeContacto, no '{type(tipo)}'.")
        if not descripcion or not isinstance(descripcion, str):
            raise ValueError("La descripción debe ser una cadena no vacía.")

        self.tipo = tipo
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.tipo.value.capitalize()}: {self.descripcion}"