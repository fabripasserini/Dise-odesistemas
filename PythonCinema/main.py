import time
from python_cinema.entidades.salas.tecnologia_premium import TecnologiaPremium
from python_cinema.patrones.factory.sala_factory import SalaFactory
from python_cinema.servicios.negocio.cadena_de_cines_service import CadenaDeCinesService
from python_cinema.servicios.infraestructura.complejo_service import ComplejoService
from python_cinema.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_cinema.reservas.sensores.demanda_reader_task import DemandaReaderTask
from python_cinema.reservas.control.control_precios_task import ControlPreciosTask

def main():
    """Punto de entrada principal de la aplicación."""
    print("### Iniciando Simulación de PythonCinema ###")

    # --- Configuración de la infraestructura ---
    cadena_service = CadenaDeCinesService()
    complejo_service = ComplejoService()

    complejo_central = cadena_service.construir_nuevo_complejo(
        id_complejo=1,
        nombre="Cine Central",
        direccion="Av. Corrientes 1234",
        superficie=2000.0
    )

    # --- Creación y asignación de salas usando la Factory ---
    print("\n--- Agregando salas al complejo ---")
    try:
        sala1 = SalaFactory.crear_sala("standard", id_sala=101, capacidad=100, precio_base=10.0)
        complejo_service.agregar_sala_a_complejo(complejo_central, sala1)

        sala2 = SalaFactory.crear_sala("vip", id_sala=102, capacidad=40, precio_base=10.0, snacks_incluidos=100)
        complejo_service.agregar_sala_a_complejo(complejo_central, sala2)

        sala3 = SalaFactory.crear_sala("premium", id_sala=103, capacidad=60, precio_base=10.0, tecnologia=TecnologiaPremium.IMAX)
        complejo_service.agregar_sala_a_complejo(complejo_central, sala3)
        
        # Intentar agregar una sala que excede la capacidad
        sala4 = SalaFactory.crear_sala("standard", id_sala=104, capacidad=500, precio_base=10.0)
        complejo_service.agregar_sala_a_complejo(complejo_central, sala4)

    except SuperficieInsuficienteException as e:
        print(f"ERROR al agregar sala: {e.message}")
    except ValueError as e:
        print(f"ERROR de configuración: {e}")

    print("\n--- Estado final del complejo ---")
    print(complejo_central)
    for sala in complejo_central.salas:
        print(f"  - {sala}")

    # --- Simulación del sistema de precios dinámicos (Observer) ---
    print("\n### Iniciando Simulación de Precios Dinámicos ###")
    precio_base_entradas = 12.50
    
    # El sujeto (observable) que emite eventos de demanda
    sensor_demanda = DemandaReaderTask()
    
    # El observador que reacciona a los eventos de demanda
    controlador_precios = ControlPreciosTask(precio_base_actual=precio_base_entradas)
    
    # Conectamos el observador al sujeto
    sensor_demanda.attach(controlador_precios)
    
    # Ejecutamos la simulación por unos pasos
    for i in range(5):
        sensor_demanda.run_simulation_step()
        time.sleep(1) # Pequeña pausa para que la salida sea legible

    print("\n### Simulación Finalizada ###")


if __name__ == "__main__":
    main()
