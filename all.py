from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import List
from dominio.Persona.MedioContacto.tipoMedioContacto import TipoMedioDeContacto
from dominio.Persona.PersonaJuridica.rubro import Rubro
from dominio.Persona.PersonaJuridica.tipoPersonaJuridico import TipoPersonaJuridica
from dominio.Persona.persona import Persona
from dominio.Rol.Colaborador.Colaboracion.DistribucionVianda.distribucionVianda import DistribucionVianda
from dominio.Rol.Colaborador.Colaboracion.DonacionDinero.donacionDinero import DonacionDinero
from dominio.Rol.Colaborador.Colaboracion.DonacionVianda.donacionVianda import DonacionVianda
from dominio.Rol.Colaborador.Colaboracion.HacerseCargoHeladera.hacerseCargoHeladera import HacerCargoHeladera
from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion
from dominio.Rol.Colaborador.colaborador import Colaborador
from dominio.Rol.rol import Rol
from dominio.Ubicacion.ubicacion import Ubicacion
from dominio.Vianda.comida import Comida
from dominio.Vianda.vianda import Vianda


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
        from dominio.Vianda.vianda import Vianda
        
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

class Persona(ABC):
    def __init__(self, nombre, rol, direccion=None):
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre es obligatorio y debe ser una cadena.")
        if not isinstance(rol, Rol):
            raise ValueError("El rol debe ser una instancia de la clase Rol o sus derivados.")
        self.nombre = nombre
        self.rol = rol
        self.direccion = direccion

    @abstractmethod
    def mostrar_informacion(self):
        pass
    
class PersonaHumana(Persona):
    def __init__(self, nombre, apellido, rol, medios_contacto, direccion=None, fecha_nacimiento=None):
        super().__init__(nombre, rol, direccion)
        if not apellido or not isinstance(apellido, str):
            raise ValueError("El apellido es obligatorio y debe ser una cadena.")
        if not isinstance(medios_contacto, list) or not all(isinstance(medio, MedioDeContacto) for medio in medios_contacto):
            raise ValueError("Los medios de contacto deben ser una lista de instancias de MedioDeContacto.")
        self.apellido = apellido
        self.medios_contacto = medios_contacto
        self.fecha_nacimiento = fecha_nacimiento
        
        if isinstance(rol, Colaborador):
            for colaboracion in rol.colaboraciones:
                ## Si es DonacionDinero o HacerCargoHeladera y no esta disponible, tira error
                if isinstance(colaboracion, DonacionDinero) or isinstance(colaboracion, DistribucionVianda) or isinstance(colaboracion, DonacionVianda):
                    if not colaboracion.disponible:
                        raise ValueError("Las colaboraciones de tipo DonacionDinero o HacerCargoHeladera deben tener disponible=True para este rol.")
                else: 
                    if colaboracion.disponible:
                        raise ValueError("Las colaboraciones distintas de DonacionDinero o HacerCargoHeladera no pueden tener disponible=True para este rol.")

    def mostrar_informacion(self):
        info = f"Nombre: {self.nombre} {self.apellido}, "
        info += f"Rol: {self.rol.descripcion()}, "
        ## valor1 if condicion1 else valor2
        info += f"Dirección: {self.direccion if self.direccion else 'No especificada'}, " 
        ## funcion(elemento) for elemento in lista) Aplico una funcion a cada elemento de una lista
        ## delimitador.join(listaDeStrings)
        info += f"Medios de contacto: {', '.join(str(medio) for medio in self.medios_contacto)}, " 
        info += f"Fecha de nacimiento: {self.fecha_nacimiento if self.fecha_nacimiento else 'No especificada'}"
        return info

