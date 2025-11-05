from .sala_service import SalaService
from ...entidades.salas.sala import Sala

class SalaVipService(SalaService):
    """Servicio específico para salas VIP."""
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        return precio_base * 2.0  # 100% de recargo
