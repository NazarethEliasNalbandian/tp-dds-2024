from dominio.Persona.MedioContacto.medioContacto import MedioDeContacto
from dominio.Persona.persona import Persona
from dominio.Rol.Colaborador.Colaboracion.DistribucionVianda.distribucionVianda import DistribucionVianda
from dominio.Rol.Colaborador.Colaboracion.DonacionDinero.donacionDinero import DonacionDinero
from dominio.Rol.Colaborador.Colaboracion.DonacionVianda.donacionVianda import DonacionVianda
from dominio.Rol.Colaborador.colaborador import Colaborador

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