"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/fabri/PythonCinema/python_cinema
Fecha de generacion: 2025-11-04 20:59:22
Total de archivos integrados: 63
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades/infraestructura
#   4. __init__.py
#   5. complejo.py
#   6. edificio.py
#   7. registro_comercial.py
#
# DIRECTORIO: entidades/personal
#   8. __init__.py
#   9. certificado_manipulacion.py
#   10. empleado.py
#   11. equipo.py
#   12. turno.py
#
# DIRECTORIO: entidades/salas
#   13. __init__.py
#   14. sala.py
#   15. sala_mini.py
#   16. sala_premium.py
#   17. sala_standard.py
#   18. sala_vip.py
#   19. tecnologia_premium.py
#
# DIRECTORIO: excepciones
#   20. __init__.py
#   21. cinema_exception.py
#   22. mensajes_exception.py
#   23. persistencia_exception.py
#   24. snacks_agotados_exception.py
#   25. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   26. __init__.py
#
# DIRECTORIO: patrones/factory
#   27. __init__.py
#   28. sala_factory.py
#
# DIRECTORIO: patrones/observer
#   29. __init__.py
#   30. observable.py
#   31. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   32. __init__.py
#   33. evento_complejo.py
#   34. evento_sensor.py
#
# DIRECTORIO: patrones/singleton
#   35. __init__.py
#
# DIRECTORIO: patrones/strategy
#   36. __init__.py
#   37. venta_entradas_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   38. __init__.py
#   39. venta_constante_strategy.py
#   40. venta_estacional_strategy.py
#
# DIRECTORIO: reservas
#   41. __init__.py
#
# DIRECTORIO: reservas/control
#   42. __init__.py
#   43. control_precios_task.py
#
# DIRECTORIO: reservas/sensores
#   44. __init__.py
#   45. demanda_reader_task.py
#   46. ocupacion_reader_task.py
#
# DIRECTORIO: servicios
#   47. __init__.py
#
# DIRECTORIO: servicios/infraestructura
#   48. __init__.py
#   49. complejo_service.py
#   50. edificio_service.py
#   51. registro_comercial_service.py
#
# DIRECTORIO: servicios/negocio
#   52. __init__.py
#   53. cadena_de_cines_service.py
#   54. grupo_cierre.py
#
# DIRECTORIO: servicios/personal
#   55. __init__.py
#   56. empleado_service.py
#
# DIRECTORIO: servicios/salas
#   57. __init__.py
#   58. sala_mini_service.py
#   59. sala_premium_service.py
#   60. sala_service.py
#   61. sala_service_registry.py
#   62. sala_standard_service.py
#   63. sala_vip_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/63: __init__.py
# Directorio: .
# Ruta completa: /home/fabri/PythonCinema/python_cinema/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/63: constantes.py
# Directorio: .
# Ruta completa: /home/fabri/PythonCinema/python_cinema/constantes.py
# ==============================================================================

CAPACIDAD_MINIMA = 10
CAPACIDAD_MAXIMA_MINI = 25
CAPACIDAD_MAXIMA_STANDARD = 100
CAPACIDAD_MAXIMA_PREMIUM = 75
CAPACIDAD_MAXIMA_VIP = 50



################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/63: __init__.py
# Directorio: entidades
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/infraestructura
################################################################################

# ==============================================================================
# ARCHIVO 4/63: __init__.py
# Directorio: entidades/infraestructura
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/infraestructura/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/63: complejo.py
# Directorio: entidades/infraestructura
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/infraestructura/complejo.py
# ==============================================================================

from typing import List
from ..salas.sala import Sala
from .edificio import Edificio

class Complejo:
    """Representa un complejo de cines, que contiene varias salas."""
    def __init__(self, id_complejo: int, nombre: str, edificio: Edificio):
        self.id_complejo = id_complejo
        self.nombre = nombre
        self.edificio = edificio
        self.salas: List[Sala] = []

    def agregar_sala(self, sala: Sala):
        self.salas.append(sala)

    def __str__(self) -> str:
        return f"Complejo '{self.nombre}' (ID: {self.id_complejo}) en {self.edificio.direccion}"


# ==============================================================================
# ARCHIVO 6/63: edificio.py
# Directorio: entidades/infraestructura
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/infraestructura/edificio.py
# ==============================================================================

