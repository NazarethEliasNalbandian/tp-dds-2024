import folium

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from dominio.Heladeraa.heladera import Heladera
from dominio.Ubicacion.ubicacion import Ubicacion

ubicacion1 = Ubicacion(-34.603722, -58.381592, "Av. Corrientes 123", "Oficina principal")
ubicacion2 = Ubicacion(-34.6083, -58.3712, "Plaza de Mayo", "Centro histórico")
ubicacion3 = Ubicacion(-34.6158, -58.4333, "Caballito", "Barrio residencial")

heladera1 = Heladera(ubicacion1, 300, "2023-01-01")
heladera2 = Heladera(ubicacion2, 200, "2023-06-15")
heladera3 = Heladera(ubicacion3, 150, "2022-12-01")

heladeras = [heladera1, heladera2, heladera3]

# Crear el mapa centrado en una ubicación general
mapa = folium.Map(location=[-34.603722, -58.381592], zoom_start=13)

# Agregar marcadores para cada heladera
for heladera in heladeras:
    folium.Marker(
        location=[heladera.ubicacion.latitud, heladera.ubicacion.longitud],
        popup=f"{heladera.puntoEstrategico}<br>{heladera.ubicacion.descripcion}",
        tooltip="Click para más info",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(mapa)

# Guardar el mapa en un archivo HTML
mapa.save("mapaInteractivo/mapa_heladeras.html")

print("Mapa generado: 'mapa_heladeras.html'")
