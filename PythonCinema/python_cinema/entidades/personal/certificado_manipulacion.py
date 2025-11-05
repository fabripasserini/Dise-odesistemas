from dataclasses import dataclass
from datetime import date

@dataclass
class CertificadoManipulacionAlimentos:
    """Certificado necesario para manipular alimentos."""
    fecha_emision: date
    fecha_vencimiento: date