class PersonaJuridica(Persona):
    def __init__(self, nombre, tipo, rubro, rol, medios_contacto, direccion=None):
        super().__init__(nombre, rol, direccion)
        if not isinstance(tipo, TipoPersonaJuridica):
            raise ValueError("El tipo debe ser una instancia de TipoPersonaJuridica.")
        if not isinstance(rubro, Rubro):
            raise ValueError("El rubro debe ser una instancia de la clase Rubro.")
        if not medios_contacto or not isinstance(medios_contacto, list) or not all(isinstance(medio, MedioDeContacto) for medio in medios_contacto):
            raise ValueError("Debe proporcionar al menos un medio de contacto válido.")
        self.tipo = tipo
        self.rubro = rubro
        self.medios_contacto = medios_contacto
        
        if isinstance(rol, Colaborador):
            for colaboracion in rol.colaboraciones:
                ## Si es DonacionDinero o HacerCargoHeladera y no esta disponible, tira error
                if isinstance(colaboracion, DonacionDinero) or isinstance(colaboracion, HacerCargoHeladera):
                    if not colaboracion.disponible:
                        raise ValueError("Las colaboraciones de tipo DonacionDinero o HacerCargoHeladera deben tener disponible=True para este rol.")
                else: 
                    if colaboracion.disponible:
                        raise ValueError("Las colaboraciones distintas de DonacionDinero o HacerCargoHeladera no pueden tener disponible=True para este rol.")

    def mostrar_informacion(self):
        info = f"Nombre: {self.nombre}, "
        info += f"Tipo: {self.tipo.value}, "
        info += f"Rubro: {self.rubro}, "
        info += f"Rol: {self.rol.descripcion()}, "
        info += f"Dirección: {self.direccion if self.direccion else 'No especificada'}, "
        info += f"Medios de contacto: {', '.join(str(medio) for medio in self.medios_contacto)}"
        return info

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


class TipoMedioDeContacto(Enum):
    WHATSAPP = "whatsapp"
    EMAIL = "email"
    TELEFONO = "telefono"

class Rubro:
    def __init__(self, descripcion):
        if not descripcion or not isinstance(descripcion, str):
            raise ValueError("La descripción del rubro debe ser una cadena no vacía.")
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion

class TipoPersonaJuridica(Enum):
    GUBERNAMENTAL = "Gubernamental"
    ONG = "ONG"
    EMPRESA = "Empresa"
    INSTITUCION = "Institución"


class Rol(ABC):
    @abstractmethod
    def descripcion(self):
        pass

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

class Colaborador(Rol):
    def __init__(self):
        self.colaboraciones: List[Colaboracion] = []

    def agregar_colaboracion(self, colaboracion):
        if not isinstance(colaboracion, Colaboracion):
            raise ValueError("La colaboración debe ser una instancia de la clase Colaboracion o sus derivados.")
        self.colaboraciones.append(colaboracion)
    
    def remover_colaboracion(self, colaboracion):
        if isinstance(colaboracion, int):  # Si se pasa un índice
            if colaboracion < 0 or colaboracion >= len(self.colaboraciones):
                raise IndexError("Índice de colaboración fuera de rango.")
            del self.colaboraciones[colaboracion]
        elif isinstance(colaboracion, Colaboracion):  # Si se pasa una instancia
            try:
                self.colaboraciones.remove(colaboracion)
            except ValueError:
                raise ValueError("La colaboración especificada no se encuentra en la lista.")
        else:
            raise ValueError("Debe proporcionar un índice o una instancia de Colaboracion para eliminar.")
    
    def actuar(self):
        resultados = []
        for colaboracion in self.colaboraciones:
            resultado = colaboracion.ejecutar()
            resultados.append(resultado)
        return resultados

class Colaboracion(ABC):
    def __init__(self, disponible):
        if not isinstance(disponible, bool):
            raise ValueError("El atributo disponible debe ser un booleano.")
        self.disponible = disponible

    @abstractmethod
    def detalle(self):
        pass
    
    @abstractmethod
    def ejecutar(self):
        pass

class HacerCargoHeladera(Colaboracion):
    def __init__(self, tiempo, disponible=True):
        super().__init__(disponible)
        if not isinstance(tiempo, int) or tiempo <= 0:
            raise ValueError("El tiempo debe ser un número entero positivo representando días.")
        self.tiempo = tiempo

    def detalle(self):
        if not self.disponible:
            return "Este colaborador no puede realizar esta tarea."
        return f"Uso de heladera por {self.tiempo} días"
    
    def ejecutar(self):
        return self.detalle()

