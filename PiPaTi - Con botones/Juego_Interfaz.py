import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

rondas = 0
ganadas = 0
perdidas = 0
empatadas = 0

ventana = Tk()
ventana.title("Juego de Piedra, Papel o Tijera")
ventana.geometry("700x500")

imagen_piedra = Image.open("piedra.png")
imagen_papel = Image.open("papel.png")
imagen_tijeras = Image.open("tijeras.png")

imagen_piedra = imagen_piedra.resize((50,50))
imagen_papel = imagen_papel.resize((50,50))
imagen_tijeras = imagen_tijeras.resize((50,50))

imagen_piedra_tk = ImageTk.PhotoImage(imagen_piedra)
imagen_papel_tk = ImageTk.PhotoImage(imagen_papel)
imagen_tijeras_tk = ImageTk.PhotoImage(imagen_tijeras)

for i in range(3):
    ventana.grid_rowconfigure(i, weight=1)
    ventana.grid_columnconfigure(i, weight=1)

# Mensaje de Bienvenida
mensaje = Message(ventana, text="Bienvenido al juego clasico de Piedra, Papel o Tijera", fg="red", font=("calibri", 25))
mensaje.grid(row=0, column=1)

# Construyendo el frame del jugador
frame1 = Frame(ventana, bg="blue")
frame1.grid(sticky="ns", row=1, column=0)
for i in range(3):
    frame1.grid_rowconfigure(i, weight=1)
frame1.grid_columnconfigure(0, weight=1)
piedra_jug = Button(frame1, text="Piedra", image=imagen_piedra_tk, command=lambda: jugar("Piedra"), width=60)
piedra_jug.grid(row=0, column=0)
papel_jug = Button(frame1, text="Papel", image=imagen_papel_tk,command=lambda: jugar("Papel"), width=60)
papel_jug.grid(row=1, column=0)
tijera_jug = Button(frame1, text="Tijera", image=imagen_tijeras_tk,command=lambda: jugar("Tijeras"), width=60)
tijera_jug.grid(row=2, column=0)

# Construyendo el frame del bot
frame2 = Frame(ventana, bg="red")
frame2.grid(sticky="ns", row=1, column=2)
for i in range(3):
    frame2.grid_rowconfigure(i, weight=1)
frame2.grid_columnconfigure(0, weight=1)
piedra_bot = Button(frame2, text="Piedra",image=imagen_piedra_tk, width=60)
piedra_bot.grid(row=0, column=0)
papel_bot = Button(frame2, text="Papel",image=imagen_papel_tk, width=60)
papel_bot.grid(row=1, column=0)
tijera_bot = Button(frame2, text="Tijera",image=imagen_tijeras_tk, width=60)
tijera_bot.grid(row=2, column=0)

# Construyendo el frame del mensaje para saber el ganador
frame3 = Frame(ventana, bg="yellow")
frame3.grid(sticky="ns", row=1, column=1)

for i in range(3):
    frame3.grid_rowconfigure(i, weight=1)
frame3.grid_columnconfigure(0, weight=1)

etiqueta = Label(frame3, text="VS", fg="Black", font=("Arial", 14, "bold"))
etiqueta.grid(row=1, column=0)

def jugar(jugador):
    global empatadas, ganadas, perdidas, rondas

    rondas += 1

    combinaciones = {
        "Piedra": "Tijeras",
        "Tijeras": "Papel",
        "Papel": "Piedra"
    }

    for widget in frame3.winfo_children():
        widget.destroy()
    
    for widget in frame2.winfo_children():
        widget.destroy()
    
    for widget in frame1.winfo_children():
        widget.destroy()
    
    piedra_jug = Button(frame1, text="Piedra", image=imagen_piedra_tk, command=lambda: jugar("Piedra"), width=60)
    piedra_jug.grid(row=0, column=0)
    papel_jug = Button(frame1, text="Papel", image=imagen_papel_tk,command=lambda: jugar("Papel"), width=60)
    papel_jug.grid(row=1, column=0)
    tijera_jug = Button(frame1, text="Tijera", image=imagen_tijeras_tk,command=lambda: jugar("Tijeras"), width=60)
    tijera_jug.grid(row=2, column=0)
    
    piedra_bot = Button(frame2, text="Piedra",image=imagen_piedra_tk, width=60)
    piedra_bot.grid(row=0, column=0)
    papel_bot = Button(frame2, text="Papel",image=imagen_papel_tk, width=60)
    papel_bot.grid(row=1, column=0)
    tijera_bot = Button(frame2, text="Tijera",image=imagen_tijeras_tk, width=60)
    tijera_bot.grid(row=2, column=0)
    
    etiqueta1 = Label(frame3, text="VS", fg="Black", font=("Arial", 14, "bold"))
    etiqueta1.grid(row=1, column=0)
    
    elecciones = ("Piedra", "Papel", "Tijeras")
    bot = random.choice(elecciones)

    if bot == "Piedra":
        piedra_bot.config(bd=10, bg="blue")
    elif bot == "Papel":
        papel_bot.config(bd=10, bg="blue")
    elif bot == "Tijeras":
        tijera_bot.config(bd=10, bg="blue")

    if jugador == "Piedra":
        piedra_jug.config(bd=10, bg="red")
    elif jugador == "Papel":
        papel_jug.config(bd=10, bg="red")
    elif jugador == "Tijeras":
        tijera_jug.config(bd=10, bg="red")

    if jugador == bot:
        etiqueta1.config(text="Es un empate")
        empatadas += 1
    elif combinaciones[jugador] == bot:
        etiqueta2 = Label(frame3, text="Usted gana", fg="Black", font=("Arial", 14, "bold"))
        etiqueta2.grid(row=0, column=0)
        ganadas += 1
    else:
        etiqueta2 = Label(frame3, text="Usted Pierde", fg="Black", font=("Arial", 14, "bold"))
        etiqueta2.grid(row=2, column=0)
        perdidas += 1

def ver_estadisticas():
    global ganadas, perdidas, empatadas, rondas

    texto = f"Rondas jugadas: {rondas:,} rondas totales"
    texto += f"\n======================================"
    texto += f"\nRondas ganadas: {ganadas:,}"
    texto += f"\nRondas empatadas: {empatadas:,}"
    texto += f"\nRondas perdidas: {perdidas:,}"

    messagebox.showinfo("Estadisticas del juego", texto)

# Construyendo el frame para el boton de salida y de las estadisticas
def frame_adicional():
    frame4 = Frame(ventana, bg="purple")
    frame4.grid(sticky="ew", row=2, column=1)

    for i in range(1):
        frame4.grid_rowconfigure(i, weight=1)
    frame4.grid_columnconfigure(0, weight=1)

    salir = Button(frame4, text="Salir del juego", command=ventana.destroy)
    salir.grid(row=1, column=0)

    estadistica = Button(frame4, text="Mostrar estadisticas", command=ver_estadisticas)
    estadistica.grid(row=0, column=0)
frame_adicional()

ventana.mainloop()