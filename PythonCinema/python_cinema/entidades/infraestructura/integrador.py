"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/entidades/infraestructura
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/infraestructura/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: complejo.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/infraestructura/complejo.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: edificio.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/infraestructura/edificio.py
# ================================================================================

from dataclasses import dataclass

@dataclass
class Edificio:
    """Representa un edificio físico."""
    direccion: str
    superficie_total: float


# ================================================================================
# ARCHIVO 4/4: registro_comercial.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/infraestructura/registro_comercial.py
# ================================================================================

from typing import List
from .complejo import Complejo

class RegistroComercial:
    """Representa el registro de todos los complejos de una cadena de cines."""
    def __init__(self, nombre_cadena: str):
        self.nombre_cadena = nombre_cadena
        self.complejos: List[Complejo] = []

    def agregar_complejo(self, complejo: Complejo):
        self.complejos.append(complejo)