from dataclasses import dataclass

@dataclass
class Edificio:
    """Representa un edificio físico."""
    direccion: str
    superficie_total: float


# ==============================================================================
# ARCHIVO 7/63: registro_comercial.py
# Directorio: entidades/infraestructura
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/infraestructura/registro_comercial.py
# ==============================================================================

from typing import List
from .complejo import Complejo

class RegistroComercial:
    """Representa el registro de todos los complejos de una cadena de cines."""
    def __init__(self, nombre_cadena: str):
        self.nombre_cadena = nombre_cadena
        self.complejos: List[Complejo] = []

    def agregar_complejo(self, complejo: Complejo):
        self.complejos.append(complejo)



################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 8/63: __init__.py
# Directorio: entidades/personal
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 9/63: certificado_manipulacion.py
# Directorio: entidades/personal
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/personal/certificado_manipulacion.py
# ==============================================================================

from dataclasses import dataclass
from datetime import date

@dataclass
class CertificadoManipulacionAlimentos:
    """Certificado necesario para manipular alimentos."""
    fecha_emision: date
    fecha_vencimiento: date


# ==============================================================================
# ARCHIVO 10/63: empleado.py
# Directorio: entidades/personal
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/personal/empleado.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 11/63: equipo.py
# Directorio: entidades/personal
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/personal/equipo.py
# ==============================================================================

from typing import List
from .empleado import Empleado

class Equipo:
    """Representa un equipo de trabajo asignado a un complejo o área."""
    def __init__(self, nombre_equipo: str):
        self.nombre_equipo = nombre_equipo
        self.miembros: List[Empleado] = []

    def agregar_miembro(self, empleado: Empleado):
        self.miembros.append(empleado)


# ==============================================================================
# ARCHIVO 12/63: turno.py
# Directorio: entidades/personal
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/personal/turno.py
# ==============================================================================

from enum import Enum

class Turno(Enum):
    """Turnos de trabajo para empleados."""
    MANANA = "Mañana"
    TARDE = "Tarde"
    NOCHE = "Noche"



################################################################################
# DIRECTORIO: entidades/salas
################################################################################

# ==============================================================================
# ARCHIVO 13/63: __init__.py
# Directorio: entidades/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/salas/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 14/63: sala.py
# Directorio: entidades/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/salas/sala.py
# ==============================================================================

from abc import ABC, abstractmethod

class Sala(ABC):
    """Clase base abstracta para una sala de cine."""
    def __init__(self, id_sala: int, capacidad: int, precio_base: float):
        self.id_sala = id_sala
        self.capacidad = capacidad
        self.precio_base = precio_base

    @abstractmethod
    def obtener_tipo(self) -> str:
        """Devuelve el tipo de sala."""
        pass

    def __str__(self) -> str:
        return f"Sala {self.obtener_tipo()} (ID: {self.id_sala}, Capacidad: {self.capacidad})"


# ==============================================================================
# ARCHIVO 15/63: sala_mini.py
# Directorio: entidades/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/salas/sala_mini.py
# ==============================================================================

from .sala import Sala

class SalaMini(Sala):
    """Sala de tipo Mini."""
    def obtener_tipo(self) -> str:
        return "Mini"


# ==============================================================================
# ARCHIVO 16/63: sala_premium.py
# Directorio: entidades/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/salas/sala_premium.py
# ==============================================================================

from .sala import Sala
from .tecnologia_premium import TecnologiaPremium

class SalaPremium(Sala):
    """Sala de tipo Premium con tecnología especial."""
    def __init__(self, id_sala: int, capacidad: int, precio_base: float, tecnologia: TecnologiaPremium):
        super().__init__(id_sala, capacidad, precio_base)
        self.tecnologia = tecnologia

    def obtener_tipo(self) -> str:
        return f"Premium ({self.tecnologia.value})"


# ==============================================================================
# ARCHIVO 17/63: sala_standard.py
# Directorio: entidades/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/salas/sala_standard.py
# ==============================================================================

from .sala import Sala

class SalaStandard(Sala):
    """Sala de tipo Standard."""
    def obtener_tipo(self) -> str:
        return "Standard"


# ==============================================================================
# ARCHIVO 18/63: sala_vip.py
# Directorio: entidades/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/salas/sala_vip.py
# ==============================================================================

