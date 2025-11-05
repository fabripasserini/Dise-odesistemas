from .sala_service import SalaService
from ...entidades.salas.sala import Sala

class SalaMiniService(SalaService):
    """Servicio específico para salas Mini."""
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        return precio_base * 0.8  # 20% de descuento
