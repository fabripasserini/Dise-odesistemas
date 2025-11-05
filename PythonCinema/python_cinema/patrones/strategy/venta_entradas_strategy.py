from abc import ABC, abstractmethod

class VentaEntradasStrategy(ABC):
    """Interfaz para el Strategy de cálculo de precios de venta."""
    @abstractmethod
    def calcular_precio(self, precio_base: float, factor_demanda: float) -> float:
        """Calcula el precio final basado en la demanda."""
        pass