from .sala import Sala
from ...excepciones.snacks_agotados_exception import SnacksAgotadosException

class SalaVip(Sala):
    """Sala de tipo VIP con servicios adicionales."""
    def __init__(self, id_sala: int, capacidad: int, precio_base: float, snacks_incluidos: int):
        super().__init__(id_sala, capacidad, precio_base)
        self.snacks_disponibles = snacks_incluidos

    def obtener_tipo(self) -> str:
        return "VIP"

    def consumir_snack(self):
        """Consume un snack de la reserva de la sala."""
        if self.snacks_disponibles > 0:
            self.snacks_disponibles -= 1
        else:
            raise SnacksAgotadosException()


# ==============================================================================
# ARCHIVO 19/63: tecnologia_premium.py
# Directorio: entidades/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/entidades/salas/tecnologia_premium.py
# ==============================================================================

from enum import Enum

class TecnologiaPremium(Enum):
    """Enumeración de tecnologías para salas Premium."""
    IMAX = "IMAX"
    DOLBY_ATMOS = "Dolby Atmos"
    SCREENX = "ScreenX"



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 20/63: __init__.py
# Directorio: excepciones
# Ruta completa: /home/fabri/PythonCinema/python_cinema/excepciones/__init__.py
# ==============================================================================

from .cinema_exception import CinemaException
from .superficie_insuficiente_exception import SuperficieInsuficienteException
from .snacks_agotados_exception import SnacksAgotadosException
from .persistencia_exception import PersistenciaException
from .mensajes_exception import MensajesException


# ==============================================================================
# ARCHIVO 21/63: cinema_exception.py
# Directorio: excepciones
# Ruta completa: /home/fabri/PythonCinema/python_cinema/excepciones/cinema_exception.py
# ==============================================================================

class CinemaException(Exception):
    """Excepción base para la aplicación PythonCinema."""
    def __init__(self, message="Ha ocurrido un error en la aplicación de cine."):
        self.message = message
        super().__init__(self.message)


# ==============================================================================
# ARCHIVO 22/63: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: /home/fabri/PythonCinema/python_cinema/excepciones/mensajes_exception.py
# ==============================================================================

from .cinema_exception import CinemaException

class MensajesException(CinemaException):
    """Lanzada para errores relacionados con el sistema de mensajería."""
    def __init__(self, message="Error en el sistema de mensajes."):
        self.message = message
        super().__init__(self.message)


# ==============================================================================
# ARCHIVO 23/63: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/fabri/PythonCinema/python_cinema/excepciones/persistencia_exception.py
# ==============================================================================

from .cinema_exception import CinemaException

class PersistenciaException(CinemaException):
    """Lanzada en caso de errores de guardado o carga de datos."""
    def __init__(self, message="Error durante la persistencia de datos."):
        self.message = message
        super().__init__(self.message)


# ==============================================================================
# ARCHIVO 24/63: snacks_agotados_exception.py
# Directorio: excepciones
# Ruta completa: /home/fabri/PythonCinema/python_cinema/excepciones/snacks_agotados_exception.py
# ==============================================================================

from .cinema_exception import CinemaException

class SnacksAgotadosException(CinemaException):
    """Lanzada cuando no hay más snacks disponibles en una sala VIP."""
    def __init__(self, message="Los snacks para esta sala se han agotado."):
        self.message = message
        super().__init__(self.message)


# ==============================================================================
# ARCHIVO 25/63: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /home/fabri/PythonCinema/python_cinema/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

from .cinema_exception import CinemaException

class SuperficieInsuficienteException(CinemaException):
    """Lanzada cuando no hay suficiente superficie para construir."""
    def __init__(self, message="La superficie disponible es insuficiente para la operación solicitada."):
        self.message = message
        super().__init__(self.message)



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 26/63: __init__.py
# Directorio: patrones
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 27/63: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 28/63: sala_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/factory/sala_factory.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 29/63: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 30/63: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/observer/observable.py
# ==============================================================================

from typing import TypeVar, Generic, List
from .observer import Observer

T = TypeVar('T')

