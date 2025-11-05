from typing import List
from .complejo import Complejo

class RegistroComercial:
    """Representa el registro de todos los complejos de una cadena de cines."""
    def __init__(self, nombre_cadena: str):
        self.nombre_cadena = nombre_cadena
        self.complejos: List[Complejo] = []

    def agregar_complejo(self, complejo: Complejo):
        self.complejos.append(complejo)
