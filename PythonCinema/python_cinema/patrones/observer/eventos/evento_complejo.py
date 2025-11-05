from dataclasses import dataclass

@dataclass
class EventoComplejo:
    """Datos de evento de un complejo."""
    id_complejo: int
    mensaje: str
