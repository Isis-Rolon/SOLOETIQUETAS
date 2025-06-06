import unittest
from datetime import date
from pedido import Pedido

class TestPedido(unittest.TestCase):
    def test_flujo_pedido(self):
        pedido = Pedido(
            id_pedido=102,
            fecha_pedido=date(2025, 5, 28),
            total=0,  # ← se calcula después
            id_usuario=1,
            id_envio=1001,
            id_pago=202,
            lista_de_imagenes=["etiqueta1.png", "etiqueta2.png"]
        )

        # Calcula el total: 2 imágenes × $1500 cada una
        pedido.calcular_total(precio_unitario=1500)

        print("\n--- DETALLES DEL PEDIDO ---")
        print("ID Pedido:", pedido.get_id_pedido())
        print("Fecha:", pedido.get_fecha_pedido())
        print("Estado:", pedido.get_estado())
        print("Total:", pedido.get_total())  # debería dar 3000
        print("ID Usuario:", pedido.get_id_usuario())
        print("ID Envío:", pedido.get_id_envio())
        print("ID Pago:", pedido.get_id_pago())
        print("Imágenes:", pedido.get_lista_imagenes())

        # Verifica que el total sea correcto
        self.assertEqual(pedido.get_total(), 3000)

        pedido.generar_pedido()

        print("\n--- ACTUALIZANDO ESTADO ---")
        pedido.actualizar_estado("en proceso")
        self.assertEqual(pedido.get_estado(), "en proceso")

        print("\n--- CANCELANDO PEDIDO ---")
        pedido.cancelar_pedido()
        self.assertEqual(pedido.get_estado(), "cancelado")


if __name__ == "__main__":
    unittest.main()
