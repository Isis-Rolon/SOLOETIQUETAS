import unittest
from datetime import date
from imagen import Imagen
from pedido import Pedido

class TestPedido(unittest.TestCase):
    def test_pedido_con_imagenes(self):
        # Creamos imágenes como objetos reales
        imagen1 = Imagen(1, "etiqueta1.png", "Etiqueta promocional", 30, 1)
        imagen2 = Imagen(2, "etiqueta2.png", "Etiqueta institucional", 50, 1)

        # Creamos un pedido con esas imágenes
        pedido = Pedido(
            id_pedido=5001,
            fecha_pedido=date.today(),
            id_usuario=1,
            id_envio=101,
            id_pago=301,
            lista_de_imagenes=[imagen1, imagen2]
        )

        # Calculamos el total según cantidad de etiquetas
        pedido.calcular_total(precio_unitario=1500)
        self.assertEqual(pedido.get_total(), 120000)

        # DETALLES DEL PEDIDO
        print("\n--- DETALLES DEL PEDIDO ---")
        print("ID Pedido:", pedido.get_id_pedido())
        print("Fecha:", pedido.get_fecha_pedido())
        print("Estado:", pedido.get_estado())
        print("Total:", pedido.get_total())
        print("ID Usuario:", pedido.get_id_usuario())
        print("ID Envío:", pedido.get_id_envio())
        print("ID Pago:", pedido.get_id_pago())
        print("Imágenes asociadas:")
        for img in pedido.get_lista_imagenes():
            print(f" - ID: {img.get_id_imagen()}, Ruta: {img.get_ruta_imagen()}, Cantidad: {img.get_cantidad_etiquetas()}")

        # Simulación de proceso del pedido
        pedido.generar_pedido()
        pedido.actualizar_estado("en proceso")
        self.assertEqual(pedido.get_estado(), "en proceso")

        pedido.cancelar_pedido()
        self.assertEqual(pedido.get_estado(), "cancelado")

if __name__ == "__main__":
    unittest.main()
