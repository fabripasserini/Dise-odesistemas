"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/patrones/strategy
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: venta_entradas_strategy.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/strategy/venta_entradas_strategy.py
# ================================================================================

from abc import ABC, abstractmethod

class VentaEntradasStrategy(ABC):
    """Interfaz para el Strategy de cálculo de precios de venta."""
    @abstractmethod
    def calcular_precio(self, precio_base: float, factor_demanda: float) -> float:
        """Calcula el precio final basado en la demanda."""
        pass


