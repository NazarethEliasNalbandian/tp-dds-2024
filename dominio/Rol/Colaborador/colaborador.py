from typing import List
from dominio.Rol.Colaborador.Colaboracion.colaboracion import Colaboracion
from dominio.Rol.rol import Rol


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