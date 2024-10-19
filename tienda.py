import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 

# Definir los productos y sus precios
productos = {
    "Manzanas": 2.00,
    "Plátanos": 1.50,
    "Tomates": 1.20,
    "Zanahorias": 0.80,
    "Detergente": 3.50,
    "Jabón": 1.00
}

# Función para calcular el total y actualizar el label
def calcular_total():
    cantidad = int(entrada_cantidad.get())
    producto_seleccionado = lista_productos.get()
    precio = productos[producto_seleccionado]
    total = cantidad * precio
    label_resultado.config(text=f"Total: Q{total:.2f}")

# Función para mostrar el GIF animado
def mostrar_gif(panel, ruta_gif):
    gif = Image.open(ruta_gif)
    frames = []

    try:
        while True:
            frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(len(frames))  # Salta al siguiente fotograma
    except EOFError:
        pass  # Termina de cargar todos los fotogramas del GIF

    def actualizar_gif(indice=0):
        frame = frames[indice]
        panel.config(image=frame)
        ventana_emergente.after(100, actualizar_gif, (indice + 1) % len(frames))  # Cicla los fotogramas

    actualizar_gif()

# Función para calcular el total y mostrar la ventana emergente con el GIF
def Comprar():
    cantidad = entrada_cantidad.get()
    if cantidad.isdigit():
        cantidad = int(cantidad)
        producto_seleccionado = lista_productos.get()
        precio = productos[producto_seleccionado]
        total = cantidad * precio

        # Crear la ventana emergente con el total
        global ventana_emergente  # Usar global para referenciar en la función mostrar_gif
        ventana_emergente = tk.Toplevel()
        ventana_emergente.title("Resumen de Compra")
        ventana_emergente.geometry("400x300")

        # Mostrar el total
        tk.Label(ventana_emergente, text=f"Gracias {entrada_nombre.get()} por tu compra").pack()
        tk.Label(ventana_emergente, text=f"Total: Q{total:.2f}").pack()

        # Panel donde se va a mostrar el GIF animado
        panel = tk.Label(ventana_emergente)
        panel.pack()

        # Mostrar el GIF animado
        ruta_gif = "/Users/barre/Documents/Universidad/Cuarto_Semestre/Programacion_I/Tienda/gracias.gif"
        mostrar_gif(panel, ruta_gif)

        # Botón de cerrar
        boton_cerrar = tk.Button(ventana_emergente, text="Cerrar", command=ventana_emergente.destroy)
        boton_cerrar.pack()
    else:
        messagebox.showerror("Error", "Por favor, ingrese una cantidad válida.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Tienda de Abarrotes")
ventana.geometry("800x500")

# Etiqueta y entrada para el nombre
tk.Label(ventana, text="Nombre del cliente:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Lista desplegable para seleccionar productos
tk.Label(ventana, text="Seleccionar Producto:").pack()
lista_productos = tk.StringVar(ventana)
lista_productos.set("Manzanas")  # Valor por defecto
opciones = tk.OptionMenu(ventana, lista_productos, *productos.keys())
opciones.pack()

# Entrada para la cantidad
tk.Label(ventana, text="Cantidad:").pack()
entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.pack()

# Botón para calcular el total
boton_calcular = tk.Button(ventana, text="Calcular Total", command=calcular_total)
boton_calcular.pack()

# Mostrar calculo
label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)

# Botón para comprar
boton_comprar = tk.Button(ventana, text="Comprar", command=Comprar)
boton_comprar.pack()

# Iniciar la ventana
ventana.mainloop()
