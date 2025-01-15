import requests
from dataclasses import dataclass
from typing import List

from dominio.APIAdapter import IAdapterRecomendadorPuntos
from dominio.Espacio.ubicacion import Ubicacion
from dominio.Espacio.zona import Zona

@dataclass
class APIRecomendadorPuntos(IAdapterRecomendadorPuntos):
    api_url: str

    def realizarRecomendacion(self, zona: Zona) -> List[Ubicacion]:
        """Realiza una solicitud a una API externa para obtener recomendaciones de ubicación."""
        
        params = {
            'latitud': zona.ubicacion.latitud,
            'longitud': zona.ubicacion.longitud,
            'radio': zona.radio
        }
        
        response = requests.get(self.api_url, params=params)
        
        response.raise_for_status()
        
        ubicaciones_recomendadas = []
        for item in response.json():
            ubicacion = Ubicacion(
                direccion=item['direccion'],
                latitud=item['latitud'],
                longitud=item['longitud']
            )
            ubicaciones_recomendadas.append(ubicacion)
        
        return ubicaciones_recomendadas
