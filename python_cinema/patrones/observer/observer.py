from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para el patrón Observer."""
    @abstractmethod
    def update(self, data: T) -> None:
        """Recibe la actualización del objeto observable."""
        pass
