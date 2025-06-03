import unittest
from metodo_envio import MetodoDeEnvio

class TestMetodoDeEnvio(unittest.TestCase):
    def mostrar_datos_envio(self, envio):
        print("\n--- DETALLES DEL ENVÍO ---")
        print("ID:", envio.get_id_envio())
        print("Tipo:", envio.get_tipo_envio())
        print("Zona:", envio.get_zona())
        print("Dirección:", envio.get_direccion())
        print("Departamento:", envio.get_departamento())
        print("Piso:", envio.get_piso())
        print("Código Postal:", envio.get_codigo_postal())
        print("Observación:", envio.get_observacion())
        print("Costo:", envio.get_costo())

    def test_zona_capital(self):
        envio = MetodoDeEnvio(
            id_envio=1,
            tipo_envio="Correo",
            zona="Capital",
            direccion="Av. Corrientes 1234",
            departamento="A",
            piso="3",
            codigo_postal="C1043AAB",
            observacion="Entregar por la tarde",
            costo=0
        )
        print("Zona Capital")
        self.mostrar_datos_envio(envio)
        envio.calcular_costo()
        self.assertEqual(envio.get_costo(), 2500)

    def test_zona_provincia(self):
        envio = MetodoDeEnvio(
            id_envio=2,
            tipo_envio="Domicilio",
            zona="Provincia",
            direccion="Calle Falsa 123",
            departamento="B",
            piso="2",
            codigo_postal="B2000XYZ",
            observacion="Llamar antes de entregar",
            costo=0
        )
        print("Zona Provincia")
        self.mostrar_datos_envio(envio)
        envio.calcular_costo()
        self.assertEqual(envio.get_costo(), 4000)

    def test_zona_otro(self):
        envio = MetodoDeEnvio(
            id_envio=3,
            tipo_envio="Retiro",
            zona="Interior",
            direccion="Ruta 9 km 1123",
            departamento="C",
            piso="1",
            codigo_postal="X5000ABC",
            observacion="Entregar en horario laboral",
            costo=0
        )
        print("Zona Interior")
        self.mostrar_datos_envio(envio)
        envio.calcular_costo()
        self.assertEqual(envio.get_costo(), 4500)

if __name__ == "__main__":
    unittest.main()