class Observable(Generic[T]):
    """Clase base para objetos observables."""
    def __init__(self):
        self._observers: List[Observer[T]] = []

    def attach(self, observer: Observer[T]) -> None:
        """Añade un observador."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer[T]) -> None:
        """Quita un observador."""
        self._observers.remove(observer)

    def notify(self, data: T) -> None:
        """Notifica a todos los observadores."""
        for observer in self._observers:
            observer.update(data)


# ==============================================================================
# ARCHIVO 31/63: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/observer/observer.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para el patrón Observer."""
    @abstractmethod
    def update(self, data: T) -> None:
        """Recibe la actualización del objeto observable."""
        pass



################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 32/63: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/observer/eventos/__init__.py
# ==============================================================================

from .evento_sensor import EventoSensor
from .evento_complejo import EventoComplejo


# ==============================================================================
# ARCHIVO 33/63: evento_complejo.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/observer/eventos/evento_complejo.py
# ==============================================================================

from dataclasses import dataclass

@dataclass
class EventoComplejo:
    """Datos de evento de un complejo."""
    id_complejo: int
    mensaje: str


# ==============================================================================
# ARCHIVO 34/63: evento_sensor.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/observer/eventos/evento_sensor.py
# ==============================================================================

from dataclasses import dataclass

@dataclass
class EventoSensor:
    """Datos de evento de un sensor de mercado."""
    tipo_sensor: str
    valor: float
    unidad: str



################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 35/63: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/singleton/__init__.py
# ==============================================================================

import functools

def singleton(cls):
    """Decorador para implementar el patrón Singleton."""
    instances = {}
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper_singleton



################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 36/63: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 37/63: venta_entradas_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/strategy/venta_entradas_strategy.py
# ==============================================================================

from abc import ABC, abstractmethod

class VentaEntradasStrategy(ABC):
    """Interfaz para el Strategy de cálculo de precios de venta."""
    @abstractmethod
    def calcular_precio(self, precio_base: float, factor_demanda: float) -> float:
        """Calcula el precio final basado en la demanda."""
        pass



################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 38/63: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 39/63: venta_constante_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/strategy/impl/venta_constante_strategy.py
# ==============================================================================

from ..venta_entradas_strategy import VentaEntradasStrategy

class VentaConstanteStrategy(VentaEntradasStrategy):
    """Estrategia de precios constantes, ignora la demanda."""
    def calcular_precio(self, precio_base: float, factor_demanda: float) -> float:
        print("Aplicando estrategia de precios constantes.")
        return precio_base


# ==============================================================================
# ARCHIVO 40/63: venta_estacional_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/fabri/PythonCinema/python_cinema/patrones/strategy/impl/venta_estacional_strategy.py
# ==============================================================================

from ..venta_entradas_strategy import VentaEntradasStrategy

class VentaEstacionalStrategy(VentaEntradasStrategy):
    """Estrategia de precios que varía con la demanda."""
    def calcular_precio(self, precio_base: float, factor_demanda: float) -> float:
        # factor_demanda es un % (ej: 1.2 para 120% de demanda)
        precio_ajustado = precio_base * factor_demanda
        print(f"Aplicando estrategia estacional. Demanda: {factor_demanda:.2f}, Precio ajustado: ${precio_ajustado:.2f}")
        return precio_ajustado



################################################################################
# DIRECTORIO: reservas
################################################################################

# ==============================================================================
# ARCHIVO 41/63: __init__.py
# Directorio: reservas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/reservas/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: reservas/control
################################################################################

# ==============================================================================
# ARCHIVO 42/63: __init__.py
# Directorio: reservas/control
# Ruta completa: /home/fabri/PythonCinema/python_cinema/reservas/control/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 43/63: control_precios_task.py
# Directorio: reservas/control
# Ruta completa: /home/fabri/PythonCinema/python_cinema/reservas/control/control_precios_task.py
# ==============================================================================

from ...patrones.observer.observer import Observer
from ...patrones.observer.eventos.evento_sensor import EventoSensor
from ...patrones.strategy.venta_entradas_strategy import VentaEntradasStrategy
from ...patrones.strategy.impl.venta_constante_strategy import VentaConstanteStrategy
from ...patrones.strategy.impl.venta_estacional_strategy import VentaEstacionalStrategy

