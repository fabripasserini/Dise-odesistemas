from .sala import Sala

class SalaStandard(Sala):
    """Sala de tipo Standard."""
    def obtener_tipo(self) -> str:
        return "Standard"
