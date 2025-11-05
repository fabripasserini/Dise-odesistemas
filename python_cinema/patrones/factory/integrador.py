"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/patrones/factory
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: sala_factory.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/factory/sala_factory.py
# ================================================================================

from ...entidades.salas.sala import Sala
from ...entidades.salas.sala_mini import SalaMini
from ...entidades.salas.sala_standard import SalaStandard
from ...entidades.salas.sala_premium import SalaPremium
from ...entidades.salas.sala_vip import SalaVip
from ...entidades.salas.tecnologia_premium import TecnologiaPremium

class SalaFactory:
    """Factory para la creación de diferentes tipos de salas."""
    @staticmethod
    def crear_sala(tipo: str, id_sala: int, capacidad: int, precio_base: float, **kwargs) -> Sala:
        if tipo.lower() == "mini":
            return SalaMini(id_sala, capacidad, precio_base)
        elif tipo.lower() == "standard":
            return SalaStandard(id_sala, capacidad, precio_base)
        elif tipo.lower() == "premium":
            tecnologia = kwargs.get("tecnologia")
            if not isinstance(tecnologia, TecnologiaPremium):
                raise ValueError("La sala premium requiere un tipo de tecnología válido.")
            return SalaPremium(id_sala, capacidad, precio_base, tecnologia)
        elif tipo.lower() == "vip":
            snacks = kwargs.get("snacks_incluidos", 50)
            return SalaVip(id_sala, capacidad, precio_base, snacks)
        else:
            raise ValueError(f"Tipo de sala desconocido: {tipo}")


