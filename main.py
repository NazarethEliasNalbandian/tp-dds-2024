from dominio.Heladera.Vianda.comida import Comida
from dominio.Heladera.Vianda.vianda import Vianda
from dominio.Heladera.heladera import Heladera
from dominio.Persona.MedioContacto.medioContacto import MedioDeContacto
from dominio.Persona.MedioContacto.tipoMedioContacto import TipoMedioDeContacto
from dominio.Persona.PersonaHumana.personaHumana import PersonaHumana
from dominio.Persona.PersonaJuridica.personaJuridica import PersonaJuridica
from dominio.Persona.PersonaJuridica.rubro import Rubro
from dominio.Persona.PersonaJuridica.tipoPersonaJuridico import TipoPersonaJuridica
from dominio.Rol.Colaborador.Colaboracion.DonacionDinero.donacionDinero import DonacionDinero
from dominio.Rol.Colaborador.Colaboracion.DonacionVianda.donacionVianda import DonacionVianda
from dominio.Rol.Colaborador.colaborador import Colaborador
from dominio.Ubicacion.ubicacion import Ubicacion

def crearPersonaHumana():
    rol_colaborador = Colaborador()

    medios_contacto_humana = [
        MedioDeContacto(TipoMedioDeContacto.EMAIL, "juan.perez@example.com"),
        MedioDeContacto(TipoMedioDeContacto.TELEFONO, "123456789")
    ]
    persona_humana = PersonaHumana("Juan", "Pérez", rol_colaborador, medios_contacto_humana, "Calle Falsa 123", "01/01/1990")

    donacion_dinero = DonacionDinero(500, "2025-01-02")
    
    ubicacionHeladera = Ubicacion(-34.603722, -58.381592, "Av. Corrientes 123", "Oficina principal")
    heladera_de_vianda = Heladera(ubicacionHeladera, 5, "2024-01-02") 
    pizza = Comida("pizza", "2026-01-02")
    vianda_para_donar = Vianda(pizza, heladera_de_vianda)
    donacion_vianda = DonacionVianda(vianda_para_donar,"2025-01-03", rol_colaborador, disponible=False)

    rol_colaborador.agregar_colaboracion(donacion_dinero)

    try:
        rol_colaborador.agregar_colaboracion(donacion_vianda)
    except PermissionError as e:
        print(e)

    print(persona_humana.mostrar_informacion())
    print(rol_colaborador.descripcion())
    print(rol_colaborador.actuar())

def crearPersonaJuridica():
    rol_colaborador = Colaborador()
    
    medios_contacto_juridica = [MedioDeContacto(TipoMedioDeContacto.EMAIL, "empresa@example.com")]
    rubro = Rubro("Tecnología")
    persona_juridica = PersonaJuridica("TechCorp", TipoPersonaJuridica.EMPRESA, rubro, rol_colaborador, medios_contacto_juridica, "Av. Siempre Viva 742")

    print(persona_juridica.mostrar_informacion())
    
if __name__ == "__main__":
    crearPersonaHumana()