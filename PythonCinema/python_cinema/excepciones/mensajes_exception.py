from .cinema_exception import CinemaException

class MensajesException(CinemaException):
    """Lanzada para errores relacionados con el sistema de mensajería."""
    def __init__(self, message="Error en el sistema de mensajes."):
        self.message = message
        super().__init__(self.message)
