from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime


class Cliente:

    def __init__(self, rut_cliente, nombre, email, telefono, tipo_cliente):
        self._rut_cliente = rut_cliente
        self._email = email
        self._telefono = telefono
        self._nombre = nombre
        self.tipo_cliente = tipo_cliente

    # --- GETTER Y SETTER PARA NOMBRE ---
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # --- GETTER PARA ID (Solo lectura, no tiene setter) ---
    @property
    def rut_cliente(self):
        return self._rut_cliente

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor

    @property
    def tipo_cliente(self):
        return self._tipo_cliente

    @tipo_cliente.setter
    def tipo_cliente(self, valor):
        self._tipo_cliente = valor

    def to_dict(self):
        return {
            "rut": self.rut_cliente,
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono,
            "tipo": self.tipo_cliente,
            "fecha registro": date.today().strftime("%d-%m-%Y"),
        }


class ClientePremium(Cliente):
    def __init__(
        self,
        rut_cliente,
        nombre,
        email,
        telefono,
        tipo_cliente,
        descuento,
        fecha_caducidad,
    ):
        super().__init__(rut_cliente, nombre, email, telefono, "Premium")
        self._descuento = descuento
        self._fecha_caducidad = fecha_caducidad

    @property
    def descuento(self):
        return self._descuento

    @descuento.setter
    def descuento(self, valor):
        if 0 < valor < 1:
            self._descuento = valor
        else:
            print("Error: El descuento debe estar entre 0 y 1.")

    @property
    def fecha_caducidad(self):
        return self._fecha_caducidad

    @fecha_caducidad.setter
    def fecha_caducidad(self, valor):
        self._fecha_caducidad = valor

    def to_dict(self):
        data = super().to_dict()
        data["descuento"] = self.descuento
        data["fecha caducidad"] = (date.today() + relativedelta(months=+6)).strftime(
            "%d-%m-%Y"
        )
        return data


class ClienteRegular(Cliente):
    def __init__(
        self, rut_cliente, nombre, email, telefono, tipo_cliente, puntos_acumulados=0
    ):
        super().__init__(rut_cliente, nombre, email, telefono, "Regular")
        self.puntos_acumulados = puntos_acumulados

    @property
    def puntos_acumulados(self):
        return self._puntos_acumulados

    @puntos_acumulados.setter
    def puntos_acumulados(self, valor):
        self._puntos_acumulados = valor

    def acumular_puntos(self, puntos):
        self.puntos_acumulados += puntos

    def to_dict(self):
        data = super().to_dict()
        data["puntos acumulados"] = self.puntos_acumulados
        return data


class ClienteCorporativo(Cliente):
    def __init__(
        self,
        rut_cliente,
        nombre,
        email,
        telefono,
        tipo_cliente,
        rut_empresa,
        razon_social,
        limite_credito,
    ):
        super().__init__(rut_cliente, nombre, email, telefono, "Corporativo")
        self.rut_empresa = rut_empresa
        self.razon_social = razon_social
        self.limite_credito = limite_credito

    @property
    def rut_empresa(self):
        return self._rut_empresa

    @rut_empresa.setter
    def rut_empresa(self, valor):
        self._rut_empresa = valor

    @property
    def razon_social(self):
        return self._razon_social

    @razon_social.setter
    def razon_social(self, valor):
        self._razon_social = valor

    @property
    def limite_credito(self):
        return self._limite_credito

    @limite_credito.setter
    def limite_credito(self, valor):
        self._limite_credito = valor

    def to_dict(self):
        data = super().to_dict()
        data["rut empresa"] = self.rut_empresa
        data["razon social"] = self.razon_social
        data["limite credito"] = self.limite_credito
        return data