class DonacionVianda(Colaboracion):
    def __init__(self, vianda, fecha_donacion, colaborador, disponible=True):
        super().__init__(disponible)
        if not isinstance(vianda, Vianda):
            raise ValueError("La vianda debe ser una instancia de la clase Vianda.")
        if not isinstance(fecha_donacion, str) or not fecha_donacion:
            raise ValueError("La fecha de donación debe ser una cadena no vacía.")
        if not isinstance(colaborador, Colaborador):
            raise ValueError("El colaborador debe ser una instancia de la clase Colaborador.")
        self.vianda = vianda
        self.fecha_donacion = fecha_donacion
        self.colaborador = colaborador

    def detalle(self):
        if not self.disponible:
            return "Este colaborador no puede realizar esta tarea."
        return f"Donación de Vianda: {self.vianda}, Fecha: {self.fecha_donacion}, Colaborador: {self.colaborador.descripcion()}"
    
    def ejecutar(self):
        return self.detalle()

class DonacionDinero(Colaboracion):
    def __init__(self, monto, fechaDonacion, disponible=True, frecuencia = None):
        super().__init__(disponible)
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("El monto debe ser un número positivo.")
        self.monto = monto
        self.fechaDonacion = fechaDonacion
        self.frecuencia = frecuencia

    def detalle(self):
        if not self.disponible:
            return "Este colaborador no puede realizar esta tarea."
        return f"Donación de dinero: ${self.monto:.2f}"
    
    def ejecutar(self):
        return self.detalle()

class DistribucionVianda(Colaboracion):
    def __init__(self, heladera_origen, heladera_destino, cantidad_viandas, motivo, fecha, disponible=True):
        super().__init__(disponible)
        if not isinstance(heladera_origen, Heladera):
            raise ValueError("La heladera de origen debe ser una instancia de la clase Heladera.")
        if not isinstance(heladera_destino, Heladera):
            raise ValueError("La heladera de destino debe ser una instancia de la clase Heladera.")
        if not isinstance(cantidad_viandas, int) or cantidad_viandas <= 0:
            raise ValueError("La cantidad de viandas debe ser un número entero positivo.")
        if not isinstance(motivo, str) or not motivo:
            raise ValueError("El motivo debe ser una cadena no vacía.")
        if not isinstance(fecha, str) or not fecha:
            raise ValueError("La fecha debe ser una cadena no vacía.")
        
        self.heladera_origen = heladera_origen
        self.heladera_destino = heladera_destino
        self.cantidad_viandas = cantidad_viandas
        self.motivo = motivo
        self.fecha = fecha

    def detalle(self):
        if not self.disponible:
            return "Este colaborador no puede realizar esta tarea."
        return (f"Distribución de viandas: {self.cantidad_viandas} unidades\n"
                f"Heladera Origen: {self.heladera_origen}\n"
                f"Heladera Destino: {self.heladera_destino}\n"
                f"Motivo: {self.motivo}\n"
                f"Fecha: {self.fecha}")
    
    def ejecutar(self):
        return self.detalle()

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

class Vianda:
    def __init__(self, comida, heladera, peso=None, entregada=False):
        if not isinstance(comida, Comida):
            raise ValueError("La comida debe ser una instancia de la clase Comida.")
        if not isinstance(heladera, Heladera):
            raise ValueError("La heladera debe ser una instancia de la clase Heladera.")
        if peso is not None and (not isinstance(peso, (int, float)) or peso <= 0):
            raise ValueError("El peso debe ser un número positivo o None.")
        if not isinstance(entregada, bool):
            raise ValueError("El atributo 'entregada' debe ser un booleano.")
        
        self.comida = comida
        self.heladera = heladera
        self.peso = peso
        self.entregada = entregada

    def __str__(self):
        peso_str = f", Peso: {self.peso}kg" if self.peso else ""
        estado_entrega = "Entregada" if self.entregada else "No entregada"
        return f"Vianda: [Comida: {self.comida}, Heladera: {self.heladera}{peso_str}, Estado: {estado_entrega}]"

class Comida:
    def __init__(self, nombre, fechaCaducidad, calorias = None):
        # Validaciones básicas para los atributos
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(calorias, (int, float)) or calorias < 0:
            raise ValueError("Las calorías deben ser un número positivo.")
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