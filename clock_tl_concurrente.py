from tkinter import *
from time import strftime, sleep
from concurrent.futures import ThreadPoolExecutor

timer = 0
semaforo_estado = "Verde"
semaforo_color = "#00FF00"

# Función para actualizar la hora, día y fecha en la interfaz
def update_clock():
    while True:
        time_string = strftime("%I:%M:%S %p")
        day_string = strftime("%A")
        date_string = strftime("%B %d, %Y")
        
        time_label.config(text=time_string)
        day_label.config(text=day_string)
        date_label.config(text=date_string)
        
        sleep(1)  # Pausa para evitar alto consumo de CPU

# Función para cambiar el estado del semáforo cada tiempo que tiene asignado
def update_semaforo():
    global timer, semaforo_estado, semaforo_color
    while True:
        # EL temporizador incrementa en cada vuelta y reinicia cuando llega a 24
        timer = (timer + 1) % 24 
        
        # El semáforo dura 10 segundos en verde
        if timer < 10:
            semaforo_estado = "Verde"
            semaforo_color = "#00FF00"
        # El semáforo dura 4 segundos en amarillo    
        elif timer < 14:
            semaforo_estado = "Amarillo"
            semaforo_color = "#FFFF00"
        # El semáforo dura 10 segundos en rojo
        else:
            semaforo_estado = "Rojo"
            semaforo_color = "#FF0000"

        semaforo_label.config(text=semaforo_estado, bg=semaforo_color)
        
        sleep(1)

# Formato de la ventana
window = Tk()
window.title("Reloj con Semáforo")
window.geometry("500x300")
window.configure(bg="#F0F0F0")

# Formato de la hora
time_label = Label(window, font=("Cascadia Code", 50), fg="#FE4D5F", bg="#F0F0F0")
time_label.pack()

# Formato del dia
day_label = Label(window, font=("Cascadia Code", 25, "bold"), fg="#FE4D5F", bg="#F0F0F0")
day_label.pack()

# Formato de la fecha
date_label = Label(window, font=("Cascadia Code", 30), fg="#FE4D5F", bg="#F0F0F0")
date_label.pack()

# Formato del semáforo
semaforo_label = Label(window, font=("Cascadia Code", 25, "bold"), fg="#000000", text=semaforo_estado, width=10, bg=semaforo_color)
semaforo_label.pack(pady=10)

# Creacion de los hilos para separar las actualizaciones
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(update_clock)
    executor.submit(update_semaforo)

window.mainloop()