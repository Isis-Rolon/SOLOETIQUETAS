import unittest
from datetime import date
from usuario import UsuarioCliente, UsuarioAdministrador

class TestUsuarioCliente(unittest.TestCase):
    def test_registro_cliente(self):
        cliente = UsuarioCliente(
            id_usuario=1,
            nombre="Lucía",
            apellido="Ramírez",
            email="lucia@mail.com",
            contrasena="abc123",
            fecha_registro=date.today(),
            direccion="Calle 123",
            telefono="1234567890"
        )

        print("\n--- REGISTRO CLIENTE ---")
        print("Nombre:", cliente.get_nombre())
        print("Apellido:", cliente.get_apellido())
        print("Email:", cliente.get_email())
        print("Dirección:", cliente.get_direccion())
        print("Teléfono:", cliente.get_telefono())

        cliente.registrar()
        self.assertTrue(cliente.iniciar_sesion("lucia@mail.com", "abc123"))

        # Métodos específicos del cliente
        cliente.realizar_pedido()
        cliente.ver_historial_pedidos()
        cliente.seleccionar_etiqueta()

        # Test para editar datos
        cliente.editar_datos(
            nuevo_nombre="Lu",
            nuevo_apellido="Fernández",
            nuevo_email="lufernandez@mail.com",
            nueva_direccion="Avenida 456",
            nuevo_telefono="987654321"
        )

        print("\n--- DATOS ACTUALIZADOS ---")
        print("Nuevo nombre:", cliente.get_nombre())
        print("Nuevo apellido:", cliente.get_apellido())
        print("Nuevo email:", cliente.get_email())
        print("Nueva dirección:", cliente.get_direccion())
        print("Nuevo teléfono:", cliente.get_telefono())

        self.assertEqual(cliente.get_nombre(), "Lu")
        self.assertEqual(cliente.get_apellido(), "Fernández")
        self.assertEqual(cliente.get_email(), "lufernandez@mail.com")
        self.assertEqual(cliente.get_direccion(), "Avenida 456")
        self.assertEqual(cliente.get_telefono(), "987654321")


class TestUsuarioAdministrador(unittest.TestCase):
    def test_login_admin(self):
        admin = UsuarioAdministrador(
            id_usuario=99,
            nombre="Carlos",
            apellido="Pérez",
            email="admin@empresa.com",
            contrasena="admin123",
            fecha_registro=date.today(),
            cargo="Supervisor",
            turno="Mañana"
        )

        print("\n--- LOGIN ADMINISTRADOR ---")
        print("Nombre:", admin.get_nombre())
        print("Apellido:", admin.get_apellido())
        print("Email:", admin.get_email())
        print("Cargo:", admin.get_cargo())
        print("Turno:", admin.get_turno())

        self.assertTrue(admin.iniciar_sesion("admin@empresa.com", "admin123"))
        self.assertFalse(admin.iniciar_sesion("admin@empresa.com", "claveErrada"))

        # Métodos del administrador
        admin.gestionar_usuarios()
        admin.ver_pedidos_de_cliente()

if __name__ == "__main__":
    unittest.main()
