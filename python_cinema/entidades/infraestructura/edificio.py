from dataclasses import dataclass

@dataclass
class Edificio:
    """Representa un edificio físico."""
    direccion: str
    superficie_total: float
