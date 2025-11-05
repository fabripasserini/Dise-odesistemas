from ..venta_entradas_strategy import VentaEntradasStrategy

class VentaEstacionalStrategy(VentaEntradasStrategy):
    """Estrategia de precios que varía con la demanda."""
    def calcular_precio(self, precio_base: float, factor_demanda: float) -> float:
        # factor_demanda es un % (ej: 1.2 para 120% de demanda)
        precio_ajustado = precio_base * factor_demanda
        print(f"Aplicando estrategia estacional. Demanda: {factor_demanda:.2f}, Precio ajustado: ${precio_ajustado:.2f}")
        return precio_ajustado
