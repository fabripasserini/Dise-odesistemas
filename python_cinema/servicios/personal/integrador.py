"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/servicios/personal
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: empleado_service.py
# Ruta: /home/fabri/PythonCinema/python_cinema/servicios/personal/empleado_service.py
# ================================================================================

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


