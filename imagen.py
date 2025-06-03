from datetime import date

class Imagen:
    def __init__(self, id_imagen, ruta_imagen, descripcion, cantidad_etiquetas, id_usuario):
        self._id_imagen = id_imagen
        self._ruta_imagen = ruta_imagen
        self._descripcion = descripcion
        self._cantidad_etiquetas = cantidad_etiquetas
        self._id_usuario = id_usuario

    # Getters
    def get_id_imagen(self):
        return self._id_imagen

    def get_ruta_imagen(self):
        return self._ruta_imagen

    def get_descripcion(self):
        return self._descripcion

    def get_cantidad_etiquetas(self):
        return self._cantidad_etiquetas

    def get_id_usuario(self):
        return self._id_usuario

    # Setters
    def set_ruta_imagen(self, nueva_ruta):
        self._ruta_imagen = nueva_ruta

    def set_descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion

    def set_cantidad_etiquetas(self, nueva_cantidad):
        self._cantidad_etiquetas = nueva_cantidad

    def set_id_usuario(self, nuevo_id_usuario):
        self._id_usuario = nuevo_id_usuario

    # Métodos principales
    def cargar_imagen(self):
        print(f"Imagen {self._id_imagen} cargada correctamente.")

    def modificar_imagen(self, nueva_ruta, nueva_descripcion, nueva_cantidad):
        self.set_ruta_imagen(nueva_ruta)
        self.set_descripcion(nueva_descripcion)
        self.set_cantidad_etiquetas(nueva_cantidad)
        print("Imagen modificada con éxito.")

    def eliminar_imagen(self):
        print(f"Imagen {self._id_imagen} eliminada del sistema.")
