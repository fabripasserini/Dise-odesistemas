class CinemaException(Exception):
    """Excepción base para la aplicación PythonCinema."""
    def __init__(self, message="Ha ocurrido un error en la aplicación de cine."):
        self.message = message
        super().__init__(self.message)
