from .cinema_exception import CinemaException

class SuperficieInsuficienteException(CinemaException):
    """Lanzada cuando no hay suficiente superficie para construir."""
    def __init__(self, message="La superficie disponible es insuficiente para la operación solicitada."):
        self.message = message
        super().__init__(self.message)
