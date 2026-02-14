def generar_properties(*atributos):
    """Genera código @property para una lista de atributos"""
    codigo = []
    for attr in atributos:
        codigo.append(f"@property")
        codigo.append(f"def {attr}(self):")
        codigo.append(f"    return self._{attr}\n")
        codigo.append(f"@{attr}.setter")
        codigo.append(f"def {attr}(self, valor):")
        codigo.append(f"    self._{attr} = valor\n")
    return "\n".join(codigo)


# Uso
print(generar_properties("descuento", "fecha_caducidad"))

# Copiar la salida y pegarla en la clase
