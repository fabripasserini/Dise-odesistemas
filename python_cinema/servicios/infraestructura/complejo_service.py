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
