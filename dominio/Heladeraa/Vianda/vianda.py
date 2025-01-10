from dominio.Heladeraa.Vianda.comida import Comida
from dominio.Heladeraa.heladera import Heladera

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
