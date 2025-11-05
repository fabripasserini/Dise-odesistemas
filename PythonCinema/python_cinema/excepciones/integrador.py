"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/excepciones
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/excepciones/__init__.py
# ================================================================================

from .cinema_exception import CinemaException
from .superficie_insuficiente_exception import SuperficieInsuficienteException
from .snacks_agotados_exception import SnacksAgotadosException
from .persistencia_exception import PersistenciaException
from .mensajes_exception import MensajesException


# ================================================================================
# ARCHIVO 2/6: cinema_exception.py
# Ruta: /home/fabri/PythonCinema/python_cinema/excepciones/cinema_exception.py
# ================================================================================

class CinemaException(Exception):
    """Excepción base para la aplicación PythonCinema."""
    def __init__(self, message="Ha ocurrido un error en la aplicación de cine."):
        self.message = message
        super().__init__(self.message)


# ================================================================================
# ARCHIVO 3/6: mensajes_exception.py
# Ruta: /home/fabri/PythonCinema/python_cinema/excepciones/mensajes_exception.py
# ================================================================================

from .cinema_exception import CinemaException

class MensajesException(CinemaException):
    """Lanzada para errores relacionados con el sistema de mensajería."""
    def __init__(self, message="Error en el sistema de mensajes."):
        self.message = message
        super().__init__(self.message)


# ================================================================================
# ARCHIVO 4/6: persistencia_exception.py
# Ruta: /home/fabri/PythonCinema/python_cinema/excepciones/persistencia_exception.py
# ================================================================================

from .cinema_exception import CinemaException

class PersistenciaException(CinemaException):
    """Lanzada en caso de errores de guardado o carga de datos."""
    def __init__(self, message="Error durante la persistencia de datos."):
        self.message = message
        super().__init__(self.message)


# ================================================================================
# ARCHIVO 5/6: snacks_agotados_exception.py
# Ruta: /home/fabri/PythonCinema/python_cinema/excepciones/snacks_agotados_exception.py
# ================================================================================

from .cinema_exception import CinemaException

class SnacksAgotadosException(CinemaException):
    """Lanzada cuando no hay más snacks disponibles en una sala VIP."""
    def __init__(self, message="Los snacks para esta sala se han agotado."):
        self.message = message
        super().__init__(self.message)


# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /home/fabri/PythonCinema/python_cinema/excepciones/superficie_insuficiente_exception.py
# ================================================================================

from .cinema_exception import CinemaException

class SuperficieInsuficienteException(CinemaException):
    """Lanzada cuando no hay suficiente superficie para construir."""
    def __init__(self, message="La superficie disponible es insuficiente para la operación solicitada."):
        self.message = message
        super().__init__(self.message)