class ControlPreciosTask(Observer[EventoSensor]):
    """Controlador que ajusta los precios en función de la demanda."""
    def __init__(self, precio_base_actual: float):
        self.precio_base = precio_base_actual
        self.precio_final = precio_base_actual
        self.strategy: VentaEntradasStrategy = VentaConstanteStrategy()

    def update(self, data: EventoSensor) -> None:
        if data.tipo_sensor == "demanda":
            print(f"\n[Controlador de Precios] Recibido evento de demanda: {data.valor}%")
            if data.valor > 110:  # Si la demanda supera el 110%
                self.strategy = VentaEstacionalStrategy()
            else:
                self.strategy = VentaConstanteStrategy()
            
            # El factor de demanda es el porcentaje convertido a multiplicador
            factor_demanda = data.valor / 100.0
            self.precio_final = self.strategy.calcular_precio(self.precio_base, factor_demanda)
            print(f"[Controlador de Precios] Nuevo precio de entrada calculado: ${self.precio_final:.2f}")




################################################################################
# DIRECTORIO: reservas/sensores
################################################################################

# ==============================================================================
# ARCHIVO 44/63: __init__.py
# Directorio: reservas/sensores
# Ruta completa: /home/fabri/PythonCinema/python_cinema/reservas/sensores/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 45/63: demanda_reader_task.py
# Directorio: reservas/sensores
# Ruta completa: /home/fabri/PythonCinema/python_cinema/reservas/sensores/demanda_reader_task.py
# ==============================================================================

import random
from ...patrones.observer.observable import Observable
from ...patrones.observer.eventos.evento_sensor import EventoSensor

class DemandaReaderTask(Observable[EventoSensor]):
    """Sensor simulado que mide la demanda del mercado."""
    def __init__(self):
        super().__init__()
        self._demanda_actual = 100.0

    def run_simulation_step(self):
        """Simula una lectura del sensor y notifica a los observadores."""
        # Simula una fluctuación aleatoria en la demanda
        fluctuacion = random.uniform(-15.0, 15.0)
        self._demanda_actual += fluctuacion
        self._demanda_actual = max(50.0, min(150.0, self._demanda_actual)) # Limitar entre 50% y 150%
        
        print(f"\n[Sensor de Demanda] Nueva lectura: {self._demanda_actual:.2f}%")
        
        evento = EventoSensor(
            tipo_sensor="demanda",
            valor=self._demanda_actual,
            unidad="%"
        )
        self.notify(evento)


# ==============================================================================
# ARCHIVO 46/63: ocupacion_reader_task.py
# Directorio: reservas/sensores
# Ruta completa: /home/fabri/PythonCinema/python_cinema/reservas/sensores/ocupacion_reader_task.py
# ==============================================================================

import random
from ...patrones.observer.observable import Observable
from ...patrones.observer.eventos.evento_sensor import EventoSensor

class OcupacionReaderTask(Observable[EventoSensor]):
    """Sensor simulado que mide la ocupación de las salas."""
    def run_simulation_step(self):
        """Simula una lectura del sensor y notifica a los observadores."""
        ocupacion = random.uniform(20.0, 100.0)
        print(f"\n[Sensor de Ocupación] Nueva lectura: {ocupacion:.2f}%")
        
        evento = EventoSensor(
            tipo_sensor="ocupacion",
            valor=ocupacion,
            unidad="%"
        )
        self.notify(evento)



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 47/63: __init__.py
# Directorio: servicios
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/infraestructura
################################################################################

# ==============================================================================
# ARCHIVO 48/63: __init__.py
# Directorio: servicios/infraestructura
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/infraestructura/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 49/63: complejo_service.py
# Directorio: servicios/infraestructura
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/infraestructura/complejo_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 50/63: edificio_service.py
# Directorio: servicios/infraestructura
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/infraestructura/edificio_service.py
# ==============================================================================

from ...entidades.infraestructura.edificio import Edificio

class EdificioService:
    """Servicio para gestionar edificios."""
    def construir_edificio(self, direccion: str, superficie: float) -> Edificio:
        """Crea una nueva instancia de Edificio."""
        print(f"Construyendo edificio en {direccion} con {superficie} m2.")
        return Edificio(direccion=direccion, superficie_total=superficie)


