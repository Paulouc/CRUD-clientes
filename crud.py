import cliente as cl, cargarDatos as cd
from datetime import date
from dateutil.relativedelta import relativedelta

sistema = cd.SistemaGestion()


class crud:

    def agregar_cliente():

        print("**********************************")
        print("******** Agregar Cliente *********")
        print("**********************************")
        rut = input("Rut Cliente: ")

        # Validamos primero para obtener el rut limpio y verificar si existe ese
        es_valido, rut_final = crud.validar_Rut(rut)

        if es_valido and rut_final in sistema.base_datos_clientes:
            print("El rut ya esta registrado")
            print(
                f"{sistema.base_datos_clientes[rut_final]['nombre']} - {sistema.base_datos_clientes[rut_final]['fecha registro']}"
            )
        else:
            if es_valido:
                nombre = input("Nombre Cliente: ")
                while not crud.validar_nombre(nombre):
                    nombre = input("Nombre Cliente: ")
                mail = input("Mail: ")
                while not crud.validar_email(mail):
                    mail = input("Mail: ")
                telefono = input("Telefono: ")
                while not crud.validar_telefono(telefono):
                    telefono = input("Telefono: ")
                while True:
                    tipo_cliente = input(
                        "Ingrese el Tipo de cliente que desea agregar (Regular, Premium, Corporativo): "
                    ).lower()
                    match tipo_cliente:
                        case "regular":
                            reg = cl.ClienteRegular(
                                rut_final, nombre, mail, telefono, tipo_cliente, 0
                            )
                            sistema.guardar_cliente(reg)
                            break

                        case "premium":
                            descuento = 2.5
                            fecha_caducidad = (
                                date.today() + relativedelta(months=+6)
                            ).strftime("%d-%m-%Y")
                            prm = cl.ClientePremium(
                                rut_final,
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
                            limite_credito = 1000000
                            rut_empresa = input("Rut Empresa: ")
                            es_valido, rut_empresa2 = crud.validar_Rut(rut_empresa)

                            if es_valido:
                                razon_social = input("Razon Social: ")
                                while not crud.validar_nombre(razon_social):
                                    razon_social = input("Razon Social: ")
                                corp = cl.ClienteCorporativo(
                                    rut_final,
                                    nombre,
                                    mail,
                                    telefono,
                                    tipo_cliente,
                                    rut_empresa2,
                                    razon_social,
                                    limite_credito,
                                )
                                sistema.guardar_cliente(corp)
                                break
                            else:
                                print("rut invalido")
                        case _:
                            print("Tipo de cliente invalido")
            else:
                print(
                    "Error: El RUT debe ser de entre 7 y 9 dígitos y solo contener números (o K)."
                )

    def editar_clientes():
        print("**********************************")
        print("********* Editar Clientes *********")
        print("**********************************")
        rut = input("Ingrese el rut del cliente a editar: ")

        if rut not in sistema.base_datos_clientes:
            print("Error: Cliente no encontrado.")
        else:
            cliente = sistema.base_datos_clientes[rut]
            while True:
                print(f"seleccione el campo a modificar")
                print("1. Nombre")
                print("2. Mail")
                print("3. Telefono")

                if cliente["tipo"] == "premium":
                    print("4. Descuento")
                    print("5. Renovar fecha de caducidad")
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
                        while not crud.validar_nombre(nombre):
                            nombre = input("Ingrese el nuevo nombre: ")
                        cliente["nombre"] = nombre
                    case "2":
                        mail = input("Ingrese el nuevo mail: ")
                        while not crud.validar_email(mail):
                            mail = input("Ingrese el nuevo mail: ")
                        cliente["email"] = mail
                    case "3":
                        telefono = input("Ingrese el nuevo telefono: ")
                        while not crud.validar_telefono(telefono):
                            telefono = input("Ingrese el nuevo telefono: ")
                        cliente["telefono"] = telefono

                    case "4":
                        if cliente["tipo"] == "premium":
                            descuento = float(input("Ingrese el nuevo descuento: "))
                            while not crud.validar_monto_rango(descuento):
                                descuento = float(input("Ingrese el nuevo descuento: "))
                            cliente["descuento"] = descuento
                        elif cliente["tipo"] == "corporativo":
                            rut_empresa = input("Ingrese el nuevo rut empresa: ")
                            while not crud.validar_Rut(rut_empresa):
                                rut_empresa = input("Ingrese el nuevo rut empresa: ")
                            cliente["rut_empresa"] = rut_empresa
                        elif cliente["tipo"] == "regular":
                            while True:
                                try:
                                    puntos_acumulados = float(
                                        input("Ingrese los nuevos puntos acumulados: ")
                                    )
                                    break
                                except ValueError:
                                    print("Error: Debe ingresar un valor numérico.")

                            if puntos_acumulados > 0:
                                cliente["puntos_acumulados"] = puntos_acumulados
                            else:
                                print("ingrese un numero mayor a 0")
                    case "5":
                        if cliente["tipo"] == "premium":
                            caduca = (date.today() + relativedelta(months=+6)).strftime(
                                "%d-%m-%Y"
                            )
                            cliente["fecha_caducidad"] = caduca
                        elif cliente["tipo"] == "corporativo":
                            razon_social = input("Ingrese la nueva razon social: ")
                            while not crud.validar_nombre(razon_social):
                                razon_social = input("Ingrese la nueva razon social: ")
                            cliente["razon_social"] = razon_social
                        else:
                            print("opcion invalida")
                    case "6":
                        if cliente["tipo"] == "corporativo":
                            while True:
                                try:
                                    lc = float(input("Ingrese el nuevo monto limite: "))
                                    break
                                except ValueError:
                                    print("Error: Debe ingresar un valor numérico.")
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

    def eliminar_clientes():
        print("**********************************")
        print("******* Eliminar Clientes ********")
        print("**********************************")
        rut = input("Ingrese el rut del cliente a eliminar: ")
        if rut in sistema.base_datos_clientes:
            del sistema.base_datos_clientes[rut]
            sistema.actualizar_cliente(sistema.base_datos_clientes)
        else:
            print(
                "Error: Cliente no encontrado, verifique que ingreso el rut correctamente."
            )

    def mostrar_clientes():

        header = f"{'RUT':<12} | {'Nombre':<15} | {'Tipo':<12} | {'Email':<25} | {'Pts - desc - lim credito':<30} | {'fecha caducidad - Empresa':<30} | {'Rut empresa':<30}"
        separator = "-" * len(header)

        print("\n" + separator)
        print(header)
        print(separator)
        clientes = sistema.base_datos_clientes

        for rut, info in clientes.items():
            # Lógica para mostrar el dato extra según el tipo
            extra = ""
            extra1 = ""
            extra2 = ""
            if info["tipo"] == "Regular":
                extra = f"Pts: {info.get('puntos acumulados', 0)}"
            elif info["tipo"] == "Premium":
                extra = f"Desc: {info.get('descuento', 0)}%"
                extra1 = f"Caduca: {info.get('fecha caducidad', 0)}%"

            elif info["tipo"] == "Corporativo":
                extra = f"Crédito: ${info.get('limite credito', 0):,.0f}"
                extra1 = f"Empresa: {info.get('razon social', 0)}%"
                extra2 = f" {info.get('rut empresa', 0)}%"

            print(
                f"{info['rut']:<12} | {info['nombre']:<15} | {info['tipo']:<12} | {info['email']:<25} | {extra:<30}| {extra1:<30}| {extra2:<30}|"
            )

        print(separator + "\n")

    def validar_Rut(rut):
        # 1. Limpiar: quitar puntos, guiones y espacios, pasar a MAYÚSCULAS
        rut_limpio = rut.replace(".", "").replace("-", "").replace(" ", "").upper()

        # 2. Reemplazar 'K' por '0' según tu requerimiento
        rut_limpio = rut_limpio.replace("K", "0")

        # 3. Validar que lo que queda sean solo números
        if rut_limpio.isdigit():
            # Validar largo, mínimo 7 para RUTs viejos, máximo 9
            if 7 <= len(rut_limpio) <= 9:
                return True, rut_limpio
            else:
                return False, None
        else:
            return False, None

    def validar_nombre(nombre):
        # 1. Eliminar espacios en blanco a los extremos
        nombre = nombre.strip()

        # 2. Verificar que no esté vacío y que tenga un largo mínimo (ej. 3 caracteres)
        if len(nombre) < 3:
            print("Error: El nombre debe tener al menos 3 caracteres.")
            return False

        # 3. Verificar que solo contenga letras (permitiendo espacios)
        # Reemplazamos espacios por nada temporalmente para usar .isalpha()
        if nombre.replace(" ", "").isalpha():
            return True
        else:
            print("Error: El nombre solo puede contener letras.")
            return False

    def validar_email(email):
        email = email.strip()
        if "@" in email and "." in email:
            # Verificamos que el punto esté después del @
            if email.find("@") < email.rfind("."):
                return True
        print("Error: El correo debe contener un '@' y un '.'")
        return False

    def validar_telefono(telefono):
        # 1. Limpiar espacios o guiones
        tel_limpio = telefono.replace(" ", "").replace("-", "").replace("+", "")

        # 2. Verificar si son solo dígitos y tienen un largo razonable (ej: 9 a 12 dígitos)
        if tel_limpio.isdigit() and 8 <= len(tel_limpio) <= 12:
            return True
        else:
            print("Error: El teléfono debe tener entre 8 y 12 números.")
            return False

    def validar_monto_rango(valor):
        try:
            # 1. Convertir a número (float permite decimales como 5.5)
            num = float(valor)

            # 2. Verificar el rango entre 1 y 10
            if 1 <= num <= 10:
                return True, num
            else:
                print("Error: El monto debe estar entre 1 y 10.")
                return False, None

        except ValueError:
            print("Error: Debe ingresar un valor numérico.")
            return False, None
