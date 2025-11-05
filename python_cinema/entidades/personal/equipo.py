from typing import List
from .empleado import Empleado

class Equipo:
    """Representa un equipo de trabajo asignado a un complejo o área."""
    def __init__(self, nombre_equipo: str):
        self.nombre_equipo = nombre_equipo
        self.miembros: List[Empleado] = []

    def agregar_miembro(self, empleado: Empleado):
        self.miembros.append(empleado)
