# Sistema de Gestión de Cine

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Sistema integral de gestión de complejos cinematográficos que demuestra la implementación de múltiples patrones de diseño de software con enfoque educativo y profesional.

---

## Tabla de Contenidos

- [Contexto del Dominio](#contexto-del-dominio)
- [Características Principales](#caracteristicas-principales)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Patrones de Diseño Implementados](#patrones-de-diseno-implementados)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación](#instalacion)
- [Uso del Sistema](#uso-del-sistema)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Módulos del Sistema](#modulos-del-sistema)
- [Documentación Técnica](#documentacion-tecnica)
- [Testing y Validación](#testing-y-validacion)
- [Contribución](#contribucion)
- [Licencia](#licencia)

---

## Contexto del Dominio

### Problema que Resuelve

El sistema **PythonCinema** aborda los desafíos de la gestión moderna de complejos cinematográficos, un dominio que requiere:

1. **Gestión de Múltiples Tipos de Salas**
   - Salas Standard para películas comerciales con tecnología 2D
   - Salas Premium con tecnologías avanzadas (3D, IMAX, Dolby Atmos)
   - Salas VIP con butacas reclinables y servicio premium
   - Salas Mini para cine arte e independiente
   - Cada tipo con características y capacidades particulares

2. **Monitoreo de Demanda en Tiempo Real**
   - Sensores de demanda y ocupación que operan continuamente
   - Sistema de precios automatizado basado en condiciones de mercado
   - Respuesta dinámica a cambios en la afluencia de público

3. **Gestión de Recursos Humanos**
   - Control de empleados con certificaciones de manipulación
   - Asignación y seguimiento de turnos laborales
   - Equipos técnicos con certificaciones específicas

4. **Planificación Espacial**
   - Optimización del uso de superficie disponible
   - Registro comercial de edificios cinematográficos
   - Control de salas y distribución espacial

5. **Persistencia y Trazabilidad**
   - Almacenamiento permanente de registros comerciales
   - Recuperación de históricos para auditoría
   - Valuación de propiedades y avalúos

### Actores del Sistema

- **Propietario de Complejo**: Gestiona el registro comercial, supervisa operaciones
- **Empleado de Cine**: Ejecuta turnos de atención, venta y limpieza
- **Sistema de Reservas Automatizado**: Opera de forma autónoma basado en sensores
- **Auditor/Inspector**: Consulta registros persistidos para verificación

### Flujo de Operaciones Típico
```
1. REGISTRO --> Se crea un registro comercial con edificio y complejo
2. CREACIÓN DE SALAS --> Se agregan salas según superficie disponible
3. MONITOREO --> Sensores detectan demanda y ocupación continuamente
4. AJUSTE DE PRECIOS --> Sistema aplica descuentos cuando se cumplen condiciones
5. PROGRAMACIÓN --> Salas venden entradas según estrategias específicas
6. TURNOS --> Empleados ejecutan tareas con equipos asignados
7. CIERRE/REAPERTURA --> Se gestionan cierres temporales por tipo de sala
8. PERSISTENCIA --> Datos se guardan para auditoría futura
```

---

## Características Principales

### Funcionalidades del Sistema

#### 1. Gestión de Salas

- **Creación dinámica** de 4 tipos de salas mediante Factory Pattern
  - **Standard**: Sala convencional con tecnología 2D
  - **Premium**: Sala con tecnología avanzada (3D, IMAX, Dolby Atmos)
  - **VIP**: Sala de lujo con butacas reclinables y servicio a la sala
  - **Mini**: Sala compacta para cine arte e independiente

- **Venta de entradas diferenciada** por tipo
  - Salas Standard/Premium: Venta estacional (200 entradas verano, 100 temporada baja)
  - Salas VIP/Mini: Venta constante (50-80 entradas independiente de temporada)

- **Registro de ingresos automático** para cada sala
  - Standard: $10 por entrada
  - Premium: $15 por entrada
  - VIP: $25 por entrada
  - Mini: $8 por entrada

#### 2. Sistema de Reservas Inteligente

- **Sensores en tiempo real** (patrón Observer)
  - Sensor de demanda: lecturas cada 2 segundos
  - Sensor de ocupación: lecturas cada 3 segundos
  - Rangos: 0 a 500 personas, 0% a 100% ocupación

- **Ajuste de precios automatizado condicional**
  - Se activa cuando:
    - Demanda menor a 100 personas, Y
    - Ocupación menor a 40%
  - Control cada 2.5 segundos
  - Descuento configurable (20% por defecto)

- **Notificaciones de eventos**
  - Eventos de sensores a observadores suscritos
  - Sistema tipo-seguro con Generics (Observable[int], Observable[float])

#### 3. Gestión de Personal

- **Empleados con certificación de manipulación**
  - Certificado obligatorio para trabajar en confitería
  - Validación automática antes de ejecutar turnos
  - Fecha de emisión y observaciones

- **Sistema de turnos**
  - Asignación múltiple de turnos por empleado
  - Ejecución ordenada por ID (descendente)
  - Estado de turnos (pendiente/completado)
  - Fecha programada para cada turno

- **Equipos certificados**
  - ID único, nombre y certificación técnica
  - Asignación a empleados durante turnos

#### 4. Gestión de Infraestructura

- **Edificio**
  - CUIT único
  - Superficie total en metros cuadrados
  - Dirección de ubicación

- **Complejo**
  - Nombre identificatorio
  - Control de superficie disponible
  - Lista de salas activas
  - Capacidad de snacks en unidades
  - Empleados asignados

- **Registro Comercial**
  - Vincula edificio con complejo
  - Propietario y valuación fiscal
  - Persistible en disco

#### 5. Operaciones de Negocio

- **Creación de salas automatizada**
  - Cálculo de superficie requerida
  - Validación de espacio disponible
  - Creación vía Factory Method

- **Programación de funciones centralizada**
  - Programa todas las salas del complejo
  - Verifica snacks disponibles antes de programar
  - Excepción si snacks insuficientes

- **Cierre/reapertura tipada**
  - Cierre selectivo por tipo de sala
  - Agrupamiento en contenedores genéricos tipo-seguros
  - Mostración de contenido de grupos

- **Mantenimiento**
  - Aplicación de mantenimiento a todo el complejo
  - Registro de tipo de mantenimiento realizado

#### 6. Persistencia de Datos

- **Serialización con Pickle**
  - Guardado completo de RegistroComercial
  - Directorio configurable (default: `data/`)
  - Nombre de archivo: `{propietario}.dat`

- **Recuperación de datos**
  - Lectura de registros persistidos
  - Validación de integridad
  - Manejo de excepciones específicas

---

## Arquitectura del Sistema

### Principios Arquitectónicos

El sistema está diseñado siguiendo principios SOLID:

- **Single Responsibility**: Cada clase tiene una única razón para cambiar
- **Open/Closed**: Abierto a extensión, cerrado a modificación
- **Liskov Substitution**: Subtipos intercambiables
- **Interface Segregation**: Interfaces específicas
- **Dependency Inversion**: Dependencias de abstracciones

### Separación de Capas
```
+----------------------------------+
|        PRESENTACIÓN              |
|  (main.py - Demostración CLI)    |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE NEGOCIO        |
|  (CadenadeCinesService,          |
|   GrupoCierre)                   |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE DOMINIO        |
|  (ComplejoService, etc.)         |
+----------------------------------+
                |
                v
+----------------------------------+
|          ENTIDADES               |
|  (Sala, Edificio, Empleado)      |
+----------------------------------+
                |
                v
+----------------------------------+
|      PATRONES / UTILIDADES       |
|  (Factory, Strategy, Observer)   |
+----------------------------------+
```

---

## Patrones de Diseño Implementados

### 1. SINGLETON Pattern

**Ubicación**: `python_cinema/servicios/salas/sala_service_registry.py`

**Problema que resuelve**:
- Garantizar una única instancia del registro de servicios
- Compartir estado entre todos los servicios del sistema

**Implementación**:
```python
class SalaServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

### 2. FACTORY METHOD Pattern

**Ubicación**: `python_cinema/patrones/factory/sala_factory.py`

**Problema que resuelve**:
- Creación de salas sin conocer clases concretas
- Extensibilidad para nuevos tipos de salas

### 3. OBSERVER Pattern

**Ubicación**: `python_cinema/patrones/observer/`

**Problema que resuelve**:
- Notificación automática a múltiples observadores
- Sistema de eventos tipo-seguro

### 4. STRATEGY Pattern

**Ubicación**: `python_cinema/patrones/strategy/`

**Problema que resuelve**:
- Algoritmos de venta intercambiables
- Eliminar condicionales tipo if/else

### 5. REGISTRY Pattern

**Ubicación**: `python_cinema/servicios/salas/sala_service_registry.py`

**Problema que resuelve**:
- Eliminar cascadas de `isinstance()`
- Dispatch polimórfico basado en tipo

---

## Requisitos del Sistema

- **Python 3.13** o superior
- **Sistema Operativo**: Windows, Linux, macOS
- **RAM**: Mínimo 512 MB
- **Disco**: 50 MB libres

---

## Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/usuario/python-cinema.git
cd python-cinema
```

### 2. Crear Entorno Virtual

#### Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Ejecutar Sistema
```bash
python main.py
```

---

## Uso del Sistema

### Ejemplo Básico
```python
from python_cinema.servicios.infraestructura.edificio_service import EdificioService
from python_cinema.servicios.infraestructura.complejo_service import ComplejoService

# Crear edificio con complejo
edificio_service = EdificioService()
edificio = edificio_service.crear_edificio_con_complejo(
    cuit=20388887341,
    superficie=5000.0,
    direccion="Av. San Martín 1234, Mendoza",
    nombre_complejo="Cinépolis Mendoza Plaza"
)

# Obtener complejo
complejo = edificio.get_complejo()

# Agregar salas
complejo_service = ComplejoService()
complejo_service.agregar_sala(complejo, "Standard", 3)
complejo_service.agregar_sala(complejo, "Premium", 2)

# Programar funciones
complejo_service.programar_funciones(complejo)
```

---

## Licencia

MIT License - Ver archivo LICENSE para más detalles

---

**Última actualización**: Noviembre 2025  
**Versión del sistema**: 1.0.0  
**Python requerido**: 3.13+
