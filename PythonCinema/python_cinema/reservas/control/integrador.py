"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/reservas/control
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/reservas/control/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: control_precios_task.py
# Ruta: /home/fabri/PythonCinema/python_cinema/reservas/control/control_precios_task.py
# ================================================================================

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



