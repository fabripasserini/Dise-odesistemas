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
