from abc import ABC, abstractmethod
from typing import List

from dominio.Espacio.ubicacion import Ubicacion
from dominio.Espacio.zona import Zona

# Asumiendo que Zona y Ubicacion son clases previamente definidas y que están importadas adecuadamente aquí.
# from dominio.ubicacion import Zona, Ubicacion  # Ejemplo de cómo podrían importarse

class IAdapterRecomendadorPuntos(ABC):
    @abstractmethod
    def realizarRecomendacion(self, zona: Zona) -> List[Ubicacion]:
        """
        Método abstracto para realizar una recomendación de puntos basada en la zona dada.

        Args:
        - zona (Zona): La zona dentro de la cual se realizará la recomendación.

        Returns:
        - List[Ubicacion]: Una lista de objetos Ubicacion recomendados dentro de la zona especificada.

        Este método debe ser implementado por cualquier clase que herede de IAdapterRecomendadorPuntos,
        proporcionando lógica específica para recomendar ubicaciones basada en algún criterio o algoritmo
        aplicado a la zona dada.
        """
        pass
