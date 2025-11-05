from .cinema_exception import CinemaException

class PersistenciaException(CinemaException):
    """Lanzada en caso de errores de guardado o carga de datos."""
    def __init__(self, message="Error durante la persistencia de datos."):
        self.message = message
        super().__init__(self.message)
