"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/patrones/observer
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/observer/observable.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/observer/observer.py
# ================================================================================

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para el patrón Observer."""
    @abstractmethod
    def update(self, data: T) -> None:
        """Recibe la actualización del objeto observable."""
        pass


