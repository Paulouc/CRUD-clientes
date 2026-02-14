from datetime import datetime
import cargarDatos as cd, cliente as cl


class Cliente:

    def __init__(self, rut_cliente, nombre, email, telefono, tipo_cliente):
        self._rut_cliente = rut_cliente
        self._email = email
        self._telefono = telefono

        # Usar setters para aplicar validaciones desde el inicio
        self.nombre = nombre
        self.tipo_cliente = tipo_cliente

    # --- GETTER Y SETTER PARA NOMBRE ---
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 2:
            self._nombre = nuevo_nombre
        else:
            print("Error: El nombre es demasiado corto.")

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
            "fecha registro": datetime.now().strftime("%d-%m-%Y"),
        }


"""
    def agregarCliente():
        

    def editarCliente():
        sistema = cd.SistemaGestion()
        rut = input("Ingrese el rut del cliente a editar: ")
        if rut in sistema.base_datos_clientes:
            cliente = sistema.base_datos_clientes[rut]
            print(f"seleccione el campo a modificar")
            print("1. Nombre")
            print("2. Mail")
            print("3. Telefono")

            if cliente["tipo"] == "premium":
                print("4. Descuento")
                print("5. Fecha de caducidad")
            elif cliente["tipo"] == "corporativo":
                print("4. Rut Empresa")
                print("5. Razon Social")
                print("6. Limite de credito")
            else:
                print("4. Puntos acumulados")
            opcion = input("Ingrese una opcion: ")
            match opcion:
                case "1":
                    nombre = input("Ingrese el nuevo nombre: ")
                    cliente["nombre"] = nombre
                case "2":
                    mail = input("Ingrese el nuevo mail: ")
                    cliente["email"] = mail
                case "3":
                    telefono = input("Ingrese el nuevo telefono: ")
                    cliente["telefono"] = telefono

                case "4":
                    if cliente["tipo"] == "premium":
                        descuento = float(input("Ingrese el nuevo descuento: "))
                        cliente["descuento"] = descuento
                    elif cliente["tipo"] == "corporativo":
                        rut_empresa = input("Ingrese el nuevo rut empresa: ")
                        cliente["rut_empresa"] = rut_empresa
                    elif cliente["tipo"] == "regular":
                        puntos_acumulados = float(
                            input("Ingrese los nuevos puntos acumulados: ")
                        )
                        cliente["puntos_acumulados"] = puntos_acumulados
                case "5":
                    if cliente["tipo"] == "premium":
                        caduca = input("Ingrese el nuevo descuento: ")
                        cliente["fecha_caducidad"] = caduca
                    elif cliente["tipo"] == "corporativo":
                        razon_social = input("Ingrese la nueva razon social: ")
                        cliente["rut_empresa"] = rut_empresa
                    else:
                        print("opcion invalida")
                case "6":
                    if cliente["tipo"] == "corporativo":
                        lc = float(input("Ingrese el nuevo monto limite: "))
                        cliente["limite_credito"] = lc
                    else:
                        print("opcion invalida")
                case _:
                    print("opcion invalida")

            sistema.actualizar_cliente(cliente)
            print(cliente)

    def eliminarCliente():
        sistema = cd.SistemaGestion()
        rut = input("Ingrese el rut del cliente a eliminar: ")
        if rut in sistema.base_datos_clientes:
            del sistema.base_datos_clientes[rut]
            sistema.actualizar_cliente(sistema.base_datos_clientes)
"""


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
        data["fecha caducidad"] = self.fecha_caducidad
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
