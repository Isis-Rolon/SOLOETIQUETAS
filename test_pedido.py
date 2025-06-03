import unittest
from datetime import date
from dataclasses import dataclass

# Simulación de la clase Pedido (como si ya estuviera importada desde pedido.py)
class Pedido:
    def __init__(self, id_pedido, fecha_pedido, estado, total, id_usuario, id_imagen):
        self._id_pedido = id_pedido
        self._fecha_pedido = fecha_pedido or date.today()
        self._estado = estado
        self._total = total
        self._id_usuario = id_usuario
        self._id_imagen = id_imagen

    def get_id_pedido(self): return self._id_pedido
    def get_fecha_pedido(self): return self._fecha_pedido
    def get_estado(self): return self._estado
    def get_total(self): return self._total
    def get_id_usuario(self): return self._id_usuario
    def get_id_imagen(self): return self._id_imagen

    def set_fecha_pedido(self, nueva_fecha): self._fecha_pedido = nueva_fecha
    def set_estado(self, nuevo_estado): self._estado = nuevo_estado
    def set_total(self, nuevo_total): self._total = nuevo_total
    def set_id_usuario(self, nuevo_id_usuario): self._id_usuario = nuevo_id_usuario
    def set_id_imagen(self, nuevo_id_imagen): self._id_imagen = nuevo_id_imagen

    def generar_pedido(self):
        print(f"Pedido {self._id_pedido} generado para el usuario {self._id_usuario}.")

    def actualizar_estado(self, nuevo_estado):
        self._estado = nuevo_estado
        print(f"Estado del pedido {self._id_pedido} actualizado a '{self._estado}'.")

    def cancelar_pedido(self):
        self._estado = "cancelado"
        print(f"Pedido {self._id_pedido} ha sido cancelado.")

# Test para la clase Pedido
class TestPedido(unittest.TestCase):
    def test_flujo_pedido(self):
        pedido = Pedido(
            id_pedido=5001,
            fecha_pedido=date(2025, 5, 28),
            estado="pendiente",
            total=15000,
            id_usuario=1,
            id_imagen=101
        )

        print("\n--- DETALLES DEL PEDIDO ---")
        print("ID Pedido:", pedido.get_id_pedido())
        print("Fecha:", pedido.get_fecha_pedido())
        print("Estado:", pedido.get_estado())
        print("Total:", pedido.get_total())
        print("ID Usuario:", pedido.get_id_usuario())
        print("ID Imagen:", pedido.get_id_imagen())

        pedido.generar_pedido()

        print("\n--- ACTUALIZANDO ESTADO ---")
        pedido.actualizar_estado("en proceso")
        self.assertEqual(pedido.get_estado(), "en proceso")

        print("\n--- CANCELANDO PEDIDO ---")
        pedido.cancelar_pedido()
        self.assertEqual(pedido.get_estado(), "cancelado")

if __name__ == "__main__":
    unittest.main()
