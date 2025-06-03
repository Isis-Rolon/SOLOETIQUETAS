from datetime import date

class MetodoDeEnvio:
    def __init__(self, id_envio, tipo_envio, zona, direccion, departamento, piso, codigo_postal, observacion, costo):
        self._id_envio = id_envio
        self._tipo_envio = tipo_envio
        self._zona = zona
        self._direccion = direccion
        self._departamento = departamento
        self._piso = piso
        self._codigo_postal = codigo_postal
        self._observacion = observacion
        self._costo = costo

    # Getters
    def get_id_envio(self): return self._id_envio
    def get_tipo_envio(self): return self._tipo_envio
    def get_zona(self): return self._zona
    def get_direccion(self): return self._direccion
    def get_departamento(self): return self._departamento
    def get_piso(self): return self._piso
    def get_codigo_postal(self): return self._codigo_postal
    def get_observacion(self): return self._observacion
    def get_costo(self): return self._costo

    # Setters
    def set_tipo_envio(self, tipo): self._tipo_envio = tipo
    def set_zona(self, zona): self._zona = zona
    def set_direccion(self, direccion): self._direccion = direccion
    def set_departamento(self, departamento): self._departamento = departamento
    def set_piso(self, piso): self._piso = piso
    def set_codigo_postal(self, codigo): self._codigo_postal = codigo
    def set_observacion(self, observacion): self._observacion = observacion
    def set_costo(self, nuevo_costo): self._costo = nuevo_costo

    # Método principal
    def calcular_costo(self):
        if self._zona.lower() == "capital":
            self._costo = 2500
        elif self._zona.lower() == "provincia":
            self._costo = 4000
        else:
            self._costo = 4500  # costo para otras zonas
        print(f"El costo de envío calculado es: ${self._costo}")
