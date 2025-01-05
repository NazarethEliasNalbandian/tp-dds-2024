import datetime

class Contraseña:
    def __init__(self, password, fecha_creacion=None, contraseñas_previas=None):
        if not password or not isinstance(password, str):
            raise ValueError("La contraseña debe ser una cadena no vacía.")
        self.password = password
        self.fecha_creacion = fecha_creacion if fecha_creacion else datetime.now().isoformat()
        self.contraseñas_previas = contraseñas_previas if contraseñas_previas else []
        self.longitud = len(password)

    def agregar_contraseña_previa(self, contraseña_previa):
        if not isinstance(contraseña_previa, Contraseña):
            raise ValueError("La contraseña previa debe ser una instancia de la clase Contraseña.")
        self.contraseñas_previas.append(contraseña_previa)

    def cambiarContraseña(self, nueva_password):
        if not nueva_password or not isinstance(nueva_password, str):
            raise ValueError("La nueva contraseña debe ser una cadena no vacía.")
        contraseña_previa = Contraseña(self.password, self.fecha_creacion)
        self.agregar_contraseña_previa(contraseña_previa)
        self.password = nueva_password
        self.fecha_creacion = datetime.now().isoformat()
        self.longitud = len(nueva_password)

    def __str__(self):
        return f"Contraseña actual: {self.password}, Longitud: {self.longitud}, Fecha de creación: {self.fecha_creacion}"