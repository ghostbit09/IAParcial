from tkinter import *
from tkinter import messagebox

listaJugadores = {}
listaRespuestas = []

def guardarRespuestaJuego1(opcion, ventana):
    if opcion.get() == 1 or opcion.get() == 2 or opcion.get() == 3 or opcion.get() == 4:
        listaRespuestas.append(opcion.get())
        ventana.destroy()
        ingresarJuego2()
    else:
        messagebox.showerror("Error", "Por favor ingrese una de las opciones")

def guardarRespuestaJuego2(opcion, ventana):
    if opcion.get() == 2 or opcion.get() == 3 or opcion.get() == 4 or opcion.get() == 5:
        listaRespuestas.append(opcion.get())
        ventana.destroy()
        ingresarJuego3()
    else:
        messagebox.showerror("Error", "Por favor ingrese una de las opciones")

def guardarRespuestaJuego3(opcion, ventana):
    if opcion.get() == 5 or opcion.get() == 6 or opcion.get() == 7 or opcion.get() == 10:
        listaRespuestas.append(opcion.get())
        ventana.destroy()
        ingresarJuego4()
    else:
        messagebox.showerror("Error", "Por favor ingrese una de las opciones")

def guardarRespuestaJuego4(opcion, ventana):
    if opcion.get() == "Izquierda" or opcion.get() == "Derecha":
        listaRespuestas.append(opcion.get())
        ventana.destroy()
        ingresarJuego5()
    else:
        messagebox.showerror("Error", "Por favor ingrese una de las opciones")

def guardarRespuestaJuego5(opcion, ventana):
    if opcion.get() == "Pueblo" or opcion.get() == "Elefante":
        listaRespuestas.append(opcion.get())
        ventana.destroy()
        root.deiconify()
    else:
        messagebox.showerror("Error", "Por favor ingrese una de las opciones")


def ingresarJuego1():
    root.withdraw()
    juego1 = Toplevel()
    juego1.title("Juego 1")
    juego1.geometry("500x500")
    opcion = IntVar()

    frame = Frame(juego1)
    frame.pack(fill="both", expand=True)

    imagenJuego1 = PhotoImage(file="Parcial1IA/img/juego1.png")
    Label(frame, image=imagenJuego1).pack(side=TOP, pady=10, padx=10)
    Label(frame, text="¿Cuantos animales ves aqui?").pack()

    Radiobutton(frame, text="1", variable=opcion, value=1).pack()
    Radiobutton(frame, text="2", variable=opcion, value=2).pack()
    Radiobutton(frame, text="3", variable=opcion, value=3).pack()
    Radiobutton(frame, text="4", variable=opcion, value=4).pack()

    Button(frame, text="Continuar", command=lambda:guardarRespuestaJuego1(opcion, juego1)).pack(pady=5)

    juego1.mainloop()

def ingresarJuego2():
    juego2 = Toplevel()
    juego2.title("Juego 2")
    juego2.geometry("500x500")
    opcion = IntVar()

    frame = Frame(juego2)
    frame.pack(fill="both", expand=True)

    imagenJuego2 = PhotoImage(file="Parcial1IA/img/juego2.png")
    Label(frame, image=imagenJuego2).pack(side=TOP, pady=10)
    Label(frame, text="¿Cuantas personas ves aqui?").pack()

    Radiobutton(frame, text="2", variable=opcion, value=2).pack()
    Radiobutton(frame, text="3", variable=opcion, value=3).pack()
    Radiobutton(frame, text="4", variable=opcion, value=4).pack()
    Radiobutton(frame, text="5", variable=opcion, value=5).pack()

    Button(frame, text="Continuar", command=lambda:guardarRespuestaJuego2(opcion, juego2)).pack(pady=5)

    juego2.mainloop()

def ingresarJuego3():
    juego3 = Toplevel()
    juego3.title("Juego 3")
    juego3.geometry("500x500")
    opcion = IntVar()

    frame = Frame(juego3)
    frame.pack(fill="both", expand=True)

    imagenJuego3 = PhotoImage(file="Parcial1IA/img/juego3.png")
    Label(frame, image=imagenJuego3).pack(side=TOP, pady=10)
    Label(frame, text="¿Cuantas animales ves aqui?").pack()

    Radiobutton(frame, text="5", variable=opcion, value=5).pack()
    Radiobutton(frame, text="6", variable=opcion, value=6).pack()
    Radiobutton(frame, text="7", variable=opcion, value=7).pack()
    Radiobutton(frame, text="10", variable=opcion, value=10).pack()

    Button(frame, text="Continuar", command=lambda:guardarRespuestaJuego3(opcion, juego3)).pack(pady=5)

    juego3.mainloop()
    
def ingresarJuego4():
    juego4 = Toplevel()
    juego4.title("Juego 4")
    juego4.geometry("500x500")
    opcion = StringVar()

    frame = Frame(juego4)
    frame.pack(fill="both", expand=True)

    imagenJuego4 = PhotoImage(file="Parcial1IA/img/juego4.png")
    Label(frame, image=imagenJuego4).pack(side=TOP, pady=10)
    Label(frame, text="¿Cual es más grande?").pack()

    Radiobutton(frame, text="Izquierda", variable=opcion, value="Izquierda").pack()
    Radiobutton(frame, text="Derecha", variable=opcion, value="Derecha").pack()

    Button(frame, text="Continuar", command=lambda:guardarRespuestaJuego4(opcion, juego4)).pack(pady=5)

    juego4.mainloop()

def ingresarJuego5():
    juego5 = Toplevel()
    juego5.title("Juego 5")
    juego5.geometry("500x500")
    opcion = StringVar()

    frame = Frame(juego5)
    frame.pack(fill="both", expand=True)

    imagenJuego5 = PhotoImage(file="Parcial1IA/img/juego5.png")
    Label(frame, image=imagenJuego5).pack(side=TOP, pady=10)
    Label(frame, text="¿Un pueblo o un elefante?").pack()

    Radiobutton(frame, text="Pueblo", variable=opcion, value="Pueblo").pack()
    Radiobutton(frame, text="Elefante", variable=opcion, value="Elefante").pack()

    Button(frame, text="Continuar", command=lambda:guardarRespuestaJuego5(opcion, juego5)).pack(pady=5)

    juego5.mainloop()


#Ventana de inicio
root = Tk()
root.title("Juego de ilusiones opticas")
frame = Frame(root)
frame.pack()
Label(frame, text="Ingresa tu nombre", font="curier 14").pack(anchor="center", pady=10)
nombre = StringVar()
entradaNombre = Entry(frame)
entradaNombre.pack(padx=20)
entradaNombre.config(bd=10, font=("curier", 20), textvariable=nombre)
botonSalir = Button(frame, text="Jugar")
botonSalir.pack(pady=10)
botonSalir.config(bd=5, font=("curier", 10), command=ingresarJuego1)

root.mainloop()