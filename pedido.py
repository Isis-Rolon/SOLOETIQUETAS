from datetime import date

class Pedido:
    def __init__(self, id_pedido, fecha_pedido, estado, total, id_usuario, id_imagen):
        self._id_pedido = id_pedido
        self._fecha_pedido = fecha_pedido or date.today()
        self._total = total
        self._id_usuario = id_usuario
        self._id_imagen = id_imagen

    # Getters
    def get_id_pedido(self):
        return self._id_pedido

    def get_fecha_pedido(self):
        return self._fecha_pedido

    def get_estado(self):
        return self._estado

    def get_total(self):
        return self._total

    def get_id_usuario(self):
        return self._id_usuario

    def get_id_imagen(self):
        return self._id_imagen

    # Setters
    def set_fecha_pedido(self, nueva_fecha):
        self._fecha_pedido = nueva_fecha

    def set_estado(self, nuevo_estado):
        self._estado = nuevo_estado

    def set_total(self, nuevo_total):
        self._total = nuevo_total

    def set_id_usuario(self, nuevo_id_usuario):
        self._id_usuario = nuevo_id_usuario

    def set_id_imagen(self, nuevo_id_imagen):
        self._id_imagen = nuevo_id_imagen

    # Métodos adicionales
    def generar_pedido(self):
        print(f"Pedido {self._id_pedido} generado para el usuario {self._id_usuario}.")

    def actualizar_estado(self, nuevo_estado):
        self._estado = nuevo_estado
        print(f"Estado del pedido {self._id_pedido} actualizado a '{self._estado}'.")

    def cancelar_pedido(self):
        self._estado = "cancelado"
        print(f"Pedido {self._id_pedido} ha sido cancelado.")
