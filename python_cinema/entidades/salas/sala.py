from abc import ABC, abstractmethod

class Sala(ABC):
    """Clase base abstracta para una sala de cine."""
    def __init__(self, id_sala: int, capacidad: int, precio_base: float):
        self.id_sala = id_sala
        self.capacidad = capacidad
        self.precio_base = precio_base

    @abstractmethod
    def obtener_tipo(self) -> str:
        """Devuelve el tipo de sala."""
        pass

    def __str__(self) -> str:
        return f"Sala {self.obtener_tipo()} (ID: {self.id_sala}, Capacidad: {self.capacidad})"
