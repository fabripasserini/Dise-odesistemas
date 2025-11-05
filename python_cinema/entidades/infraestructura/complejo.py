from typing import List
from ..salas.sala import Sala
from .edificio import Edificio

class Complejo:
    """Representa un complejo de cines, que contiene varias salas."""
    def __init__(self, id_complejo: int, nombre: str, edificio: Edificio):
        self.id_complejo = id_complejo
        self.nombre = nombre
        self.edificio = edificio
        self.salas: List[Sala] = []

    def agregar_sala(self, sala: Sala):
        self.salas.append(sala)

    def __str__(self) -> str:
        return f"Complejo '{self.nombre}' (ID: {self.id_complejo}) en {self.edificio.direccion}"
