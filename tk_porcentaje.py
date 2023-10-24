import tkinter as tk

# Declarar resultado_label como variable global
resultado_label = None

# Función para calcular el porcentaje
def calcular_porcentaje(precio_inicial, porcentaje, tipo):
    global resultado_label  # Utilizar la variable global
    try:
        precio_inicial = float(precio_inicial)
        porcentaje = float(porcentaje)
        if tipo == "aumento":
            precio_final = precio_inicial + (precio_inicial * (porcentaje / 100))
        else:
            precio_final = precio_inicial - (precio_inicial * (porcentaje / 100))
        resultado_label.config(text=f"Precio final: {precio_final:.2f} euros")
    except ValueError:
        resultado_label.config(text="Por favor, ingresa valores válidos")

# Función para abrir la ventana de cálculo
def abrir_ventana_calculo(tipo):
    ventana_calculo = tk.Toplevel(ventana)
    ventana_calculo.title(f"Calculadora de {tipo.capitalize()}")
    ventana_calculo.geometry("450x375")

    entry_precio_inicial = tk.Entry(ventana_calculo)
    entry_precio_inicial.grid(row=0, column=1, padx=10, pady=5)

    entry_porcentaje = tk.Entry(ventana_calculo)
    entry_porcentaje.grid(row=1, column=1, padx=10, pady=5)

    global resultado_label  # Utilizar la variable global
    resultado_label = tk.Label(ventana_calculo, text="")
    resultado_label.grid(row=2, column=1, padx=10, pady=5)

    precio_inicial_label = tk.Label(ventana_calculo, text="Precio Inicial:")
    precio_inicial_label.grid(row=0, column=0, padx=10, pady=5)

    porcentaje_label = tk.Label(ventana_calculo, text="Porcentaje añadido:")
    porcentaje_label.grid(row=1, column=0, padx=10, pady=5)

    calcular_button = tk.Button(ventana_calculo, text="Calcular", command=lambda: calcular_porcentaje(entry_precio_inicial.get(), entry_porcentaje.get(), tipo))
    calcular_button.grid(row=3, columnspan=2, padx=10, pady=5)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Porcentajes")
ventana.geometry("500x250")

# Etiqueta con el título "Elige una opción" sobre los botones
titulo_label = tk.Label(ventana, text="Elige una opción")
titulo_label.pack(pady=40)

# Botones cuadrados para calcular aumento y descuento
boton_aumento = tk.Button(ventana, text="Aumento", command=lambda: abrir_ventana_calculo("aumento"))
boton_aumento.place(x=50, y=100, width=150, height=100)
boton_descuento = tk.Button(ventana, text="Descuento", command=lambda: abrir_ventana_calculo("descuento"))
boton_descuento.place(x=300, y=100, width=150, height=100)

# Ejecución de la aplicación
ventana.mainloop()
