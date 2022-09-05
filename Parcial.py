#import tkinter as tk
#from tkinter import ttk, messagebox
from tkinter import *
from tkinter import messagebox

listaJugadores = {}
listaRespuestas = []

def guardarRespuestaEntero(opcion):
    if opcion.get() == 1 or opcion.get() == 2 or opcion.get() == 3 or opcion.get() == 4:
        listaRespuestas.append(opcion)
        messagebox.showinfo("Informacion", "Opcion guardada correctamente")
    elif opcion.get() == 5 or opcion.get() == 6 or opcion.get() == 7 or opcion.get() == 10:
        listaRespuestas.append(opcion)
        messagebox.showinfo("Informacion", "Opcion guardada correctamente")

def guardarRespuestaJuego1(opcion, ventana):
    if opcion.get() == 1 or opcion.get() == 2 or opcion.get() == 3 or opcion.get() == 4:
        listaRespuestas.append(opcion)
        ventana.destroy()


# def guardarRespuestaCadena(opcion):
#     if opcion.get() == "Izquierda" or opcion.get() == "Derecha":
#         listaRespuestas.append(opcion)
#         messagebox.showinfo("Informacion", "Opcion guardada correctamente")
#     elif opcion.get() == "Pueblo" or opcion.get() == "Elefante":
#         listaRespuestas.append(opcion)
#         messagebox.showinfo("Informacion", "Opcion guardada correctamente")

# def guardarRespuestasJugador():
#     if len(listaRespuestas) == 5:
#         listaJugadores[nombre] = listaRespuestas


# def ingresarJuego():
#     root.withdraw()
#     #Ventana de los juegos
#     juego = tk.Toplevel()
#     juego.title("Juegos")
#     juego.geometry("500x500")
#     cuadroMadre = ttk.Notebook(juego)
#     opcionEntero = tk.IntVar()
#     opcionCadena = tk.StringVar()

#     imagen1 = tk.PhotoImage(file="Parcial1IA/img/juego1.png")
#     imagen2 = tk.PhotoImage(file="Parcial1IA/img/juego2.png")
#     imagen3 = tk.PhotoImage(file="Parcial1IA/img/juego3.png")
#     imagen4 = tk.PhotoImage(file="Parcial1IA/img/juego4.png")
#     imagen5 = tk.PhotoImage(file="Parcial1IA/img/juego5.png")

#     frame1 = ttk.Frame(cuadroMadre)
#     frame2 = ttk.Frame(cuadroMadre)
#     frame3 = ttk.Frame(cuadroMadre)
#     frame4 = ttk.Frame(cuadroMadre)
#     frame5 = ttk.Frame(cuadroMadre)

#     frame1.pack(fill="both", expand=True)
#     frame2.pack(fill="both", expand=True)
#     frame3.pack(fill="both", expand=True)
#     frame4.pack(fill="both", expand=True)
#     frame5.pack(fill="both", expand=True)

#     #Agregamos los frames al cuadro madre
#     cuadroMadre.add(frame1, text="Juego 1")
#     cuadroMadre.add(frame2, text="Juego 2")
#     cuadroMadre.add(frame3, text="Juego 3")
#     cuadroMadre.add(frame4, text="Juego 4")
#     cuadroMadre.add(frame5, text="Juego 5")

#     tk.Label(frame1, image=imagen1).pack(side=tk.TOP, pady=5, padx=5)
#     tk.Label(frame1, text="¿Cuantos animales ves aqui?").pack()
#     tk.Label(frame2, image=imagen2).pack(side=tk.TOP, pady=5, padx=5)
#     tk.Label(frame2, text="¿Cuantas personas ves aqui?").pack()
#     tk.Label(frame3, image=imagen3).pack(side=tk.TOP, pady=5, padx=5)
#     tk.Label(frame3, text="¿Cuantos animales ves aqui?").pack()
#     tk.Label(frame4, image=imagen4).pack(side=tk.TOP, pady=5, padx=5)
#     tk.Label(frame4, text="¿Cual es mas grande?").pack()
#     tk.Label(frame5, image=imagen5).pack(side=tk.TOP, pady=5, padx=5)
#     tk.Label(frame5, text="¿Un pueblo o un elefante?").pack()

