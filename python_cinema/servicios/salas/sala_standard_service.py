from .sala_service import SalaService
from ...entidades.salas.sala import Sala

class SalaStandardService(SalaService):
    """Servicio específico para salas Standard."""
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        return precio_base  # Precio sin modificar
