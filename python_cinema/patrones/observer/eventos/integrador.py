"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/patrones/observer/eventos
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/observer/eventos/__init__.py
# ================================================================================

from .evento_sensor import EventoSensor
from .evento_complejo import EventoComplejo


# ================================================================================
# ARCHIVO 2/3: evento_complejo.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/observer/eventos/evento_complejo.py
# ================================================================================

from dataclasses import dataclass

@dataclass
class EventoComplejo:
    """Datos de evento de un complejo."""
    id_complejo: int
    mensaje: str


# ================================================================================
# ARCHIVO 3/3: evento_sensor.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/observer/eventos/evento_sensor.py
# ================================================================================

from dataclasses import dataclass

@dataclass
class EventoSensor:
    """Datos de evento de un sensor de mercado."""
    tipo_sensor: str
    valor: float
    unidad: str