#     tk.Radiobutton(frame1, text="1", variable=opcionEntero, value=1).pack()
#     tk.Radiobutton(frame1, text="2", variable=opcionEntero, value=2).pack()
#     tk.Radiobutton(frame1, text="3", variable=opcionEntero, value=3).pack()
#     tk.Radiobutton(frame1, text="4", variable=opcionEntero, value=4).pack()
#     tk.Radiobutton(frame2, text="2", variable=opcionEntero, value=2).pack()
#     tk.Radiobutton(frame2, text="3", variable=opcionEntero, value=3).pack()
#     tk.Radiobutton(frame2, text="4", variable=opcionEntero, value=4).pack()
#     tk.Radiobutton(frame2, text="5", variable=opcionEntero, value=5).pack()
#     tk.Radiobutton(frame3, text="5", variable=opcionEntero, value=5).pack()
#     tk.Radiobutton(frame3, text="6", variable=opcionEntero, value=6).pack()
#     tk.Radiobutton(frame3, text="7", variable=opcionEntero, value=7).pack()
#     tk.Radiobutton(frame3, text="10", variable=opcionEntero, value=10).pack()
#     tk.Radiobutton(frame4, text="Izquierda", variable=opcionCadena, value="Izquierda").pack()
#     tk.Radiobutton(frame4, text="Derecha", variable=opcionCadena, value="Derecha").pack()
#     tk.Radiobutton(frame5, text="Pueblo", variable=opcionCadena, value="Pueblo").pack()
#     tk.Radiobutton(frame5, text="Elefante", variable=opcionCadena, value="Elefante").pack()

#     ttk.Button(frame1, text="Guardar", command=lambda:guardarRespuestaEntero(opcionEntero)).pack(pady=5)
#     ttk.Button(frame2, text="Guardar", command=lambda:guardarRespuestaEntero(opcionEntero)).pack(pady=5)
#     ttk.Button(frame3, text="Guardar", command=lambda:guardarRespuestaEntero(opcionEntero)).pack(pady=5)
#     ttk.Button(frame4, text="Guardar", command=lambda:guardarRespuestaCadena(opcionCadena)).pack(pady=5)
#     ttk.Button(frame5, text="Guardar", command=lambda:guardarRespuestaCadena(opcionCadena)).pack(pady=5)

#     cuadroMadre.pack(expand=True, fill=tk.BOTH, pady=5, padx=5)
#     juego.mainloop()


def ingresarJuego1():
    #root.withdraw()
    juego1 = Toplevel()
    juego1.title("Juego 1")
    juego1.geometry("500x500")

    frame = Frame(juego1)
    frame.pack(fill="both", expand=True)

    imagenJuego1 = PhotoImage(file="Parcial1IA/img/juego1.png")
    Label(frame, image=imagenJuego1).pack(side=TOP, pady=10)
    Label(frame, text="¿Cuantos animales ves aqui?").pack()

    Radiobutton(frame, text="1", variable=opcionEntero, value=1).pack()
    Radiobutton(frame, text="2", variable=opcionEntero, value=2).pack()
    Radiobutton(frame, text="3", variable=opcionEntero, value=3).pack()
    Radiobutton(frame, text="4", variable=opcionEntero, value=4).pack()

    Button(frame, text="Guardar", command=lambda:guardarRespuestaJuego1(opcionEntero, juego1)).pack(pady=5)

    juego1.mainloop()


#Ventana de inicio
root = Tk()
root.title("Juego de ilusiones opticas")
frame = Frame(root)
frame.pack()
Label(frame, text="Ingresa tu nombre", font="curier 15").pack(anchor="center", pady=10)
nombre = StringVar()
entradaNombre = Entry(frame)
entradaNombre.pack()
entradaNombre.config(bd=10, font=("curier", 20), textvariable=nombre)
botonSalir = Button(frame, text="Jugar")
botonSalir.pack(pady=10)
botonSalir.config(bd=5, font=("curier", 10), command=ingresarJuego1)

opcionEntero = IntVar()

root.mainloop() 