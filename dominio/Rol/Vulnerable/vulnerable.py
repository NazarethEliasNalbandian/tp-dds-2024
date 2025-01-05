from dominio.Rol.rol import Rol

class Vulnerable(Rol):
    def __init__(self, fecha_nacimiento, fecha_registro, posee_domicilio, numero_documento, tipo_documento, cantidad_hijos):
        if not isinstance(fecha_nacimiento, str) or not fecha_nacimiento:
            raise ValueError("La fecha de nacimiento debe ser una cadena no vacía.")
        if not isinstance(fecha_registro, str) or not fecha_registro:
            raise ValueError("La fecha de registro debe ser una cadena no vacía.")
        if not isinstance(posee_domicilio, bool):
            raise ValueError("El atributo posee_domicilio debe ser un booleano.")
        if not isinstance(numero_documento, (int, str)) or not numero_documento:
            raise ValueError("El número de documento debe ser un valor válido.")
        if not isinstance(tipo_documento, str) or not tipo_documento:
            raise ValueError("El tipo de documento debe ser una cadena no vacía.")
        if not isinstance(cantidad_hijos, int) or cantidad_hijos < 0:
            raise ValueError("La cantidad de hijos debe ser un número entero no negativo.")

        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_registro = fecha_registro
        self.posee_domicilio = posee_domicilio
        self.numero_documento = numero_documento
        self.tipo_documento = tipo_documento
        self.cantidad_hijos = cantidad_hijos

    def posee_hijos(self):
        return self.cantidad_hijos > 0

    def posee_domicilio(self):
        return self.posee_domicilio and self.posee_domicilio is not None

    def descripcion(self):
        return (f"Vulnerable - Fecha de Nacimiento: {self.fecha_nacimiento}, Fecha de Registro: {self.fecha_registro}, "
                f"Posee Domicilio: {'Sí' if self.posee_domicilio() else 'No'}, Número de Documento: {self.numero_documento}, "
                f"Tipo de Documento: {self.tipo_documento}, Cantidad de Hijos: {self.cantidad_hijos}, "
                f"Posee Hijos: {'Sí' if self.posee_hijos() else 'No'}")