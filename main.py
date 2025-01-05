from dominio.Persona.MedioContacto.medioContacto import MedioDeContacto
from dominio.Persona.MedioContacto.tipoMedioContacto import TipoMedioDeContacto
from dominio.Persona.PersonaHumana.personaHumana import PersonaHumana
from dominio.Persona.PersonaJuridica.personaJuridica import PersonaJuridica
from dominio.Persona.PersonaJuridica.rubro import Rubro
from dominio.Persona.PersonaJuridica.tipoPersonaJuridico import TipoPersonaJuridica
from dominio.Rol.Colaborador.Colaboracion.DonacionDinero.donacionDinero import DonacionDinero
from dominio.Rol.Colaborador.Colaboracion.DonacionVianda.donacionVianda import DonacionVianda
from dominio.Rol.Colaborador.colaborador import Colaborador

def crearPersonaHumana():
    rol_colaborador = Colaborador()

    medios_contacto_humana = [
        MedioDeContacto(TipoMedioDeContacto.EMAIL, "juan.perez@example.com"),
        MedioDeContacto(TipoMedioDeContacto.TELEFONO, "123456789")
    ]
    persona_humana = PersonaHumana("Juan", "Pérez", rol_colaborador, medios_contacto_humana, "Calle Falsa 123", "01/01/1990")

    donacion_dinero = DonacionDinero(500)
    donacion_vianda = DonacionVianda(10, disponible=False)

    rol_colaborador.agregar_colaboracion(donacion_dinero)

    try:
        rol_colaborador.agregar_colaboracion(donacion_vianda)
    except PermissionError as e:
        print(e)

    print(persona_humana.mostrar_informacion())
    print(rol_colaborador.descripcion())

def crearPersonaJuridica():
    rol_colaborador = Colaborador()
    
    medios_contacto_juridica = [MedioDeContacto(TipoMedioDeContacto.EMAIL, "empresa@example.com")]
    rubro = Rubro("Tecnología")
    persona_juridica = PersonaJuridica("TechCorp", TipoPersonaJuridica.EMPRESA, rubro, rol_colaborador, medios_contacto_juridica, "Av. Siempre Viva 742")

    print(persona_juridica.mostrar_informacion())
    
if __name__ == "__main__":
    crearPersonaJuridica()