from datetime import date
from imagen import Imagen

class Pedido:
    def __init__(self, id_pedido, fecha_pedido, id_usuario, id_envio, id_pago, lista_de_imagenes):
        self._id_pedido = id_pedido
        self._fecha_pedido = fecha_pedido or date.today()
        self._id_usuario = id_usuario
        self._id_envio = id_envio
        self._id_pago = id_pago
        self._lista_de_imagenes = lista_de_imagenes  # lista de objetos Imagen
        self._estado = "pendiente"
        self._total = 0  # se calcula con lógica

    # Getters
    def get_id_pedido(self): return self._id_pedido
    def get_fecha_pedido(self): return self._fecha_pedido
    def get_total(self): return self._total
    def get_id_usuario(self): return self._id_usuario
    def get_id_envio(self): return self._id_envio
    def get_id_pago(self): return self._id_pago
    def get_estado(self): return self._estado
    def get_lista_imagenes(self): return self._lista_de_imagenes

    # Setters
    def set_fecha_pedido(self, nueva_fecha): self._fecha_pedido = nueva_fecha
    def set_total(self, nuevo_total): self._total = nuevo_total
    def set_id_usuario(self, nuevo_id_usuario): self._id_usuario = nuevo_id_usuario
    def set_id_envio(self, nuevo_id_envio): self._id_envio = nuevo_id_envio
    def set_id_pago(self, nuevo_id_pago): self._id_pago = nuevo_id_pago
    def set_estado(self, nuevo_estado): self._estado = nuevo_estado
    def set_lista_imagenes(self, nueva_lista): self._lista_de_imagenes = nueva_lista

    # Metodos adicionales
    def calcular_total(self, precio_unitario):
        total = 0
        for imagen in self._lista_de_imagenes:
            total += imagen.get_cantidad_etiquetas() * precio_unitario
        self._total = total
        print(f"Total calculado para el pedido {self._id_pedido}: ${self._total}")

    def generar_pedido(self):
        print(f"Pedido {self._id_pedido} generado para el usuario {self._id_usuario}.")

    def actualizar_estado(self, nuevo_estado):
        self._estado = nuevo_estado
        print(f"Estado del pedido {self._id_pedido} actualizado a '{self._estado}'.")

    def cancelar_pedido(self):
        self._estado = "cancelado"
        print(f"Pedido {self._id_pedido} ha sido cancelado.")
