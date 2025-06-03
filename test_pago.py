import unittest
from datetime import date
from pago import Pago

class TestPago(unittest.TestCase):
    def test_flujo_pago(self):
        pago = Pago(
            id_pago=301,
            id_pedido=1001,
            monto=18000,
            fecha_pago=date.today(),
            metodo_pago="Transferencia"
        )

        print("\n--- DATOS INICIALES DEL PAGO ---")
        pago.ver_detalle_pago()

        # Procesar pago
        print("\n--- PROCESAR PAGO ---")
        pago.procesar_pago()
        self.assertEqual(pago.get_estado_pago(), "realizado")

        # Cancelar pago
        print("\n--- CANCELAR PAGO ---")
        pago.cancelar_pago()
        self.assertEqual(pago.get_estado_pago(), "cancelado")

        print("\n--- DATOS FINALES DEL PAGO ---")
        pago.ver_detalle_pago()

if __name__ == "__main__":
    unittest.main()
