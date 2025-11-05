from ..venta_entradas_strategy import VentaEntradasStrategy

class VentaConstanteStrategy(VentaEntradasStrategy):
    """Estrategia de precios constantes, ignora la demanda."""
    def calcular_precio(self, precio_base: float, factor_demanda: float) -> float:
        print("Aplicando estrategia de precios constantes.")
        return precio_base
