from registro.contraseña import Contraseña
from registro.seguridadContraseña.seguridad import contrasenaNoEstaEnTop10000, cumpleRequisitosLongitudYCaracteres, noUtilizaCredencialesPredeterminadas


class Usuario:
    def __init__(self, username, password):
        if not username or not isinstance(username, str):
            raise ValueError("El nombre de usuario debe ser una cadena no vacía.")
        if not password or not isinstance(password, str):
            raise ValueError("La contraseña debe ser una cadena no vacía.")
        if not noUtilizaCredencialesPredeterminadas(password):
            raise ValueError("La contraseña no debe ser una credencial predeterminada.")
        if not contrasenaNoEstaEnTop10000(password):
            raise ValueError("La contraseña está en la lista de las peores contraseñas.")
        if not cumpleRequisitosLongitudYCaracteres(password):
            raise ValueError("La contraseña no cumple con los requisitos mínimos de longitud y caracteres permitidos.")
        self.username = username
        self.password = Contraseña(password)

    def cambiarContraseña(self, nueva_password):
        if not nueva_password or not isinstance(nueva_password, str):
            raise ValueError("La nueva contraseña debe ser una cadena no vacía.")
        if not noUtilizaCredencialesPredeterminadas(nueva_password):
            raise ValueError("La nueva contraseña no debe ser una credencial predeterminada.")
        if not contrasenaNoEstaEnTop10000(nueva_password):
            raise ValueError("La nueva contraseña está en la lista de las peores contraseñas.")
        if not cumpleRequisitosLongitudYCaracteres(nueva_password):
            raise ValueError("La nueva contraseña no cumple con los requisitos mínimos de longitud y caracteres permitidos.")
        self.password.cambiarContraseña(nueva_password)

    def __str__(self):
        return f"Usuario: {self.username}"
