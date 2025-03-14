from tkinter import *
from time import strftime, sleep
import threading

timer = 0
semaforo_estado = "Verde"
semaforo_color = "#00FF00"

# Función para actualizar la hora, día y fecha en la interfaz
def update_reloj():

    # Se utiliza el try y except para el funcionamiento del reloj
    try:
        while True:
            time_string = strftime("%I:%M:%S %p")
            day_string = strftime("%A")
            date_string = strftime("%B %d, %Y")
            
            time_label.config(text=time_string)
            day_label.config(text=day_string)
            date_label.config(text=date_string)
            
            sleep(1) 
    except Exception as e:
        print(f"Error en update_reloj: {e}")

# Función para cambiar el estado del semáforo cada tiempo asignado
def update_semaforo():
    global timer, semaforo_estado, semaforo_color
    
    # Se utiliza el try y except para el funcionamiento del semáforo
    try:
        while True:
            timer = (timer + 1) % 24 
            
            if timer < 10:
                semaforo_estado = "Verde"
                semaforo_color = "#00FF00"
            elif timer < 14:
                semaforo_estado = "Amarillo"
                semaforo_color = "#FFFF00"
            else:
                semaforo_estado = "Rojo"
                semaforo_color = "#FF0000"
            
            semaforo_label.config(text=semaforo_estado, bg=semaforo_color)
            
            sleep(1)
    except Exception as e:
        print(f"Error en update_semaforo: {e}")

# Formato de la ventana
window = Tk()
window.title("Reloj con Semáforo")
window.geometry("500x300")
window.configure(bg="#F0F0F0")

# Formato de la hora
time_label = Label(window, font=("Cascadia Code", 50), fg="#FE4D5F", bg="#F0F0F0")
time_label.pack()

# Formato del día
day_label = Label(window, font=("Cascadia Code", 25, "bold"), fg="#FE4D5F", bg="#F0F0F0")
day_label.pack()

# Formato de la fecha
date_label = Label(window, font=("Cascadia Code", 30), fg="#FE4D5F", bg="#F0F0F0")
date_label.pack()

# Formato del semáforo
semaforo_label = Label(window, font=("Cascadia Code", 25, "bold"), fg="#000000", text=semaforo_estado, width=10, bg=semaforo_color)
semaforo_label.pack(pady=10)

# Creación de los hilos para las actualizaciones
# Se hace un try except para evitar todo tipo de error en ejecución
try:
    reloj_thread = threading.Thread(target=update_reloj, daemon=True)
    semaforo_thread = threading.Thread(target=update_semaforo, daemon=True)
    
    reloj_thread.start()
    semaforo_thread.start()
except Exception as e:
    print(f"Error al iniciar los hilos: {e}")

window.mainloop()