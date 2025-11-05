"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/servicios/negocio
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/negocio/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: cadena_de_cines_service.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/negocio/cadena_de_cines_service.py
# ================================================================================

from ..infraestructura.edificio_service import EdificioService
from ..infraestructura.complejo_service import ComplejoService
from ..infraestructura.registro_comercial_service import RegistroComercialService
from ...entidades.infraestructura.registro_comercial import RegistroComercial

class CadenaDeCinesService:
    """Servicio de alto nivel para orquestar las operaciones de la cadena de cines."""
    def __init__(self):
        self.edificio_service = EdificioService()
        self.complejo_service = ComplejoService()
        self.registro_service = RegistroComercialService()
        self.registro_comercial: RegistroComercial = self.registro_service.crear_registro("Python Cinemas")

    def construir_nuevo_complejo(self, id_complejo: int, nombre: str, direccion: str, superficie: float):
        """Construye un edificio y crea un complejo en él."""
        print(f"--- Iniciando construcción del complejo '{nombre}' ---")
        edificio = self.edificio_service.construir_edificio(direccion, superficie)
        complejo = self.complejo_service.crear_complejo(id_complejo, nombre, edificio)
        self.registro_service.registrar_complejo(self.registro_comercial, complejo)
        print("--- Construcción finalizada ---")
        return complejo


# ================================================================================
# ARCHIVO 3/3: grupo_cierre.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/negocio/grupo_cierre.py
# ================================================================================

from typing import List, TypeVar, Generic

T = TypeVar('T')

class GrupoCierre(Generic[T]):
    """Clase genérica para agrupar elementos para una operación de cierre."""
    def __init__(self, nombre_grupo: str):
        self.nombre_grupo = nombre_grupo
        self.elementos: List[T] = []

    def agregar_elemento(self, elemento: T):
        self.elementos.append(elemento)

    def procesar_grupo(self):
        print(f"Procesando grupo de cierre '{self.nombre_grupo}' con {len(self.elementos)} elementos.")


