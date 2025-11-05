from datetime import date, timedelta
from ...entidades.personal.empleado import Empleado
from ...entidades.personal.turno import Turno
from ...entidades.personal.certificado_manipulacion import CertificadoManipulacionAlimentos

class EmpleadoService:
    """Servicio para la gestión de empleados."""
    def contratar_empleado(self, nombre: str, apellido: str, turno: Turno, necesita_certificado: bool) -> Empleado:
        """Contrata un nuevo empleado."""
        certificado = None
        if necesita_certificado:
            certificado = CertificadoManipulacionAlimentos(
                fecha_emision=date.today(),
                fecha_vencimiento=date.today() + timedelta(days=365 * 2)
            )
        return Empleado(nombre, apellido, turno, certificado)
