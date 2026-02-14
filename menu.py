import clientes as cl, cargarDatos as cd


def menu():

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
                cl.Cliente.agregarCliente()
            case "2":
                print("**********************************")
                print("********* Editar Clientes *********")
                print("**********************************")
                cl.Cliente.editarCliente()
            case "3":
                print("**********************************")
                print("********* Editar Clientes *********")
                print("**********************************")
                cl.Cliente.eliminarCliente()
            case "4":
                print("**********************************")
                print("********* Listar Clientes ********")
                print("**********************************")
            case _:
                break


menu()
