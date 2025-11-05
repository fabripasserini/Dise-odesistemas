from ...entidades.infraestructura.edificio import Edificio

class EdificioService:
    """Servicio para gestionar edificios."""
    def construir_edificio(self, direccion: str, superficie: float) -> Edificio:
        """Crea una nueva instancia de Edificio."""
        print(f"Construyendo edificio en {direccion} con {superficie} m2.")
        return Edificio(direccion=direccion, superficie_total=superficie)
