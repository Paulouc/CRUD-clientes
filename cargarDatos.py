import json


class SistemaGestion:

    def __init__(self):
        # Este es nuestro diccionario "base de datos"
        base_datos_clientes = getdatos()
        self.base_datos_clientes = base_datos_clientes

    def guardar_cliente(self, cliente):
        """
        Recibe una instancia de Cliente y la guarda en el diccionario.
        Usa el rut_cliente como llave única.
        """
        try:
            # Extraemos el RUT usando el @property
            rut = cliente.rut_cliente

            # Convertimos el objeto a diccionario usando su método to_dict()
            self.base_datos_clientes[rut] = cliente.to_dict()
            setdatos(self.base_datos_clientes)

            print(f"Cliente [{cliente.nombre}] guardado correctamente.")
        except AttributeError:
            print("Error: El objeto proporcionado no es un cliente válido.")

    def actualizar_cliente(self, dict):
        # self.base_datos_clientes.update(dict)
        setdatos(self.base_datos_clientes)
        print(f"Cliente actualizado correctamente.")


def setdatos(datos: dict):
    try:
        with open(
            "archivos/datos.json", "w", encoding="utf-8"
        ) as archivo:  # abre el archivo (datos.json) con metodo de escritura
            json.dump(
                datos, archivo, ensure_ascii=False, indent=4
            )  # copia los datos del parametro al archivo
    except Exception as e:
        print("error al exportar los datos", e)


def getdatos():
    try:
        with open(
            "archivos/datos.json", "r", encoding="utf-8"
        ) as archivo:  # abre el archivo (datos.json) con metodo de lectura
            datos = json.load(
                archivo
            )  # carga los datos del archivo datos.json al diccionario dato
            return datos
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o está vacío/corrupto, devuelve una lista vacía
        return {}  # o devuelve un diccionario vacio
