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
        # Extraemos el RUT usando el @property
        rut = cliente.rut_cliente

        # Convertimos el objeto a diccionario usando su método to_dict()
        self.base_datos_clientes[rut] = cliente.to_dict()
        setdatos(self.base_datos_clientes)

        print(f"Cliente [{cliente.nombre}] guardado correctamente.")

    def actualizar_cliente(self, dict):
        # self.base_datos_clientes.update(dict)
        setdatos(self.base_datos_clientes)
        print(f"Cliente actualizado correctamente.")

    def mostrar_clientes(self):

        header = f"{'RUT':<12} | {'Nombre':<15} | {'Tipo':<12} | {'Email':<25} | {'Extra':<30} | {'Extra1':<30} | {'Extra2':<30}"
        separator = "-" * len(header)

        print("\n" + separator)
        print(header)
        print(separator)
        clientes = self.base_datos_clientes

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
                extra2 = f"Rut empresa: {info.get('rut empresa', 0)}%"

            print(
                f"{info['rut']:<12} | {info['nombre']:<15} | {info['tipo']:<12} | {info['email']:<25} | {extra:<30}| {extra1:<30}| {extra2:<30}|"
            )

        print(separator + "\n")


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
