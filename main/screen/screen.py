import tkinter as tk


def sumar_numeros():
    try:
        # Obtiene los valores ingresados por el usuario de las cajas de entrada
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())

        # Realiza la suma de los números
        resultado = num1 + num2

        # Actualiza el texto en el cuadro de mensaje con el resultado
        etiqueta_resultado.config(text="Resultado: {:.2f}".format(resultado))
    except ValueError:
        # Si ocurre un error al convertir a números, muestra un mensaje de error
        etiqueta_resultado.config(text="Error: Ingresa números válidos")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Suma de Números")

# Crear cajas de entrada para los números
entrada_num1 = tk.Entry(ventana)
entrada_num1.pack(pady=5)

entrada_num2 = tk.Entry(ventana)
entrada_num2.pack(pady=5)

# Crear botón para realizar la suma
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar_numeros)
boton_sumar.pack(pady=5)

# Crear un cuadro de mensaje para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=5)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
