import tkinter as tk
from PIL import Image, ImageTk
from main.tomorrow_api.get_weather_forecast import get_weather_forecast


class PantallaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Pantalla Principal")
        self.configurar_tamano()
        self.resizable(False, False)

    def configurar_tamano(self):
        # Maximizar la ventana pero no colocarla en pantalla completa
        self.state('zoomed')


class WidgetRectangular(tk.Frame):
    def __init__(self, master, width, height, bg):
        super().__init__(master, width=width, height=height, bg=bg)

class App:
    def __init__(self, master):
        self.master = master

        # Creamos el rectángulo vertical
        vertical_widget = WidgetRectangular(master, 1800, master.winfo_height(), "#3498DB")
        vertical_widget.place(relwidth=0.2, relheight=0.95, x=20, y=20)

        days = get_weather_forecast()



        # Creamos los rectángulos horizontales dentro del rectángulo vertical
        for i in range(6):
            if i == 0:
                # Creamos el rectángulo horizontal
                horizontal_widget = WidgetRectangular(vertical_widget, 285, vertical_widget.winfo_width()*290, "#85C1E9")
                horizontal_widget.place(relwidth=0.01, relheight=0.95, x=20, y=20, )
                horizontal_widget.grid(row=i, column=0, padx=(10, 10), pady=(10,30), sticky="ew")
            else:


                # Creamos el rectángulo horizontal
                horizontal_widget = WidgetRectangular(vertical_widget, 285, vertical_widget.winfo_width()*50, "#3498DB")
                horizontal_widget.place(relwidth=0.2, relheight=0.95, x=20, y=20, )
                horizontal_widget.grid(row=i, column=0, padx=(10,10), pady=(10,10), sticky="ew")



                day_of_week = days[i-1]["day_of_week"][0:3]
                temperature = str(days[i-1]["temperatureAvg"])[0:2] + "°C"

                icon = days[i-1]["icon"]
                for j in range(3):

                    if j == 0:
                        # Creamos el cuadro
                        texto_label = tk.Label(horizontal_widget, text=day_of_week, bg='#3498DB', fg='white',
                                               font=("Arial", 12))
                        texto_label.grid(row=0, column=j, padx=25, pady=5, sticky="nsew")
                    elif j == 1:

                        imagen = Image.open(icon)
                        imagen = imagen.resize((50, 50))  # Redimensionamos la imagen a 50x20 píxeles
                        imagen_tk = ImageTk.PhotoImage(imagen)
                        # Creamos el widget de imagen con la imagen redimensionada
                        imagen_label = tk.Label(horizontal_widget, image=imagen_tk, bg='#3498DB')
                        imagen_label.image = imagen_tk  # Keep a reference to the image
                        imagen_label.grid(row=0, column=j, padx=25, pady=5, sticky="nsew")

                    elif j == 2:
                        # Creamos el cuadro
                        texto_label = tk.Label(horizontal_widget, text=temperature, bg='#3498DB', fg='white',
                                               font=("Arial", 12))
                        texto_label.grid(row=0, column=j, padx=25, pady=5, sticky="nsew")



if __name__ == "__main__":
    pantalla_principal = PantallaPrincipal()
    app = App(pantalla_principal)
    pantalla_principal.mainloop()
