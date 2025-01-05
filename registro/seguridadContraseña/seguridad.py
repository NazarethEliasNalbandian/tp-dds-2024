import unicodedata
import string
from registro.contraseña import Contraseña


def noUtilizaCredencialesPredeterminadas(password):
    credenciales_por_defecto = ["1234", "admin", "password", "123456"]
    return password not in credenciales_por_defecto

def contrasenaNoEstaEnTop10000(password):
    # Obtengo un objeto file que contiene los datos del archivo y se le pueden aplicar metodos
    # Al usar with, se cierra solo el archivo
    with open("top10000passwords.txt", "r") as file:
        # file.read() devuelve un string con el contenido del archivo
        # string.splitlines() devuelve una lista de strings separados por "\n"
        top_passwords = file.read().splitlines()
    return password not in top_passwords

def contrasenaNoEsPalabraDiccionario(password):
    with open("dictionary.txt", "r") as file:
        diccionario_palabras = file.read().splitlines()
    return password.lower() not in diccionario_palabras

def es_repetitiva_o_secuencial(password):
    # set(password) devuelve una lista con todos los elementos distintos de un Iterable
    # Si todos los elementos de password son iguales (mismo caracter), entonces set devolvera una lista de un solo elemento
    if len(set(password)) == 1:
        return True

    # Verificar si la contraseña es secuencial ascendente o descendente
    secuencia_ascendente = "0123456789abcdefghijklmnopqrstuvwxyz"
    secuencia_descendente = secuencia_ascendente[::-1] # secuencia[start:end:step], no aclaramos start y end (lista completa de inicio a fin)
    # [secuencia_ascendente, secuencia_descendente] Lista de dos elementos
    # for secuencia in [secuencia_ascendente, secuencia_descendente] Recorro esa lista comparando secuencia con cada elemento
    # Comparo segun esta condicion (password es una subcadena de secuencia): password in secuencia
    # Luego, va creando una lista de Boolean, si alguno es True, el any devuelve True
    if any(password in secuencia for secuencia in [secuencia_ascendente, secuencia_descendente]):
        return True

    return False

def cumpleRequisitosLongitudYCaracteres(password_obj):
    if not isinstance(password_obj, Contraseña):
        raise ValueError("El argumento debe ser una instancia de la clase Contraseña.")
    password = password_obj.password

    password = unicodedata.normalize("NFKC", password)

    if password_obj.longitud < 8:
        return False

    try:
        password.encode("utf-8")
    except UnicodeEncodeError:
        return False
    
    if es_repetitiva_o_secuencial(password):
        return False
    
    if not contrasenaNoEsPalabraDiccionario(password):
        return False

    return True