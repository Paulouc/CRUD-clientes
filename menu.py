import cliente as cl, cargarDatos as cd


def menu():
    sistema = cd.SistemaGestion()
    while True:
        print("*************************************")
        print("********* CRUD Clientes **********")
        print("*************************************")
        print("1. Agregar Nuevo Cliente")
        print("2. Editar Cliente")
        print("3. Eliminat Cliente")
        print("4. Listar Clientes")
        print("5. Salir")
        opcion = input("Ingrese una opcion: ")
        match opcion:
            case "1":
                print("**********************************")
                print("******** Agregar Cliente *********")
                print("**********************************")

                rut = input("Rut Cliente: ")
                nombre = input("Nombre Cliente: ")
                mail = input("Mail: ")
                telefono = input("Telefono: ")
                while True:
                    tipo_cliente = input(
                        "Ingrese el Tipo de cliente que desea agregar (Regular, Premium, Corporativo): "
                    )
                    tipo_cliente = tipo_cliente.lower()
                    match tipo_cliente:
                        case "regular":
                            reg = cl.ClienteRegular(
                                rut, nombre, mail, telefono, tipo_cliente, 0
                            )
                            sistema.guardar_cliente(reg)
                            break

                        case "premium":
                            descuento = float(input("Ingrese el descuento: "))
                            fecha_caducidad = input(
                                "Ingrese la fecha de caducidad (YYYY-MM-DD): "
                            )
                            prm = cl.ClientePremium(
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
                            limite_credito = float(
                                input("Ingrese el limite de credito: ")
                            )
                            corp = cl.ClienteCorporativo(
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

            case "2":
                print("**********************************")
                print("********* Editar Clientes *********")
                print("**********************************")
                rut = input("Ingrese el rut del cliente a editar: ")
                cliente = sistema.base_datos_clientes[rut]
                while True:
                    if rut in sistema.base_datos_clientes:
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
                                    descuento = float(
                                        input("Ingrese el nuevo descuento: ")
                                    )
                                    cliente["descuento"] = descuento
                                elif cliente["tipo"] == "corporativo":
                                    rut_empresa = input(
                                        "Ingrese el nuevo rut empresa: "
                                    )
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
                                    razon_social = input(
                                        "Ingrese la nueva razon social: "
                                    )
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

                    opcion = input("Desea actualizar otro campo? (s/n): ")
                    if opcion.lower() == "n":
                        sistema.actualizar_cliente(cliente)
                        print(cliente)
                        break
                    else:
                        continue

            case "3":
                print("**********************************")
                print("******* Eliminar Clientes ********")
                print("**********************************")
                rut = input("Ingrese el rut del cliente a eliminar: ")
                if rut in sistema.base_datos_clientes:
                    del sistema.base_datos_clientes[rut]
                    sistema.actualizar_cliente(sistema.base_datos_clientes)
            case "4":
                sistema.mostrar_clientes()

            case "5":
                break
            case _:
                print("Opcion invalida")


menu()
