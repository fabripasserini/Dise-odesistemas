from dataclasses import dataclass
from typing import Optional
from .turno import Turno
from .certificado_manipulacion import CertificadoManipulacionAlimentos

@dataclass
class Empleado:
    """Representa a un empleado del cine."""
    nombre: str
    apellido: str
    turno: Turno
    certificado: Optional[CertificadoManipulacionAlimentos] = None
