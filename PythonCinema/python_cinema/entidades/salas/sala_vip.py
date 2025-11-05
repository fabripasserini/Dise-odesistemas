from .sala import Sala
from ...excepciones.snacks_agotados_exception import SnacksAgotadosException

class SalaVip(Sala):
    """Sala de tipo VIP con servicios adicionales."""
    def __init__(self, id_sala: int, capacidad: int, precio_base: float, snacks_incluidos: int):
        super().__init__(id_sala, capacidad, precio_base)
        self.snacks_disponibles = snacks_incluidos

    def obtener_tipo(self) -> str:
        return "VIP"

    def consumir_snack(self):
        """Consume un snack de la reserva de la sala."""
        if self.snacks_disponibles > 0:
            self.snacks_disponibles -= 1
        else:
            raise SnacksAgotadosException()
