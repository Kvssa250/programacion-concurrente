from tkinter import *
from time import *

timer = 0
semaforo_estado = "Verde"
semaforo_color = "#00FF00"

def update():
    global timer, semaforo_estado, semaforo_color
    
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    
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
    
    window.after(1000, update)

window = Tk()
window.title("Reloj con Semáforo")
window.geometry("400x300")
window.configure(bg="#F0F0F0")

time_label = Label(window, font=("Cascadia Code", 50), fg="#FE4D5F", bg="#F0F0F0")
time_label.pack()

day_label = Label(window, font=("Cascadia Code", 25, "bold"), fg="#FE4D5F", bg="#F0F0F0")
day_label.pack()

date_label = Label(window, font=("Cascadia Code", 30), fg="#FE4D5F", bg="#F0F0F0")
date_label.pack()

semaforo_label = Label(window, font=("Cascadia Code", 25, "bold"), fg="#000000", text=semaforo_estado, width=10, bg=semaforo_color)
semaforo_label.pack(pady=10)

update()

window.mainloop()