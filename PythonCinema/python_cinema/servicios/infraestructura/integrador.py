"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/servicios/infraestructura
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/infraestructura/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: complejo_service.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/infraestructura/complejo_service.py
# ================================================================================

from ...entidades.infraestructura.complejo import Complejo
from ...entidades.infraestructura.edificio import Edificio
from ...entidades.salas.sala import Sala
from ...excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException

class ComplejoService:
    """Servicio para gestionar complejos de cines."""
    def crear_complejo(self, id_complejo: int, nombre: str, edificio: Edificio) -> Complejo:
        """Crea un nuevo complejo."""
        print(f"Creando complejo '{nombre}' en {edificio.direccion}.")
        return Complejo(id_complejo, nombre, edificio)

    def agregar_sala_a_complejo(self, complejo: Complejo, sala: Sala):
        """Agrega una sala a un complejo, verificando la superficie."""
        superficie_requerida = sala.capacidad * 1.5  # Asumimos 1.5 m2 por asiento
        superficie_ocupada = sum(s.capacidad * 1.5 for s in complejo.salas)
        
        if superficie_ocupada + superficie_requerida > complejo.edificio.superficie_total:
            raise SuperficieInsuficienteException()
        
        complejo.agregar_sala(sala)
        print(f"Sala {sala.id_sala} agregada al complejo '{complejo.nombre}'.")


# ================================================================================
# ARCHIVO 3/4: edificio_service.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/infraestructura/edificio_service.py
# ================================================================================

from ...entidades.infraestructura.edificio import Edificio

class EdificioService:
    """Servicio para gestionar edificios."""
    def construir_edificio(self, direccion: str, superficie: float) -> Edificio:
        """Crea una nueva instancia de Edificio."""
        print(f"Construyendo edificio en {direccion} con {superficie} m2.")
        return Edificio(direccion=direccion, superficie_total=superficie)


# ================================================================================
# ARCHIVO 4/4: registro_comercial_service.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/infraestructura/registro_comercial_service.py
# ================================================================================

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


