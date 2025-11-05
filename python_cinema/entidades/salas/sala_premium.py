from .sala import Sala
from .tecnologia_premium import TecnologiaPremium

class SalaPremium(Sala):
    """Sala de tipo Premium con tecnología especial."""
    def __init__(self, id_sala: int, capacidad: int, precio_base: float, tecnologia: TecnologiaPremium):
        super().__init__(id_sala, capacidad, precio_base)
        self.tecnologia = tecnologia

    def obtener_tipo(self) -> str:
        return f"Premium ({self.tecnologia.value})"
