from .sala import Sala

class SalaMini(Sala):
    """Sala de tipo Mini."""
    def obtener_tipo(self) -> str:
        return "Mini"
