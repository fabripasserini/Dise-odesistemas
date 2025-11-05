"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/PythonCinema/python_cinema/patrones/singleton
Fecha: 2025-11-04 20:59:22
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: __init__.py
# Ruta: /home/fabri/PythonCinema/python_cinema/patrones/singleton/__init__.py
# ================================================================================

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


