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
