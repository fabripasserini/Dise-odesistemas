"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/entidades/personal
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: certificado_manipulacion.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/personal/certificado_manipulacion.py
# ================================================================================

from dataclasses import dataclass
from datetime import date

@dataclass
class CertificadoManipulacionAlimentos:
    """Certificado necesario para manipular alimentos."""
    fecha_emision: date
    fecha_vencimiento: date


# ================================================================================
# ARCHIVO 3/5: empleado.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/personal/empleado.py
# ================================================================================

from dataclasses import dataclass
from typing import Optional
from .turno import Turno
from .certificado_manipulacion import CertificadoManipulacionAlimentos

@dataclass
class Empleado:
    """Representa a un empleado del cine."""
    nombre: str
    apellido: str
    turno: Turno
    certificado: Optional[CertificadoManipulacionAlimentos] = None


# ================================================================================
# ARCHIVO 4/5: equipo.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/personal/equipo.py
# ================================================================================

from typing import List
from .empleado import Empleado

class Equipo:
    """Representa un equipo de trabajo asignado a un complejo o área."""
    def __init__(self, nombre_equipo: str):
        self.nombre_equipo = nombre_equipo
        self.miembros: List[Empleado] = []

    def agregar_miembro(self, empleado: Empleado):
        self.miembros.append(empleado)


# ================================================================================
# ARCHIVO 5/5: turno.py
# Ruta: /home/fabri/PythonCinema/python_cinema/entidades/personal/turno.py
# ================================================================================

from enum import Enum

class Turno(Enum):
    """Turnos de trabajo para empleados."""
    MANANA = "Mañana"
    TARDE = "Tarde"
    NOCHE = "Noche"


