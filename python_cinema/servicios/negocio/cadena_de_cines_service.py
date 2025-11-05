from ..infraestructura.edificio_service import EdificioService
from ..infraestructura.complejo_service import ComplejoService
from ..infraestructura.registro_comercial_service import RegistroComercialService
from ...entidades.infraestructura.registro_comercial import RegistroComercial

class CadenaDeCinesService:
    """Servicio de alto nivel para orquestar las operaciones de la cadena de cines."""
    def __init__(self):
        self.edificio_service = EdificioService()
        self.complejo_service = ComplejoService()
        self.registro_service = RegistroComercialService()
        self.registro_comercial: RegistroComercial = self.registro_service.crear_registro("Python Cinemas")

    def construir_nuevo_complejo(self, id_complejo: int, nombre: str, direccion: str, superficie: float):
        """Construye un edificio y crea un complejo en él."""
        print(f"--- Iniciando construcción del complejo '{nombre}' ---")
        edificio = self.edificio_service.construir_edificio(direccion, superficie)
        complejo = self.complejo_service.crear_complejo(id_complejo, nombre, edificio)
        self.registro_service.registrar_complejo(self.registro_comercial, complejo)
        print("--- Construcción finalizada ---")
        return complejo
