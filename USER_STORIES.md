# Historias de Usuario - Sistema de Gestión de Cines

**Proyecto**: PythonCinema
**Version**: 1.0.0
**Fecha**: Noviembre 2025
**Metodologia**: User Story Mapping

---

## Indice

1. [Epic 1: Gestión de Infraestructura](#epic-1-gestion-de-infraestructura)
2. [Epic 2: Gestión de Salas](#epic-2-gestion-de-salas)
3. [Epic 3: Sistema de Precios Dinámicos](#epic-3-sistema-de-precios-dinamicos)
4. [Epic 4: Operaciones de la Cadena](#epic-4-operaciones-de-la-cadena)
5. [Historias Tecnicas (Patrones de Diseno)](#historias-tecnicas-patrones-de-diseno)

---

## Epic 1: Gestión de Infraestructura

### US-001: Construir Edificio para un Complejo

**Como** inversor de la cadena de cines
**Quiero** registrar un edificio con su dirección y superficie total
**Para** establecer la ubicación física y los límites de un futuro complejo.

#### Criterios de Aceptacion

- [x] El sistema debe permitir crear un edificio con:
  - Dirección (cadena de texto)
  - Superficie total en metros cuadrados (número positivo)
- [x] La superficie debe ser un valor positivo.
- [x] El servicio debe confirmar la construcción del edificio.

#### Detalles Tecnicos

**Clase**: `Edificio` (`python_cinema/entidades/infraestructura/edificio.py`)
**Servicio**: `EdificioService` (`python_cinema/servicios/infraestructura/edificio_service.py`)

**Codigo de ejemplo**:
```python
from python_cinema.servicios.infraestructura.edificio_service import EdificioService

edificio_service = EdificioService()
edificio = edificio_service.construir_edificio(
    direccion="Av. Corrientes 1234",
    superficie=2000.0
)
```

**Trazabilidad**: `main.py` líneas 17-22 (invocado a través de `CadenaDeCinesService`)

---

### US-002: Crear un Complejo de Cines en un Edificio

**Como** gerente de operaciones
**Quiero** crear un complejo de cines asociado a un edificio existente
**Para** organizar las salas y operaciones en una ubicación específica.

#### Criterios de Aceptacion

- [x] Un complejo debe tener:
  - ID de complejo (número único)
  - Nombre identificatorio
  - Una referencia a un objeto `Edificio` válido.
  - Una lista de salas (vacía al inicio).
- [x] El servicio debe confirmar la creación del complejo.

#### Detalles Tecnicos

**Clase**: `Complejo` (`python_cinema/entidades/infraestructura/complejo.py`)
**Servicio**: `ComplejoService` (`python_cinema/servicios/infraestructura/complejo_service.py`)

**Codigo de ejemplo**:
```python
from python_cinema.servicios.infraestructura.complejo_service import ComplejoService

complejo_service = ComplejoService()
complejo = complejo_service.crear_complejo(
    id_complejo=1,
    nombre="Cine Central",
    edificio=edificio
)
```

**Trazabilidad**: `main.py` líneas 17-22 (invocado a través de `CadenaDeCinesService`)

---

### US-003: Agregar una Sala a un Complejo

**Como** gerente de un complejo
**Quiero** agregar una sala a mi complejo, validando la superficie disponible
**Para** expandir la oferta de películas sin exceder la capacidad del edificio.

#### Criterios de Aceptacion

- [x] El sistema debe permitir agregar un objeto `Sala` a un `Complejo`.
- [x] Se debe calcular la superficie requerida por la nueva sala (capacidad * 1.5 m²).
- [x] Se debe verificar que la superficie ocupada total no exceda la superficie del edificio.
- [x] Si no hay superficie suficiente, se debe lanzar la excepción `SuperficieInsuficienteException`.
- [x] Si la sala se agrega con éxito, se debe mostrar un mensaje de confirmación.

#### Detalles Tecnicos

**Servicio**: `ComplejoService.agregar_sala_a_complejo()`

**Codigo de ejemplo**:
```python
from python_cinema.servicios.infraestructura.complejo_service import ComplejoService
from python_cinema.patrones.factory.sala_factory import SalaFactory

complejo_service = ComplejoService()
sala_standard = SalaFactory.crear_sala("standard", 101, 100, 10.0)

try:
    complejo_service.agregar_sala_a_complejo(complejo, sala_standard)
except SuperficieInsuficienteException as e:
    print(e.message)
```

**Trazabilidad**: `main.py` líneas 28-39

---

## Epic 2: Gestión de Salas

### US-004: Crear Diferentes Tipos de Salas

**Como** administrador del sistema
**Quiero** crear salas de tipo "Standard", "VIP", "Premium" y "Mini" con características específicas
**Para** ofrecer distintas experiencias y precios a los clientes.

#### Criterios de Aceptacion

- [x] Se deben poder crear los siguientes tipos de sala:
  - **Standard**: Capacidad y precio base.
  - **VIP**: Capacidad, precio y cantidad de snacks incluidos.
  - **Premium**: Capacidad, precio y una tecnología específica (IMAX, Dolby Atmos, etc.).
  - **Mini**: Capacidad y precio base.
- [x] La creación debe realizarse a través de un Factory Method para desacoplar al cliente de las clases concretas.
- [x] Si se solicita un tipo de sala desconocido, se debe lanzar `ValueError`.

#### Detalles Tecnicos

**Clases**: `Sala`, `SalaStandard`, `SalaVip`, `SalaPremium`, `SalaMini`
**Factory**: `SalaFactory` (`python_cinema/patrones/factory/sala_factory.py`)

**Codigo de ejemplo**:
```python
from python_cinema.patrones.factory.sala_factory import SalaFactory
from python_cinema.entidades.salas.tecnologia_premium import TecnologiaPremium

# Crear una sala VIP
sala_vip = SalaFactory.crear_sala("vip", 102, 40, 10.0, snacks_incluidos=100)

# Crear una sala Premium
sala_premium = SalaFactory.crear_sala("premium", 103, 60, 10.0, tecnologia=TecnologiaPremium.IMAX)
```

**Trazabilidad**: `main.py` líneas 28-37

---

### US-005: Consumir Snack en Sala VIP

**Como** cliente de una sala VIP
**Quiero** poder consumir un snack de los incluidos en mi entrada
**Para** disfrutar del servicio exclusivo de la sala.

#### Criterios de Aceptacion

- [x] La sala VIP debe tener un contador de snacks disponibles.
- [x] El método `consumir_snack` debe decrementar el contador en uno.
- [x] Si se intenta consumir un snack y no quedan disponibles, se debe lanzar la excepción `SnacksAgotadosException`.

#### Detalles Tecnicos

**Clase**: `SalaVip` (`python_cinema/entidades/salas/sala_vip.py`)

**Codigo de ejemplo**:
```python
# sala_vip fue creada con 100 snacks
try:
    sala_vip.consumir_snack()
    print(f"Snacks restantes: {sala_vip.snacks_disponibles}")
except SnacksAgotadosException as e:
    print(e.message)
```

**Trazabilidad**: No está en `main.py`, pero es una funcionalidad clave de la entidad `SalaVip`.

---

## Epic 3: Sistema de Precios Dinámicos

### US-006: Monitorear la Demanda del Mercado

**Como** el sistema de precios automatizado
**Quiero** simular una lectura de la demanda del mercado a intervalos regulares
**Para** proveer datos en tiempo real para el ajuste de precios.

#### Criterios de Aceptacion

- [x] El sensor debe ser un objeto `Observable` que notifica a sus observadores.
- [x] Debe simular una lectura de demanda (un valor porcentual) en cada paso.
- [x] La lectura debe generar un `EventoSensor` con el tipo "demanda" y el valor leído.
- [x] Debe notificar a todos los observadores adjuntos con el nuevo evento.

#### Detalles Tecnicos

**Clase**: `DemandaReaderTask` (`python_cinema/reservas/sensores/demanda_reader_task.py`)
**Patrón**: Observer (Observable)

**Codigo de ejemplo**:
```python
from python_cinema.reservas.sensores.demanda_reader_task import DemandaReaderTask

sensor_demanda = DemandaReaderTask()
# ... adjuntar observadores ...
sensor_demanda.run_simulation_step() # Simula un paso y notifica
```

**Trazabilidad**: `main.py` líneas 57, 66

---

### US-007: Controlar Precios Basado en la Demanda

**Como** el sistema de precios automatizado
**Quiero** recibir notificaciones de cambios en la demanda
**Para** reaccionar y decidir si debo cambiar la estrategia de precios.

#### Criterios de Aceptacion

- [x] El controlador debe ser un `Observer` que se suscribe a un `Observable` (el sensor).
- [x] Su método `update` debe recibir el `EventoSensor`.
- [x] Debe analizar el valor de la demanda recibido en el evento.
- [x] Basado en el valor, debe seleccionar una `VentaEntradasStrategy` apropiada.

#### Detalles Tecnicos

**Clase**: `ControlPreciosTask` (`python_cinema/reservas/control/control_precios_task.py`)
**Patrón**: Observer (Observer)

**Codigo de ejemplo**:
```python
from python_cinema.reservas.control.control_precios_task import ControlPreciosTask

controlador_precios = ControlPreciosTask(precio_base_actual=12.50)
sensor_demanda.attach(controlador_precios) # Suscripción

# Cuando sensor_demanda.notify() es llamado, controlador_precios.update() se ejecuta.
```

**Trazabilidad**: `main.py` líneas 60, 63

---

### US-008: Aplicar Estrategias de Cálculo de Precios

**Como** el controlador de precios
**Quiero** aplicar diferentes algoritmos para calcular el precio final de una entrada
**Para** ajustar dinámicamente los ingresos según la demanda del mercado.

#### Criterios de Aceptacion

- [x] Debe existir una interfaz `VentaEntradasStrategy`.
- [x] Deben existir al menos dos implementaciones:
  - `VentaConstanteStrategy`: Devuelve el precio base sin cambios.
  - `VentaEstacionalStrategy`: Ajusta el precio base multiplicándolo por un factor de demanda.
- [x] El `ControlPreciosTask` debe poder cambiar de estrategia dinámicamente.
- [x] El cálculo del precio final se delega al objeto de estrategia actual.

#### Detalles Tecnicos

**Interfaz**: `VentaEntradasStrategy` (`python_cinema/patrones/strategy/venta_entradas_strategy.py`)
**Implementaciones**: `VentaConstanteStrategy`, `VentaEstacionalStrategy`
**Patrón**: Strategy

**Lógica de decisión**:
```python
# Dentro de ControlPreciosTask.update()
if data.valor > 110:  # Si la demanda supera el 110%
    self.strategy = VentaEstacionalStrategy()
else:
    self.strategy = VentaConstanteStrategy()

self.precio_final = self.strategy.calcular_precio(self.precio_base, factor_demanda)
```

**Trazabilidad**: `control_precios_task.py` líneas 16-24

---

## Epic 4: Operaciones de la Cadena

### US-009: Orquestar la Construcción de un Nuevo Complejo

**Como** director ejecutivo de la cadena
**Quiero** un servicio de alto nivel que gestione la construcción completa de un nuevo complejo
**Para** simplificar y centralizar la expansión de la cadena.

#### Criterios de Aceptacion

- [x] El servicio debe orquestar otros servicios de más bajo nivel (`EdificioService`, `ComplejoService`).
- [x] Debe tomar los datos necesarios (ID, nombre, dirección, superficie).
- [x] Debe invocar al servicio de edificios para crear el edificio.
- [x] Debe invocar al servicio de complejos para crear el complejo en ese edificio.
- [x] Debe registrar el nuevo complejo en el registro comercial de la cadena.
- [x] Debe retornar el objeto `Complejo` recién creado.

#### Detalles Tecnicos

**Servicio**: `CadenaDeCinesService` (`python_cinema/servicios/negocio/cadena_de_cines_service.py`)

**Codigo de ejemplo**:
```python
from python_cinema.servicios.negocio.cadena_de_cines_service import CadenaDeCinesService

cadena_service = CadenaDeCinesService()
complejo = cadena_service.construir_nuevo_complejo(
    id_complejo=1,
    nombre="Cine Central",
    direccion="Av. Corrientes 1234",
    superficie=2000.0
)
```

**Trazabilidad**: `main.py` líneas 14, 17-22

---

## Historias Tecnicas (Patrones de Diseno)

### US-TECH-001: Implementar Singleton para el Registro de Servicios

**Como** arquitecto de software
**Quiero** garantizar que exista una única instancia del registro de servicios de salas (`SalaServiceRegistry`)
**Para** asegurar un punto de acceso global y consistente a los servicios de cada tipo de sala.

#### Criterios de Aceptacion

- [x] La clase `SalaServiceRegistry` debe implementar el patrón Singleton.
- [x] Se debe usar un decorador `@singleton` para encapsular la lógica del patrón.
- [x] Múltiples llamadas al constructor deben devolver la misma instancia del objeto.
- [x] La instancia debe inicializar y mantener un diccionario de servicios para cada tipo de sala.

#### Detalles Tecnicos

**Patrón**: Singleton
**Clase**: `SalaServiceRegistry` (`python_cinema/servicios/salas/sala_service_registry.py`)
**Decorador**: `singleton` (`python_cinema/patrones/singleton/__init__.py`)

**Uso**:
```python
from python_cinema.servicios.salas.sala_service_registry import SalaServiceRegistry

registry1 = SalaServiceRegistry()
registry2 = SalaServiceRegistry()

assert registry1 is registry2 # Ambas variables apuntan a la misma instancia
```

**Trazabilidad**: `sala_service_registry.py` línea 9

---

### US-TECH-002: Implementar Factory Method para la Creación de Salas

**Como** arquitecto de software
**Quiero** centralizar la lógica de creación de objetos `Sala` en una `SalaFactory`
**Para** desacoplar el código cliente de las clases concretas de salas y facilitar la adición de nuevos tipos en el futuro.

#### Criterios de Aceptacion

- [x] Crear una clase `SalaFactory` con un método estático `crear_sala`.
- [x] El método debe aceptar un `tipo` de sala (string) y los parámetros necesarios.
- [x] Debe devolver una instancia de la subclase de `Sala` correspondiente (`SalaStandard`, `SalaVip`, etc.).
- [x] Debe manejar la lógica específica de creación, como la asignación de tecnología para `SalaPremium`.
- [x] Debe lanzar `ValueError` si el `tipo` de sala es desconocido.

#### Detalles Tecnicos

**Patrón**: Factory Method
**Clase**: `SalaFactory` (`python_cinema/patrones/factory/sala_factory.py`)

**Implementación**:
```python
class SalaFactory:
    @staticmethod
    def crear_sala(tipo: str, id_sala: int, capacidad: int, precio_base: float, **kwargs) -> Sala:
        if tipo.lower() == "standard":
            return SalaStandard(id_sala, capacidad, precio_base)
        elif tipo.lower() == "vip":
            snacks = kwargs.get("snacks_incluidos", 50)
            return SalaVip(id_sala, capacidad, precio_base, snacks)
        # ... etc.
```

**Trazabilidad**: `sala_factory.py` líneas 9-26

---

### US-TECH-003: Implementar Observer para Precios Dinámicos

**Como** arquitecto de software
**Quiero** implementar el patrón Observer con tipos genéricos (`Observable[T]`, `Observer[T]`)
**Para** notificar cambios en los sensores de mercado a los controladores de forma desacoplada y tipo-segura.

#### Criterios de Aceptacion

- [x] Crear una clase genérica `Observable[T]` con métodos `attach`, `detach` y `notify`.
- [x] Crear una interfaz genérica `Observer[T]` con un método `update`.
- [x] La clase `DemandaReaderTask` debe heredar de `Observable[EventoSensor]`.
- [x] La clase `ControlPreciosTask` debe heredar de `Observer[EventoSensor]`.
- [x] La notificación debe ser segura y pasar el objeto `EventoSensor` a los observadores.

#### Detalles Tecnicos

**Patrón**: Observer
**Clases**: `Observable`, `Observer` (`python_cinema/patrones/observer/`)

**Implementación**:
```python
# Observable
class DemandaReaderTask(Observable[EventoSensor]):
    def run_simulation_step(self):
        # ... crear evento ...
        self.notify(evento)

# Observer
class ControlPreciosTask(Observer[EventoSensor]):
    def update(self, data: EventoSensor) -> None:
        # ... reaccionar al evento ...
```

**Trazabilidad**: `observable.py`, `observer.py`, `demanda_reader_task.py`, `control_precios_task.py`

---

### US-TECH-004: Implementar Strategy para el Cálculo de Precios

**Como** arquitecto de software
**Quiero** implementar algoritmos de cálculo de precios intercambiables usando el patrón Strategy
**Para** permitir que el comportamiento del cálculo de precios cambie dinámicamente en tiempo de ejecución.

#### Criterios de Aceptacion

- [x] Crear una interfaz abstracta `VentaEntradasStrategy` con un método `calcular_precio`.
- [x] Crear implementaciones concretas como `VentaConstanteStrategy` y `VentaEstacionalStrategy`.
- [x] El `ControlPreciosTask` debe contener una referencia a un objeto de estrategia.
- [x] El `ControlPreciosTask` debe delegar la llamada de `calcular_precio` a su objeto de estrategia actual.
- [x] Se debe poder cambiar la estrategia del `ControlPreciosTask` en cualquier momento.

#### Detalles Tecnicos

**Patrón**: Strategy
**Interfaz**: `VentaEntradasStrategy` (`python_cinema/patrones/strategy/venta_entradas_strategy.py`)

**Uso**:
```python
# En ControlPreciosTask
# self.strategy es una instancia de VentaEntradasStrategy
self.precio_final = self.strategy.calcular_precio(self.precio_base, factor_demanda)
```

**Trazabilidad**: `venta_entradas_strategy.py`, `impl/venta_constante_strategy.py`, `impl/venta_estacional_strategy.py`
