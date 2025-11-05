from .cinema_exception import CinemaException

class SnacksAgotadosException(CinemaException):
    """Lanzada cuando no hay más snacks disponibles en una sala VIP."""
    def __init__(self, message="Los snacks para esta sala se han agotado."):
        self.message = message
        super().__init__(self.message)
