from abc import ABC, abstractmethod
from ...entidades.salas.sala import Sala

class SalaService(ABC):
    """Interfaz para servicios de gestión de salas."""
    @abstractmethod
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        """Calcula el precio final de una entrada para esta sala."""
        pass
