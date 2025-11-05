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
