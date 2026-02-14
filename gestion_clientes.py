import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class AplicacionClientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Clientes")
        self.root.geometry("900x600")
        self.root.minsize(700, 450)

        # Lista simulada de clientes con tipos y campos condicionales
        self.clientes = [
            {
                "id": 1,
                "nombre": "Juan Pérez",
                "email": "juan@example.com",
                "telefono": "555-1234",
                "tipo": "regular",
            },
            {
                "id": 2,
                "nombre": "María López",
                "email": "maria@example.com",
                "telefono": "555-5678",
                "tipo": "premium",
                "descuento": 15.5,
                "fecha_caducidad": "2026-12-31",
            },
            {
                "id": 3,
                "nombre": "Carlos S.A.",
                "email": "ventas@carlos.sa",
                "telefono": "555-9999",
                "tipo": "corporativo",
                "rut_empresa": "12.345.678-9",
                "razon_social": "Carlos Distribuciones Ltda.",
                "limite_credito": 5000000,
            },
        ]
        self.proximo_id = 4

        self.crear_menu()
        self.crear_interfaz_principal()

    def crear_menu(self):
        """Crea la barra de menú principal"""
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        menu_clientes = tk.Menu(barra_menu, tearoff=0)
        menu_clientes.add_command(
            label="Crear Cliente", command=self.crear_cliente, accelerator="Ctrl+N"
        )
        menu_clientes.add_command(
            label="Editar Cliente", command=self.editar_cliente, accelerator="Ctrl+E"
        )
        menu_clientes.add_command(
            label="Eliminar Cliente",
            command=self.eliminar_cliente,
            accelerator="Ctrl+D",
        )
        menu_clientes.add_separator()
        menu_clientes.add_command(
            label="Salir", command=self.root.quit, accelerator="Ctrl+Q"
        )

        barra_menu.add_cascade(label="Clientes", menu=menu_clientes)

        # Atajos de teclado
        self.root.bind("<Control-n>", lambda e: self.crear_cliente())
        self.root.bind("<Control-e>", lambda e: self.editar_cliente())
        self.root.bind("<Control-d>", lambda e: self.eliminar_cliente())
        self.root.bind("<Control-q>", lambda e: self.root.quit())

    def crear_interfaz_principal(self):
        """Crea la interfaz principal con tabla de clientes mejorada"""
        frame_titulo = ttk.Frame(self.root, padding=10)
        frame_titulo.pack(fill=tk.X)

        titulo = ttk.Label(
            frame_titulo,
            text="Sistema de Gestión de Clientes",
            font=("Arial", 18, "bold"),
        )
        titulo.pack()

        frame_tabla = ttk.Frame(self.root, padding=10)
        frame_tabla.pack(fill=tk.BOTH, expand=True)

        # Scrollbars
        scrollbar_y = ttk.Scrollbar(frame_tabla)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        scrollbar_x = ttk.Scrollbar(frame_tabla, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Treeview con columna de tipo
        columnas = ("id", "nombre", "email", "telefono", "tipo", "info_adicional")
        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set,
        )

        # Configurar encabezados
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("email", text="Email")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.heading("tipo", text="Tipo")
        self.tabla.heading("info_adicional", text="Información Adicional")

        # Configurar anchos
        self.tabla.column("id", width=50, anchor=tk.CENTER)
        self.tabla.column("nombre", width=180)
        self.tabla.column("email", width=220)
        self.tabla.column("telefono", width=110, anchor=tk.CENTER)
        self.tabla.column("tipo", width=100, anchor=tk.CENTER)
        self.tabla.column("info_adicional", width=200)

        self.tabla.pack(fill=tk.BOTH, expand=True)

        scrollbar_y.config(command=self.tabla.yview)
        scrollbar_x.config(command=self.tabla.xview)

        self.cargar_clientes()

        frame_info = ttk.Frame(self.root, padding=10)
        frame_info.pack(fill=tk.X)

        info = ttk.Label(
            frame_info,
            text="💡 Selecciona un cliente y usa el menú 'Clientes' para gestionarlo",
            foreground="gray",
        )
        info.pack()

    def cargar_clientes(self):
        """Carga los clientes en la tabla con información adicional según tipo"""
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for cliente in self.clientes:
            # Formatear información adicional según tipo
            if cliente["tipo"] == "premium":
                info = f"Desc: {cliente.get('descuento', 0)}% | Vence: {cliente.get('fecha_caducidad', 'N/A')}"
            elif cliente["tipo"] == "corporativo":
                rut = cliente.get("rut_empresa", "N/A")
                limite = cliente.get("limite_credito", 0)
                info = f"RUT: {rut} | Límite: ${limite:,.0f}"
            else:
                info = "Cliente regular"

            # Mapear tipo para visualización amigable
            tipo_visual = {
                "regular": "Regular",
                "premium": "Premium",
                "corporativo": "Corporativo",
            }.get(cliente["tipo"], cliente["tipo"].capitalize())

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    cliente["id"],
                    cliente["nombre"],
                    cliente["email"],
                    cliente["telefono"],
                    tipo_visual,
                    info,
                ),
            )

    def crear_cliente(self):
        """Ventana para crear un nuevo cliente con campos condicionales"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Crear Nuevo Cliente")
        dialog.geometry("450x480")
        dialog.transient(self.root)
        dialog.grab_set()

        # Variables
        nombre_var = tk.StringVar()
        email_var = tk.StringVar()
        telefono_var = tk.StringVar()
        tipo_var = tk.StringVar(value="regular")

        # Frames para organización
        main_frame = ttk.Frame(dialog, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Formulario base
        ttk.Label(main_frame, text="Nombre completo:", font=("Arial", 10, "bold")).grid(
            row=0, column=0, sticky=tk.W, pady=(0, 5)
        )
        ttk.Entry(main_frame, textvariable=nombre_var, width=40).grid(
            row=1, column=0, columnspan=2, sticky=tk.EW, pady=(0, 15)
        )

        ttk.Label(main_frame, text="Email:").grid(
            row=2, column=0, sticky=tk.W, pady=(0, 5)
        )
        ttk.Entry(main_frame, textvariable=email_var, width=40).grid(
            row=3, column=0, columnspan=2, sticky=tk.EW, pady=(0, 15)
        )

        ttk.Label(main_frame, text="Teléfono:").grid(
            row=4, column=0, sticky=tk.W, pady=(0, 5)
        )
        ttk.Entry(main_frame, textvariable=telefono_var, width=40).grid(
            row=5, column=0, columnspan=2, sticky=tk.EW, pady=(0, 15)
        )

        # Selector de tipo
        ttk.Label(main_frame, text="Tipo de cliente:", font=("Arial", 10, "bold")).grid(
            row=6, column=0, sticky=tk.W, pady=(0, 5)
        )
        tipos = [
            ("Regular", "regular"),
            ("Premium", "premium"),
            ("Corporativo", "corporativo"),
        ]
        tipo_frame = ttk.Frame(main_frame)
        tipo_frame.grid(row=7, column=0, columnspan=2, sticky=tk.W, pady=(0, 15))

        for texto, valor in tipos:
            ttk.Radiobutton(
                tipo_frame, text=texto, variable=tipo_var, value=valor
            ).pack(side=tk.LEFT, padx=(0, 15))

        # Frame para campos condicionales (se actualizará dinámicamente)
        campos_condicionales = ttk.Frame(main_frame)
        campos_condicionales.grid(
            row=8, column=0, columnspan=2, sticky=tk.EW, pady=(0, 15)
        )

        # Variables condicionales
        descuento_var = tk.StringVar()
        fecha_cad_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        rut_var = tk.StringVar()
        razon_var = tk.StringVar()
        limite_var = tk.StringVar(value="0")

        def actualizar_campos_condicionales(*args):
            """Actualizar campos según el tipo seleccionado"""
            # Limpiar frame
            for widget in campos_condicionales.winfo_children():
                widget.destroy()

            tipo = tipo_var.get()

            if tipo == "premium":
                ttk.Label(
                    campos_condicionales, text="Descuento (%):", foreground="#2196F3"
                ).grid(row=0, column=0, sticky=tk.W, pady=(5, 2))
                ttk.Entry(
                    campos_condicionales, textvariable=descuento_var, width=15
                ).grid(row=0, column=1, sticky=tk.W, padx=(10, 0), pady=(5, 2))

                ttk.Label(
                    campos_condicionales,
                    text="Fecha caducidad (YYYY-MM-DD):",
                    foreground="#2196F3",
                ).grid(row=1, column=0, sticky=tk.W, pady=(5, 2))
                ttk.Entry(
                    campos_condicionales, textvariable=fecha_cad_var, width=15
                ).grid(row=1, column=1, sticky=tk.W, padx=(10, 0), pady=(5, 2))

            elif tipo == "corporativo":
                ttk.Label(
                    campos_condicionales, text="RUT Empresa:", foreground="#4CAF50"
                ).grid(row=0, column=0, sticky=tk.W, pady=(5, 2))
                ttk.Entry(campos_condicionales, textvariable=rut_var, width=25).grid(
                    row=0, column=1, sticky=tk.W, padx=(10, 0), pady=(5, 2)
                )

                ttk.Label(
                    campos_condicionales, text="Razón Social:", foreground="#4CAF50"
                ).grid(row=1, column=0, sticky=tk.W, pady=(5, 2))
                ttk.Entry(campos_condicionales, textvariable=razon_var, width=30).grid(
                    row=1, column=1, sticky=tk.W, padx=(10, 0), pady=(5, 2)
                )

                ttk.Label(
                    campos_condicionales,
                    text="Límite de Crédito ($):",
                    foreground="#4CAF50",
                ).grid(row=2, column=0, sticky=tk.W, pady=(5, 2))
                ttk.Entry(campos_condicionales, textvariable=limite_var, width=20).grid(
                    row=2, column=1, sticky=tk.W, padx=(10, 0), pady=(5, 2)
                )

        # Vincular actualización al cambio de tipo
        tipo_var.trace_add("write", actualizar_campos_condicionales)
        actualizar_campos_condicionales()  # Inicializar

        def guardar():
            nombre = nombre_var.get().strip()
            email = email_var.get().strip()
            telefono = telefono_var.get().strip()
            tipo = tipo_var.get()

            if not nombre:
                messagebox.showwarning("Advertencia", "El nombre es obligatorio")
                return

            # Validaciones según tipo
            if tipo == "premium":
                try:
                    descuento = float(descuento_var.get())
                    if descuento < 0 or descuento > 100:
                        messagebox.showwarning(
                            "Advertencia", "El descuento debe estar entre 0 y 100"
                        )
                        return
                except ValueError:
                    messagebox.showwarning(
                        "Advertencia", "El descuento debe ser un número válido"
                    )
                    return

                # Validar formato de fecha simple
                fecha = fecha_cad_var.get().strip()
                if not self.validar_fecha(fecha):
                    messagebox.showwarning(
                        "Advertencia", "Formato de fecha inválido. Use YYYY-MM-DD"
                    )
                    return

            elif tipo == "corporativo":
                rut = rut_var.get().strip()
                razon = razon_var.get().strip()
                if not rut or not razon:
                    messagebox.showwarning(
                        "Advertencia",
                        "RUT y Razón Social son obligatorios para clientes corporativos",
                    )
                    return

                try:
                    limite = float(limite_var.get())
                    if limite < 0:
                        messagebox.showwarning(
                            "Advertencia", "El límite de crédito no puede ser negativo"
                        )
                        return
                except ValueError:
                    messagebox.showwarning(
                        "Advertencia", "El límite de crédito debe ser un número válido"
                    )
                    return

            # Construir cliente
            cliente_base = {
                "id": self.proximo_id,
                "nombre": nombre,
                "email": email,
                "telefono": telefono,
                "tipo": tipo,
            }

            if tipo == "premium":
                cliente_base.update(
                    {
                        "descuento": float(descuento_var.get()),
                        "fecha_caducidad": fecha_cad_var.get().strip(),
                    }
                )
            elif tipo == "corporativo":
                cliente_base.update(
                    {
                        "rut_empresa": rut_var.get().strip(),
                        "razon_social": razon_var.get().strip(),
                        "limite_credito": float(limite_var.get()),
                    }
                )

            self.clientes.append(cliente_base)
            self.proximo_id += 1
            self.cargar_clientes()
            messagebox.showinfo(
                "Éxito",
                f"Cliente '{nombre}' creado correctamente como {tipo.capitalize()}",
            )
            dialog.destroy()

        # Botones
        frame_botones = ttk.Frame(dialog, padding=(0, 10))
        frame_botones.pack(fill=tk.X, padx=15, pady=(0, 10))

        ttk.Button(
            frame_botones, text="Guardar", command=guardar, style="Accent.TButton"
        ).pack(side=tk.RIGHT, padx=5)
        ttk.Button(frame_botones, text="Cancelar", command=dialog.destroy).pack(
            side=tk.RIGHT, padx=5
        )

    def editar_cliente(self):
        """Editar cliente seleccionado con campos condicionales"""
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showinfo(
                "Información", "Por favor, selecciona un cliente para editar"
            )
            return

        item = self.tabla.item(seleccion[0])
        cliente_id = item["values"][0]
        cliente = next((c for c in self.clientes if c["id"] == cliente_id), None)

        if not cliente:
            messagebox.showerror("Error", "Cliente no encontrado")
            return

        dialog = tk.Toplevel(self.root)
        dialog.title(f"Editar Cliente: {cliente['nombre']}")
        dialog.geometry("450x480")
        dialog.transient(self.root)
        dialog.grab_set()

        # Variables con valores actuales
        nombre_var = tk.StringVar(value=cliente.get("nombre", ""))
        email_var = tk.StringVar(value=cliente.get("email", ""))
        telefono_var = tk.StringVar(value=cliente.get("telefono", ""))
        tipo_var = tk.StringVar(value=cliente.get("tipo", "regular"))

        main_frame = ttk.Frame(dialog, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="Nombre completo:", font=("Arial", 10, "bold")).grid(
            row=0, column=0, sticky=tk.W, pady=(0, 5)
        )
        ttk.Entry(main_frame, textvariable=nombre_var, width=40).grid(
            row=1, column=0, columnspan=2, sticky=tk.EW, pady=(0, 15)
        )

        ttk.Label(main_frame, text="Email:").grid(
            row=2, column=0, sticky=tk.W, pady=(0, 5)
        )
        ttk.Entry(main_frame, textvariable=email_var, width=40).grid(
            row=3, column=0, columnspan=2, sticky=tk.EW, pady=(0, 15)
        )

        ttk.Label(main_frame, text="Teléfono:").grid(
            row=4, column=0, sticky=tk.W, pady=(0, 5)
        )
        ttk.Entry(main_frame, textvariable=telefono_var, width=40).grid(
            row=5, column=0, columnspan=2, sticky=tk.EW, pady=(0, 15)
        )

        ttk.Label(main_frame, text="Tipo de cliente:", font=("Arial", 10, "bold")).grid(
            row=6, column=0, sticky=tk.W, pady=(0, 5)
        )
        tipos = [
            ("Regular", "regular"),
            ("Premium", "premium"),
            ("Corporativo", "corporativo"),
        ]
        tipo_frame = ttk.Frame(main_frame)
        tipo_frame.grid(row=7, column=0, columnspan=2, sticky=tk.W, pady=(0, 15))

        for texto, valor in tipos:
            ttk.Radiobutton(
                tipo_frame, text=texto, variable=tipo_var, value=valor
            ).pack(side=tk.LEFT, padx=(0, 15))

        campos_condicionales = ttk.Frame(main_frame)
        campos_condicionales.grid(
            row=8, column=0, columnspan=2, sticky=tk.EW, pady=(0, 15)
        )

        # Variables condicionales con valores actuales
        descuento_var = tk.StringVar(
            value=(
                str(cliente.get("descuento", "0"))
                if cliente.get("tipo") == "premium"
                else "0"
            )
        )
        fecha_cad_var = tk.StringVar(
            value=cliente.get("fecha_caducidad", datetime.now().strftime("%Y-%m-%d"))
        )
        rut_var = tk.StringVar(value=cliente.get("rut_empresa", ""))
        razon_var = tk.StringVar(value=cliente.get("razon_social", ""))
        limite_var = tk.StringVar(
            value=(
                str(cliente.get("limite_credito", "0"))
                if cliente.get("tipo") == "corporativo"
                else "0"
            )
        )

        def actualizar_campos_condicionales(*args):
            for widget in campos_condicionales.winfo_children():
                widget.destroy()

            tipo = tipo_var.get()

            if tipo == "premium":
                ttk.Label(
                    campos_condicionales, text="Descuento (%):", foreground="#2196F3"
                ).grid(row=0, column=0, sticky=tk.W, pady=(5, 2))
                ttk.Entry(
                    campos_condicionales, textvariable=descuento_var, width=15
                ).grid(row=0, column=1, sticky=tk.W, padx=(10, 0), pady=(5, 2))

                ttk.Label(
                    campos_condicionales,
                    text="Fecha caducidad (YYYY-MM-DD):",
                    foreground="#2196F3",
                ).grid(row=1, column=0, sticky=tk.W, pady=(5, 2))
                ttk.Entry(
                    campos_condicionales, textvariable=fecha_cad_var, width=15
                ).grid(row=1, column=1, sticky=tk.W, padx=(10, 0), pady=(5, 2))

            elif tipo == "corporativo":
                ttk.Label(
                    campos_condicionales, text="RUT Empresa:", foreground="#4CAF50"
                ).grid(row=0, column=0, sticky=tk.W, pady=(5, 2))
                ttk.Entry(campos_condicionales, textvariable=rut_var, width=25).grid(
                    row=0, column=1, sticky=tk.W, padx=(10, 0), pady=(5, 2)
                )

                ttk.Label(
                    campos_condicionales, text="Razón Social:", foreground="#4CAF50"
                ).grid(row=1, column=0, sticky=tk.W, pady=(5, 2))
                ttk.Entry(campos_condicionales, textvariable=razon_var, width=30).grid(
                    row=1, column=1, sticky=tk.W, padx=(10, 0), pady=(5, 2)
                )

                ttk.Label(
                    campos_condicionales,
                    text="Límite de Crédito ($):",
                    foreground="#4CAF50",
                ).grid(row=2, column=0, sticky=tk.W, pady=(5, 2))
                ttk.Entry(campos_condicionales, textvariable=limite_var, width=20).grid(
                    row=2, column=1, sticky=tk.W, padx=(10, 0), pady=(5, 2)
                )

        tipo_var.trace_add("write", actualizar_campos_condicionales)
        actualizar_campos_condicionales()  # Inicializar con valores actuales

        def guardar():
            nombre = nombre_var.get().strip()
            email = email_var.get().strip()
            telefono = telefono_var.get().strip()
            tipo = tipo_var.get()

            if not nombre:
                messagebox.showwarning("Advertencia", "El nombre es obligatorio")
                return

            # Validaciones según tipo
            if tipo == "premium":
                try:
                    descuento = float(descuento_var.get())
                    if descuento < 0 or descuento > 100:
                        messagebox.showwarning(
                            "Advertencia", "El descuento debe estar entre 0 y 100"
                        )
                        return
                except ValueError:
                    messagebox.showwarning(
                        "Advertencia", "El descuento debe ser un número válido"
                    )
                    return

                fecha = fecha_cad_var.get().strip()
                if not self.validar_fecha(fecha):
                    messagebox.showwarning(
                        "Advertencia", "Formato de fecha inválido. Use YYYY-MM-DD"
                    )
                    return

            elif tipo == "corporativo":
                rut = rut_var.get().strip()
                razon = razon_var.get().strip()
                if not rut or not razon:
                    messagebox.showwarning(
                        "Advertencia",
                        "RUT y Razón Social son obligatorios para clientes corporativos",
                    )
                    return

                try:
                    limite = float(limite_var.get())
                    if limite < 0:
                        messagebox.showwarning(
                            "Advertencia", "El límite de crédito no puede ser negativo"
                        )
                        return
                except ValueError:
                    messagebox.showwarning(
                        "Advertencia", "El límite de crédito debe ser un número válido"
                    )
                    return

            # Actualizar cliente
            cliente.update(
                {"nombre": nombre, "email": email, "telefono": telefono, "tipo": tipo}
            )

            if tipo == "premium":
                cliente.update(
                    {
                        "descuento": float(descuento_var.get()),
                        "fecha_caducidad": fecha_cad_var.get().strip(),
                    }
                )
            elif tipo == "corporativo":
                cliente.update(
                    {
                        "rut_empresa": rut_var.get().strip(),
                        "razon_social": razon_var.get().strip(),
                        "limite_credito": float(limite_var.get()),
                    }
                )
            else:
                # Eliminar campos condicionales si cambia a regular
                cliente.pop("descuento", None)
                cliente.pop("fecha_caducidad", None)
                cliente.pop("rut_empresa", None)
                cliente.pop("razon_social", None)
                cliente.pop("limite_credito", None)

            self.cargar_clientes()
            messagebox.showinfo(
                "Éxito", f"Cliente '{nombre}' actualizado correctamente"
            )
            dialog.destroy()

        frame_botones = ttk.Frame(dialog, padding=(0, 10))
        frame_botones.pack(fill=tk.X, padx=15, pady=(0, 10))

        ttk.Button(
            frame_botones, text="Guardar", command=guardar, style="Accent.TButton"
        ).pack(side=tk.RIGHT, padx=5)
        ttk.Button(frame_botones, text="Cancelar", command=dialog.destroy).pack(
            side=tk.RIGHT, padx=5
        )

    def eliminar_cliente(self):
        """Eliminar cliente seleccionado"""
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showinfo(
                "Información", "Por favor, selecciona un cliente para eliminar"
            )
            return

        item = self.tabla.item(seleccion[0])
        cliente_id = item["values"][0]
        nombre_cliente = item["values"][1]
        tipo_cliente = item["values"][4]

        respuesta = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Estás seguro de eliminar al cliente '{nombre_cliente}' ({tipo_cliente})?\nEsta acción no se puede deshacer.",
        )

        if respuesta:
            self.clientes = [c for c in self.clientes if c["id"] != cliente_id]
            self.cargar_clientes()
            messagebox.showinfo(
                "Éxito", f"Cliente '{nombre_cliente}' eliminado correctamente"
            )

    def validar_fecha(self, fecha_str):
        """Valida formato YYYY-MM-DD y fecha razonable"""
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
            # Verificar que no sea una fecha muy antigua
            year = int(fecha_str.split("-")[0])
            return year >= 2000 and year <= 2100
        except ValueError:
            return False


if __name__ == "__main__":
    root = tk.Tk()

    # Estilo moderno
    try:
        style = ttk.Style()
        style.theme_use("clam")

        # Colores personalizados
        style.configure("TFrame", background="#f5f5f5")
        style.configure("TLabel", background="#f5f5f5")
        style.configure(
            "Accent.TButton",
            background="#2196F3",
            foreground="white",
            font=("Arial", 10, "bold"),
        )
        style.map(
            "Accent.TButton",
            background=[("active", "#1976D2")],
            foreground=[("active", "white")],
        )
    except:
        pass

    app = AplicacionClientes(root)
    root.mainloop()
