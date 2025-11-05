"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/reservas/sensores
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/reservas/sensores/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: demanda_reader_task.py
# Ruta: /home/fabri/PythonCinema/python_cinema/reservas/sensores/demanda_reader_task.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: ocupacion_reader_task.py
# Ruta: /home/fabri/PythonCinema/python_cinema/reservas/sensores/ocupacion_reader_task.py
# ================================================================================

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


