import unittest
from imagen import Imagen

class TestImagen(unittest.TestCase):
    def test_flujo_imagen(self):
        # Lista vacía 
        lista_imagenes = []  

        # Crear una imagen
        imagen = Imagen(
            id_imagen=101,
            ruta_imagen="etiquetas/logo.png",
            descripcion="Logo para etiquetas premium",
            cantidad_etiquetas=50,
            id_usuario=1
        )

        print("\n--- CARGANDO IMAGEN ---")
        imagen.cargar_imagen(lista_imagenes)  
        self.assertIn(imagen, lista_imagenes)

        print("\n--- DETALLES DE LA IMAGEN ---")
        print("ID:", imagen.get_id_imagen())
        print("Ruta:", imagen.get_ruta_imagen())
        print("Descripción:", imagen.get_descripcion())
        print("Cantidad de etiquetas:", imagen.get_cantidad_etiquetas())
        print("ID Usuario:", imagen.get_id_usuario())

        print("\n--- MODIFICANDO IMAGEN ---")
        imagen.modificar_imagen("etiquetas/logo_v2.png", "Logo actualizado", 75)
        self.assertEqual(imagen.get_ruta_imagen(), "etiquetas/logo_v2.png")
        self.assertEqual(imagen.get_descripcion(), "Logo actualizado")
        self.assertEqual(imagen.get_cantidad_etiquetas(), 75)

        print("\n--- ELIMINANDO IMAGEN ---")
        imagen.eliminar_imagen(lista_imagenes)
        self.assertNotIn(imagen, lista_imagenes)

if __name__ == "__main__":
    unittest.main()