# ==============================================================================
# ARCHIVO 51/63: registro_comercial_service.py
# Directorio: servicios/infraestructura
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/infraestructura/registro_comercial_service.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 52/63: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/negocio/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 53/63: cadena_de_cines_service.py
# Directorio: servicios/negocio
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/negocio/cadena_de_cines_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 54/63: grupo_cierre.py
# Directorio: servicios/negocio
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/negocio/grupo_cierre.py
# ==============================================================================

from typing import List, TypeVar, Generic

T = TypeVar('T')

class GrupoCierre(Generic[T]):
    """Clase genérica para agrupar elementos para una operación de cierre."""
    def __init__(self, nombre_grupo: str):
        self.nombre_grupo = nombre_grupo
        self.elementos: List[T] = []

    def agregar_elemento(self, elemento: T):
        self.elementos.append(elemento)

    def procesar_grupo(self):
        print(f"Procesando grupo de cierre '{self.nombre_grupo}' con {len(self.elementos)} elementos.")



################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 55/63: __init__.py
# Directorio: servicios/personal
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 56/63: empleado_service.py
# Directorio: servicios/personal
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/personal/empleado_service.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios/salas
################################################################################

# ==============================================================================
# ARCHIVO 57/63: __init__.py
# Directorio: servicios/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/salas/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 58/63: sala_mini_service.py
# Directorio: servicios/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/salas/sala_mini_service.py
# ==============================================================================

from .sala_service import SalaService
from ...entidades.salas.sala import Sala

class SalaMiniService(SalaService):
    """Servicio específico para salas Mini."""
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        return precio_base * 0.8  # 20% de descuento


# ==============================================================================
# ARCHIVO 59/63: sala_premium_service.py
# Directorio: servicios/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/salas/sala_premium_service.py
# ==============================================================================

from .sala_service import SalaService
from ...entidades.salas.sala import Sala

class SalaPremiumService(SalaService):
    """Servicio específico para salas Premium."""
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        return precio_base * 1.5  # 50% de recargo


# ==============================================================================
# ARCHIVO 60/63: sala_service.py
# Directorio: servicios/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/salas/sala_service.py
# ==============================================================================

from abc import ABC, abstractmethod
from ...entidades.salas.sala import Sala

class SalaService(ABC):
    """Interfaz para servicios de gestión de salas."""
    @abstractmethod
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        """Calcula el precio final de una entrada para esta sala."""
        pass


# ==============================================================================
# ARCHIVO 61/63: sala_service_registry.py
# Directorio: servicios/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/salas/sala_service_registry.py
# ==============================================================================

from ...patrones.singleton import singleton
from .sala_service import SalaService
from .sala_mini_service import SalaMiniService
from .sala_standard_service import SalaStandardService
from .sala_premium_service import SalaPremiumService
from .sala_vip_service import SalaVipService

@singleton
class SalaServiceRegistry:
    """Registro Singleton para los servicios de salas."""
    def __init__(self):
        self._servicios = {
            "mini": SalaMiniService(),
            "standard": SalaStandardService(),
            "premium": SalaPremiumService(),
            "vip": SalaVipService()
        }

    def get_service(self, tipo_sala: str) -> SalaService:
        """Obtiene el servicio para un tipo de sala específico."""
        tipo_sala_key = tipo_sala.split(' ')[0].lower()
        service = self._servicios.get(tipo_sala_key)
        if not service:
            raise ValueError(f"No se encontró servicio para el tipo de sala: {tipo_sala}")
        return service


# ==============================================================================
# ARCHIVO 62/63: sala_standard_service.py
# Directorio: servicios/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/salas/sala_standard_service.py
# ==============================================================================

from .sala_service import SalaService
from ...entidades.salas.sala import Sala

class SalaStandardService(SalaService):
    """Servicio específico para salas Standard."""
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        return precio_base  # Precio sin modificar


# ==============================================================================
# ARCHIVO 63/63: sala_vip_service.py
# Directorio: servicios/salas
# Ruta completa: /home/fabri/PythonCinema/python_cinema/servicios/salas/sala_vip_service.py
# ==============================================================================

from .sala_service import SalaService
from ...entidades.salas.sala import Sala

class SalaVipService(SalaService):
    """Servicio específico para salas VIP."""
    def calcular_precio_final(self, sala: Sala, precio_base: float) -> float:
        return precio_base * 2.0  # 100% de recargo



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 63
# Generado: 2025-11-04 20:59:22
################################################################################
