from dataclasses import dataclass

@dataclass
class EventoSensor:
    """Datos de evento de un sensor de mercado."""
    tipo_sensor: str
    valor: float
    unidad: str
