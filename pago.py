from datetime import date

class Pago:
    def __init__(self, id_pago, id_pedido, monto, fecha_pago, metodo_pago, estado_pago="pendiente"):
        self._id_pago = id_pago
        self._id_pedido = id_pedido
        self._monto = monto
        self._fecha_pago = fecha_pago
        self._metodo_pago = metodo_pago
        self._estado_pago = estado_pago

    # Getters
    def get_id_pago(self): return self._id_pago
    def get_id_pedido(self): return self._id_pedido
    def get_monto(self): return self._monto
    def get_fecha_pago(self): return self._fecha_pago
    def get_metodo_pago(self): return self._metodo_pago
    def get_estado_pago(self): return self._estado_pago

    # Setters
    def set_monto(self, nuevo_monto): self._monto = nuevo_monto
    def set_fecha_pago(self, nueva_fecha): self._fecha_pago = nueva_fecha
    def set_metodo_pago(self, nuevo_metodo): self._metodo_pago = nuevo_metodo
    def set_estado_pago(self, nuevo_estado): self._estado_pago = nuevo_estado

    # Métodos principales
    def procesar_pago(self):
        self._estado_pago = "realizado"
        print(f"Pago procesado con éxito. Estado: {self._estado_pago}")

    def cancelar_pago(self):
        self._estado_pago = "cancelado"
        print(f"Pago cancelado. Estado: {self._estado_pago}")

    def ver_detalle_pago(self):
        print("\n--- DETALLES DEL PAGO ---")
        print(f"ID Pago: {self._id_pago}")
        print(f"ID Pedido: {self._id_pedido}")
        print(f"Monto: ${self._monto}")
        print(f"Fecha de Pago: {self._fecha_pago}")
        print(f"Método de Pago: {self._metodo_pago}")
        print(f"Estado: {self._estado_pago}")
