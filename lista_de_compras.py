import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import PhotoImage


class ListaDeComprasApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Compras")

        # Datos iniciales de las categorías y sus ítems
        self.categorias = {
            "Verdulería": ["Tomate", "Lechuga", "Papa","Cebolla","Frutilla","Manzana","Pera"],
            "Perfumería": ["Shampoo", "Jabón", "Perfume","Pasta de Dientes","Peine","Afeitadora"],
            "Lácteos": ["Leche", "Yogur", "Queso"]
        }

        # Lista de compras
        self.lista_compras = []

        # Crear los marcos para organizar los widgets
        self.frame_categorias = tk.Frame(master)
        self.frame_categorias.pack(side=tk.LEFT, padx=10, pady=10)

        self.frame_items = tk.Frame(master)
        self.frame_items.pack(side=tk.LEFT, padx=10, pady=10)

        self.frame_lista_compras = tk.Frame(master)
        self.frame_lista_compras.pack(side=tk.LEFT, padx=10, pady=10)

        # Lista de categorías
        tk.Label(self.frame_categorias, text="Categorías").pack()
        self.lista_categorias = tk.Listbox(self.frame_categorias, height=10)
        self.lista_categorias.pack()
        for categoria in self.categorias.keys():
            self.lista_categorias.insert(tk.END, categoria)

        # Vincular la selección de una categoría al evento para mostrar los ítems
        self.lista_categorias.bind(
            '<<ListboxSelect>>', self.seleccionar_categoria)

        # Lista de ítems en la categoría seleccionada con opción de selección múltiple
        tk.Label(self.frame_items, text="Ítems").pack()
        self.lista_items = tk.Listbox(
            self.frame_items, height=10, selectmode=tk.MULTIPLE)
        self.lista_items.pack()

        # Botón para agregar los ítems seleccionados a la lista de compras
        self.btn_agregar = tk.Button(
            self.frame_items, text="Agregar a la lista", command=self.agregar_items)
        self.btn_agregar.pack(pady=5)

        # Botón para añadir un nuevo ítem a la categoría seleccionada
        self.btn_add_item = tk.Button(
            self.frame_items, text="Agregar Ítem a Categoría", command=self.agregar_item_a_categoria)
        self.btn_add_item.pack(pady=5)

        # Lista de compras
        tk.Label(self.frame_lista_compras, text="Lista de Compras").pack()
        self.lista_text = tk.Listbox(self.frame_lista_compras, height=10)
        self.lista_text.pack()

        # Botón para eliminar un ítem de la lista de compras
        self.btn_eliminar = tk.Button(
            self.frame_lista_compras, text="Eliminar ítem", command=self.eliminar_item)
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
    def seleccionar_categoria(self, event):
        categoria = self.lista_categorias.get(tk.ACTIVE)
        self.lista_items.delete(0, tk.END)
        for item in self.categorias[categoria]:
            self.lista_items.insert(tk.END, item)

    # Función para agregar un nuevo ítem a la categoría seleccionada
    def agregar_item_a_categoria(self):
        categoria = self.lista_categorias.get(tk.ACTIVE)
        if categoria:
            nuevo_item = simpledialog.askstring(
                "Agregar Ítem", f"Ingresa un nuevo ítem para la categoría {categoria}:")
            if nuevo_item:
                self.categorias[categoria].append(nuevo_item)
                self.seleccionar_categoria(None)
            else:
                messagebox.showwarning(
                    "Advertencia", "No se ingresó ningún ítem.")
        else:
            messagebox.showwarning(
                "Advertencia", "Selecciona una categoría primero.")


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


btn_abrir = tk.Button(root, text="Abrir Lista de Compras",
                      command=abrir_lista_compras)
btn_abrir.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
