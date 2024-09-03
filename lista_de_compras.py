import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import PhotoImage

# Crear una ventana principal
root = tk.Tk()
root.title("Aplicación Principal")
root.geometry("398x600")

# Agregar una imagen a la ventana principal
# Reemplaza con la ruta de tu imagen
image = PhotoImage(file="FONDO_400X660.png")
background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Crear un botón para abrir la ventana Toplevel con la lista de compras


def abrir_lista_compras():
    ventana_lista_compras = tk.Toplevel(root)
    app = ListaDeComprasApp(ventana_lista_compras)


btn_abrir = tk.Button(root,
                      text="Abrir Lista de Compras",
                      command=abrir_lista_compras,
                      activebackground="lightgrey",
                      activeforeground="lightgrey",
                      anchor="center",
                      bd=2,
                      bg="orange",
                      cursor="hand2",
                      disabledforeground="green",
                      fg="black",
                      font=("Arial", 14, "bold"),
                      height=3,
                      highlightbackground="black",
                      highlightcolor="green",
                      highlightthickness=1,
                      justify="center",
                      overrelief="raised",
                      padx=6,
                      pady=6,
                      width=20,
                      wraplength=100)
btn_abrir.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class ListaDeComprasApp:

    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Compras")
        self.master.config(background='gray15')

        # Datos iniciales de las categorías y sus ítems
        self.categorias = {
            "Verdulería": ["Tomate", "Lechuga", "Papa"],
            "Perfumería": ["Shampoo", "Jabón", "Perfume"],
            "Lácteos": ["Leche", "Yogur", "Queso"]
        }

        # Lista de compras
        self.lista_compras = []

        # Crear los marcos para organizar los widgets
        self.frame_categorias = tk.LabelFrame(master,
                                              text="Categorias",
                                              border=6,
                                              bg="gray15",
                                              font=("Arial", 11, "bold"),
                                              fg="white")
        self.frame_categorias.pack(side=tk.LEFT, padx=25, pady=10)

        self.frame_items = tk.LabelFrame(master,
                                         text="Items",
                                         border=6,
                                         bg="gray15",
                                         font=("Arial", 11, "bold"),
                                         fg="white")
        self.frame_items.pack(side=tk.LEFT, padx=25, pady=10)

        self.frame_lista_compras = tk.LabelFrame(master,
                                                 text="Lista de Compras",
                                                 border=6,
                                                 bg="gray15",
                                                 font=("Arial", 11, "bold"),
                                                 fg="white")
        self.frame_lista_compras.pack(side=tk.LEFT, padx=25, pady=10)

        # Lista de categorías
        self.lista_categorias = tk.Listbox(self.frame_categorias,
                                           height=10,
                                           background='gray15',
                                           fg="white",
                                           font=("Arial", 12))
        self.lista_categorias.pack(padx=15, pady=15)
        for categoria in self.categorias.keys():
            self.lista_categorias.insert(tk.END, categoria)

        # Botón para seleccionar una categoría
        self.btn_seleccionar_categoria = tk.Button(
            self.frame_categorias,
            text="Seleccionar Categoría",
            command=self.seleccionar_categoria,
            activebackground="lightgrey",
            activeforeground="lightgrey",
            anchor="center",
            bd=3,
            bg="orange",
            cursor="hand2",
            disabledforeground="green",
            fg="black",
            font=(
                "Arial",
                10,
            ),
            height=1,
            highlightbackground="black",
            highlightcolor="green",
            highlightthickness=2,
            justify="center",
            overrelief="raised",
            padx=6,
            pady=6,
            width=13,
            wraplength=100)
        self.btn_seleccionar_categoria.pack(pady=5)

        # Botón para crear una nueva categoría
        self.btn_add_cat = tk.Button(self.frame_categorias,
                                     text="Agregar Categoria",
                                     command=self.crear_categoria,
                                     activebackground="lightgrey",
                                     activeforeground="lightgrey",
                                     anchor="center",
                                     bd=3,
                                     bg="orange",
                                     cursor="hand2",
                                     disabledforeground="green",
                                     fg="black",
                                     font=(
                                         "Arial",
                                         10,
                                     ),
                                     height=1,
                                     highlightbackground="black",
                                     highlightcolor="green",
                                     highlightthickness=2,
                                     justify="center",
                                     overrelief="raised",
                                     padx=6,
                                     pady=6,
                                     width=13,
                                     wraplength=100)
        self.btn_add_cat.pack(pady=5)

        # Lista de ítems en la categoría seleccionada con opción de selección múltiple
        self.lista_items = tk.Listbox(self.frame_items,
                                      selectmode=tk.MULTIPLE,
                                      background='gray15',
                                      fg="white",
                                      font=("Arial", 12))
        self.lista_items.pack(padx=15, pady=15)

        # Botón para agregar los ítems seleccionados a la lista de compras
        self.btn_agregar = tk.Button(self.frame_items,
                                     text="Agregar a la lista",
                                     command=self.agregar_items,
                                     activebackground="lightgrey",
                                     activeforeground="lightgrey",
                                     anchor="center",
                                     bd=3,
                                     bg="orange",
                                     cursor="hand2",
                                     disabledforeground="green",
                                     fg="black",
                                     font=(
                                         "Arial",
                                         10,
                                     ),
                                     height=1,
                                     highlightbackground="black",
                                     highlightcolor="green",
                                     highlightthickness=2,
                                     justify="center",
                                     overrelief="raised",
                                     padx=6,
                                     pady=6,
                                     width=13,
                                     wraplength=100)
        self.btn_agregar.pack(pady=5)

        # Botón para añadir un nuevo ítem a la categoría seleccionada
        self.btn_add_item = tk.Button(self.frame_items,
                                      text="Agregar Ítem a Categoría",
                                      command=self.agregar_item_a_categoria,
                                      activebackground="lightgrey",
                                      activeforeground="lightgrey",
                                      anchor="center",
                                      bd=3,
                                      bg="orange",
                                      cursor="hand2",
                                      disabledforeground="green",
                                      fg="black",
                                      font=("Arial", 10),
                                      height=1,
                                      highlightbackground="black",
                                      highlightcolor="green",
                                      highlightthickness=2,
                                      justify="center",
                                      overrelief="raised",
                                      padx=6,
                                      pady=6,
                                      width=13,
                                      wraplength=100)
        self.btn_add_item.pack(pady=5)

        # Lista de compras
        self.lista_text = tk.Listbox(self.frame_lista_compras,
                                     background='gray15',
                                     fg="white",
                                     font=("Arial", 12))
        self.lista_text.pack(padx=15, pady=15)

        # Botón para eliminar un ítem de la lista de compras
        self.btn_eliminar = tk.Button(self.frame_lista_compras,
                                      text="Eliminar ítem",
                                      command=self.eliminar_item,
                                      activebackground="lightgrey",
                                      activeforeground="lightgrey",
                                      anchor="center",
                                      bd=3,
                                      bg="orange",
                                      cursor="hand2",
                                      disabledforeground="green",
                                      fg="black",
                                      font=(
                                          "Arial",
                                          10,
                                      ),
                                      height=1,
                                      highlightbackground="black",
                                      highlightcolor="green",
                                      highlightthickness=2,
                                      justify="center",
                                      overrelief="raised",
                                      padx=6,
                                      pady=6,
                                      width=10,
                                      wraplength=100)
        self.btn_eliminar.pack(pady=5)

    # Función para actualizar la lista de compras en la interfaz
    def actualizar_lista(self):
        self.lista_text.delete(0, tk.END)
        for item in self.lista_compras:
            self.lista_text.insert(tk.END, item)

    # Función para agregar ítems seleccionados a la lista de compras
    def agregar_items(self):
        seleccionados = self.lista_items.curselection()
        for i in seleccionados:
            item = self.lista_items.get(i)
            if item not in self.lista_compras:
                self.lista_compras.append(item)
        self.actualizar_lista()

    # Función para eliminar un ítem de la lista de compras
    def eliminar_item(self):
        seleccionado = self.lista_text.curselection()
        if seleccionado:
            self.lista_compras.pop(seleccionado[0])
            self.actualizar_lista()

    # Función para seleccionar una categoría y mostrar sus ítems
    def seleccionar_categoria(self):
        categoria = self.lista_categorias.get(tk.ACTIVE)
        if categoria:
            self.lista_items.delete(0, tk.END)
            for item in self.categorias[categoria]:
                self.lista_items.insert(tk.END, item)

    # Función para agregar un nuevo ítem a la categoría seleccionada
    def agregar_item_a_categoria(self):
        categoria = self.lista_categorias.get(tk.ACTIVE)

        if categoria:
            nuevo_item = simpledialog.askstring(
                "Agregar Ítem",
                f"Ingresa un nuevo ítem para la categoría {categoria}:",
            )
            if nuevo_item:
                self.categorias[categoria].append(nuevo_item)
                self.seleccionar_categoria()
            else:
                messagebox.showwarning("Advertencia",
                                       "No se ingresó ningún ítem.")
        else:
            messagebox.showwarning("Advertencia",
                                   "Selecciona una categoría primero.")

    # Función para crear una nueva categoría
    def crear_categoria(self):
        nueva_categoria = simpledialog.askstring(
            "Nueva Categoría", "Ingresa el nombre de la nueva categoría:")
        if nueva_categoria:
            if nueva_categoria not in self.categorias:
                self.categorias[nueva_categoria] = []
                self.lista_categorias.insert(tk.END, nueva_categoria)
            else:
                messagebox.showwarning("Advertencia",
                                       "Esa categoría ya existe.")
        else:
            messagebox.showwarning("Advertencia",
                                   "No se ingresó ningún nombre.")


root.mainloop()
