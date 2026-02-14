def agregarCliente():
        sistema = cd.SistemaGestion()
        rut = input("Rut Cliente: ")
        nombre = input("Nombre Cliente: ")
        mail = input("Mail: ")
        telefono = input("Telefono: ")
        tipo_cliente = input(
                "Ingrese el Tipo de cliente que desea agregar (Regular, Premium, Corporativo): "
            ) 
        cliente = cliente(rut, nombre, mail, telefono, tipo_cliente)
        return cliente
        
def agregarCliente(self):
    descuento = float(input("Ingrese el descuento: "))
    fecha_caducidad = input(
        "Ingrese la fecha de caducidad (YYYY-MM-DD): "
    )
    prm = ClientePremium(
        self.rut,
        self.nombre,
        self.mail,
        self.telefono,
        self.tipo_cliente,
        descuento,
        fecha_caducidad,
    )
    return prm
        
        
        
        
        
        
        
        reg = ClienteRegular(
            rut, nombre, mail, telefono, tipo_cliente, 0
        )
        sistema.guardar_cliente(reg)
                    break
                case "premium":
                    descuento = float(input("Ingrese el descuento: "))
                    fecha_caducidad = input(
                        "Ingrese la fecha de caducidad (YYYY-MM-DD): "
                    )
                    prm = ClientePremium(
                        rut,
                        nombre,
                        mail,
                        telefono,
                        tipo_cliente,
                        descuento,
                        fecha_caducidad,
                    )
                    sistema.guardar_cliente(prm)
                    break

                case "corporativo":
                    rut_empresa = input("Rut Empresa: ")
                    razon_social = input("Razon Social: ")
                    limite_credito = float(input("Ingrese el limite de credito: "))
                    corp = ClienteCorporativo(
                        rut,
                        nombre,
                        mail,
                        telefono,
                        tipo_cliente,
                        rut_empresa,
                        razon_social,
                        limite_credito,
                    )
                    sistema.guardar_cliente(corp)
                    break
                case _:
                    print("Tipo de cliente invalido")