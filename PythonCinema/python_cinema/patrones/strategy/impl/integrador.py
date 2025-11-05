"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/patrones/strategy/impl
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: venta_constante_strategy.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/strategy/impl/venta_constante_strategy.py
# ================================================================================

from ..venta_entradas_strategy import VentaEntradasStrategy

class VentaConstanteStrategy(VentaEntradasStrategy):
    """Estrategia de precios constantes, ignora la demanda."""
    def calcular_precio(self, precio_base: float, factor_demanda: float) -> float:
        print("Aplicando estrategia de precios constantes.")
        return precio_base


# ================================================================================
# ARCHIVO 3/3: venta_estacional_strategy.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/strategy/impl/venta_estacional_strategy.py
# ================================================================================

from ..venta_entradas_strategy import VentaEntradasStrategy

class VentaEstacionalStrategy(VentaEntradasStrategy):
    """Estrategia de precios que varía con la demanda."""
    def calcular_precio(self, precio_base: float, factor_demanda: float) -> float:
        # factor_demanda es un % (ej: 1.2 para 120% de demanda)
        precio_ajustado = precio_base * factor_demanda
        print(f"Aplicando estrategia estacional. Demanda: {factor_demanda:.2f}, Precio ajustado: ${precio_ajustado:.2f}")
        return precio_ajustado


