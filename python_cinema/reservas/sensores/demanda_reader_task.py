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
