from typing import TypeVar, Generic, List
from .observer import Observer

T = TypeVar('T')

class Observable(Generic[T]):
    """Clase base para objetos observables."""
    def __init__(self):
        self._observers: List[Observer[T]] = []

    def attach(self, observer: Observer[T]) -> None:
        """Añade un observador."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer[T]) -> None:
        """Quita un observador."""
        self._observers.remove(observer)

    def notify(self, data: T) -> None:
        """Notifica a todos los observadores."""
        for observer in self._observers:
            observer.update(data)
