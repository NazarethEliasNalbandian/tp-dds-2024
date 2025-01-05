from dominio.Persona.MedioContacto.medioContacto import MedioDeContacto
from dominio.Persona.PersonaJuridica.rubro import Rubro
from dominio.Persona.PersonaJuridica.tipoPersonaJuridico import TipoPersonaJuridica
from dominio.Persona.persona import Persona
from dominio.Rol.Colaborador.Colaboracion.DonacionDinero.donacionDinero import DonacionDinero
from dominio.Rol.Colaborador.Colaboracion.HacerseCargoHeladera.hacerseCargoHeladera import HacerCargoHeladera
from dominio.Rol.Colaborador.colaborador import Colaborador


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