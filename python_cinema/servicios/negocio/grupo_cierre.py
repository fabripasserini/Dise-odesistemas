from typing import List, TypeVar, Generic

T = TypeVar('T')

class GrupoCierre(Generic[T]):
    """Clase genérica para agrupar elementos para una operación de cierre."""
    def __init__(self, nombre_grupo: str):
        self.nombre_grupo = nombre_grupo
        self.elementos: List[T] = []

    def agregar_elemento(self, elemento: T):
        self.elementos.append(elemento)

    def procesar_grupo(self):
        print(f"Procesando grupo de cierre '{self.nombre_grupo}' con {len(self.elementos)} elementos.")
