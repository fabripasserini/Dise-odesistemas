"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/servicios/salas
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/salas/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/7: sala_mini_service.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/salas/sala_mini_service.py
# ================================================================================

from .sala_service import SalaService
from ...entidades.salas.sala import Sala

class SalaMiniService(SalaService):
    """Servicio específico para salas Mini."""
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        return precio_base * 0.8  # 20% de descuento


# ================================================================================
# ARCHIVO 3/7: sala_premium_service.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/salas/sala_premium_service.py
# ================================================================================

from .sala_service import SalaService
from ...entidades.salas.sala import Sala

class SalaPremiumService(SalaService):
    """Servicio específico para salas Premium."""
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        return precio_base * 1.5  # 50% de recargo


# ================================================================================
# ARCHIVO 4/7: sala_service.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/salas/sala_service.py
# ================================================================================

from abc import ABC, abstractmethod
from ...entidades.salas.sala import Sala

class SalaService(ABC):
    """Interfaz para servicios de gestión de salas."""
    @abstractmethod
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        """Calcula el precio final de una entrada para esta sala."""
        pass


# ================================================================================
# ARCHIVO 5/7: sala_service_registry.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/salas/sala_service_registry.py
# ================================================================================

from ...patrones.singleton import singleton
from .sala_service import SalaService
from .sala_mini_service import SalaMiniService
from .sala_standard_service import SalaStandardService
from .sala_premium_service import SalaPremiumService
from .sala_vip_service import SalaVipService

@singleton
class SalaServiceRegistry:
    """Registro Singleton para los servicios de salas."""
    def __init__(self):
        self._servicios = {
            "mini": SalaMiniService(),
            "standard": SalaStandardService(),
            "premium": SalaPremiumService(),
            "vip": SalaVipService()
        }

    def get_service(self, tipo_sala: str) -> SalaService:
        """Obtiene el servicio para un tipo de sala específico."""
        tipo_sala_key = tipo_sala.split(' ')[0].lower()
        service = self._servicios.get(tipo_sala_key)
        if not service:
            raise ValueError(f"No se encontró servicio para el tipo de sala: {tipo_sala}")
        return service


# ================================================================================
# ARCHIVO 6/7: sala_standard_service.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/salas/sala_standard_service.py
# ================================================================================

from .sala_service import SalaService
from ...entidades.salas.sala import Sala

class SalaStandardService(SalaService):
    """Servicio específico para salas Standard."""
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        return precio_base  # Precio sin modificar


# ================================================================================
# ARCHIVO 7/7: sala_vip_service.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/salas/sala_vip_service.py
# ================================================================================

from .sala_service import SalaService
from ...entidades.salas.sala import Sala

class SalaVipService(SalaService):
    """Servicio específico para salas VIP."""
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        return precio_base * 2.0  # 100% de recargo


