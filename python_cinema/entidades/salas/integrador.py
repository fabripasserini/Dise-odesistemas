"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/entidades/salas
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/salas/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/7: sala.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/salas/sala.py
# ================================================================================

from abc import ABC, abstractmethod

class Sala(ABC):
    """Clase base abstracta para una sala de cine."""
    def __init__(self, id_sala: int, capacidad: int, precio_base: float):
        self.id_sala = id_sala
        self.capacidad = capacidad
        self.precio_base = precio_base

    @abstractmethod
    def obtener_tipo(self) -> str:
        """Devuelve el tipo de sala."""
        pass

    def __str__(self) -> str:
        return f"Sala {self.obtener_tipo()} (ID: {self.id_sala}, Capacidad: {self.capacidad})"


# ================================================================================
# ARCHIVO 3/7: sala_mini.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/salas/sala_mini.py
# ================================================================================

from .sala import Sala

class SalaMini(Sala):
    """Sala de tipo Mini."""
    def obtener_tipo(self) -> str:
        return "Mini"


# ================================================================================
# ARCHIVO 4/7: sala_premium.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/salas/sala_premium.py
# ================================================================================

from .sala import Sala
from .tecnologia_premium import TecnologiaPremium

class SalaPremium(Sala):
    """Sala de tipo Premium con tecnología especial."""
    def __init__(self, id_sala: int, capacidad: int, precio_base: float, tecnologia: TecnologiaPremium):
        super().__init__(id_sala, capacidad, precio_base)
        self.tecnologia = tecnologia

    def obtener_tipo(self) -> str:
        return f"Premium ({self.tecnologia.value})"


# ================================================================================
# ARCHIVO 5/7: sala_standard.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/salas/sala_standard.py
# ================================================================================

from .sala import Sala

class SalaStandard(Sala):
    """Sala de tipo Standard."""
    def obtener_tipo(self) -> str:
        return "Standard"


# ================================================================================
# ARCHIVO 6/7: sala_vip.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/salas/sala_vip.py
# ================================================================================

from .sala import Sala
from ...excepciones.snacks_agotados_exception import SnacksAgotadosException

class SalaVip(Sala):
    """Sala de tipo VIP con servicios adicionales."""
    def __init__(self, id_sala: int, capacidad: int, precio_base: float, snacks_incluidos: int):
        super().__init__(id_sala, capacidad, precio_base)
        self.snacks_disponibles = snacks_incluidos

    def obtener_tipo(self) -> str:
        return "VIP"

    def consumir_snack(self):
        """Consume un snack de la reserva de la sala."""
        if self.snacks_disponibles > 0:
            self.snacks_disponibles -= 1
        else:
            raise SnacksAgotadosException()


# ================================================================================
# ARCHIVO 7/7: tecnologia_premium.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/salas/tecnologia_premium.py
# ================================================================================

from enum import Enum

class TecnologiaPremium(Enum):
    """Enumeración de tecnologías para salas Premium."""
    IMAX = "IMAX"
    DOLBY_ATMOS = "Dolby Atmos"
    SCREENX = "ScreenX"


