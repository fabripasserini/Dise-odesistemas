from ...entidades.infraestructura.registro_comercial import RegistroComercial
from ...entidades.infraestructura.complejo import Complejo

class RegistroComercialService:
    """Servicio para gestionar el registro comercial de la cadena."""
    def crear_registro(self, nombre_cadena: str) -> RegistroComercial:
        """Crea un nuevo registro comercial."""
        return RegistroComercial(nombre_cadena)

    def registrar_complejo(self, registro: RegistroComercial, complejo: Complejo):
        """Añade un complejo al registro."""
        registro.agregar_complejo(complejo)
        print(f"Complejo '{complejo.nombre}' registrado en la cadena '{registro.nombre_cadena}'.")
