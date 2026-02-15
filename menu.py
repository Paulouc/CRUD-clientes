import cliente as cl, cargarDatos as cd
from crud import crud as crd


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
        try:
            match opcion:
                case "1":
                    crd.agregar_cliente()
                case "2":
                    crd.editar_clientes()
                case "3":
                    crd.eliminar_clientes()
                case "4":
                    crd.mostrar_clientes()
                case "5":
                    break
                case _:
                    print("Opcion invalida")
        except KeyboardInterrupt:
            print("\nSaliendo del sistema...")
            break
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")


menu()
