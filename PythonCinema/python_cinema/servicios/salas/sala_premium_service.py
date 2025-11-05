from .sala_service import SalaService
from ...entidades.salas.sala import Sala

class SalaPremiumService(SalaService):
    """Servicio específico para salas Premium."""
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        return precio_base * 1.5  # 50% de recargo
