'''
    Juego de ilusiones opticas

    Elaborado por

    - Braian Camilo Piedrahita Rodriguez
    - Fernando Jose Murcia Hincapie
'''

#Librerias usada para las interfaces graficas
from tkinter import *
from tkinter import messagebox

'''Lista que muestra los nombres de los jugadores y las respuestas en los 
    resultados finales del juego
'''
listaJugadores = {}
listaRespuestas = []

'''Método que guarda la respuesta del primer juego en la lista de respuestas'''
def guardarRespuestaJuego1(opcion, ventana):
    if opcion.get() == 1 or opcion.get() == 2 or opcion.get() == 3 or opcion.get() == 4:
        listaRespuestas.append(opcion.get())
        ventana.destroy()
        ingresarJuego2()
    else:
        messagebox.showerror("Error", "Por favor ingrese una de las opciones")

'''Método que guarda la respuesta del segundo juego en la lista de respuestas'''
def guardarRespuestaJuego2(opcion, ventana):
    if opcion.get() == 2 or opcion.get() == 3 or opcion.get() == 4 or opcion.get() == 5:
        listaRespuestas.append(opcion.get())
        ventana.destroy()
        ingresarJuego3()
    else:
        messagebox.showerror("Error", "Por favor ingrese una de las opciones")

'''Método que guarda la respuesta del tercer juego en la lista de respuestas'''
def guardarRespuestaJuego3(opcion, ventana):
    if opcion.get() == 5 or opcion.get() == 6 or opcion.get() == 7 or opcion.get() == 10:
        listaRespuestas.append(opcion.get())
        ventana.destroy()
        ingresarJuego4()
    else:
        messagebox.showerror("Error", "Por favor ingrese una de las opciones")

'''Método que guarda la respuesta del cuarto juego en la lista de respuestas'''
def guardarRespuestaJuego4(opcion, ventana):
    if opcion.get() == "izquierda" or opcion.get() == "derecha":
        listaRespuestas.append(opcion.get())
        ventana.destroy()
        ingresarJuego5()
    else:
        messagebox.showerror("Error", "Por favor ingrese una de las opciones")

'''Método que guarda la respuesta del quinto juego en la lista de respuestas'''
def guardarRespuestaJuego5(opcion, ventana):
    if opcion.get() == "pueblo" or opcion.get() == "elefante":
        listaRespuestas.append(opcion.get())
        ventana.destroy()
        abrirVentanaResultados()
    else:
        messagebox.showerror("Error", "Por favor ingrese una de las opciones")

'''Método que genera y abre la interfaz del primer juego'''
def ingresarJuego1():
    if nombre.get() == "":
        messagebox.showerror("Error", "Por favor ingrese un nombre para empezar el juego")
    else:
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

'''Método que genera y abre la interfaz del segundo juego'''
def ingresarJuego2():
    juego2 = Toplevel()
    juego2.title("Juego 2")
    juego2.geometry("500x500")
    opcion = IntVar()

    frame = Frame(juego2)
    frame.pack(fill="both", expand=True)

    imagenJuego2 = PhotoImage(file="Parcial1IA/img/juego2.png")
    Label(frame, image=imagenJuego2).pack(side=TOP, pady=10, padx=10)
    Label(frame, text="¿Cuantas personas ves aqui?").pack()

    Radiobutton(frame, text="2", variable=opcion, value=2).pack()
    Radiobutton(frame, text="3", variable=opcion, value=3).pack()
    Radiobutton(frame, text="4", variable=opcion, value=4).pack()
    Radiobutton(frame, text="5", variable=opcion, value=5).pack()

    Button(frame, text="Continuar", command=lambda:guardarRespuestaJuego2(opcion, juego2)).pack(pady=5)

    juego2.mainloop()

'''Método que genera y abre la interfaz del tercer juego'''
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

'''Método que genera y abre la interfaz del cuarto juego'''   
def ingresarJuego4():
    juego4 = Toplevel()
    juego4.title("Juego 4")
    juego4.geometry("500x450")
    opcion = StringVar()

    frame = Frame(juego4)
    frame.pack(fill="both", expand=True)

    imagenJuego4 = PhotoImage(file="Parcial1IA/img/juego4.png")
    Label(frame, image=imagenJuego4).pack(side=TOP, pady=10)
    Label(frame, text="¿Cual es más grande?").pack()

    Radiobutton(frame, text="Izquierda", variable=opcion, value="izquierda").pack()
    Radiobutton(frame, text="Derecha", variable=opcion, value="derecha").pack()

    Button(frame, text="Continuar", command=lambda:guardarRespuestaJuego4(opcion, juego4)).pack(pady=5)

    juego4.mainloop()

'''Método que genera y abre la interfaz del quinto juego'''
def ingresarJuego5():
    juego5 = Toplevel()
    juego5.title("Juego 5")
    juego5.geometry("500x450")
    opcion = StringVar()

    frame = Frame(juego5)
    frame.pack(fill="both", expand=True)

    imagenJuego5 = PhotoImage(file="Parcial1IA/img/juego5.png")
    Label(frame, image=imagenJuego5).pack(side=TOP, pady=10)
    Label(frame, text="¿Un pueblo o un elefante?").pack()

    Radiobutton(frame, text="Pueblo", variable=opcion, value="pueblo").pack()
    Radiobutton(frame, text="Elefante", variable=opcion, value="elefante").pack()

    Button(frame, text="Continuar", command=lambda:guardarRespuestaJuego5(opcion, juego5)).pack(pady=5)

    juego5.mainloop()

'''Método que genera y abre la interfaz de los resultados del jugador'''
def abrirVentanaResultados():
    ventana = Toplevel()
    ventana.title("Resultados")
    ventana.geometry("500x350")
    global listaRespuestas
    global listaJugadores

    frame = Frame(ventana)
    frame.pack(fill="both", expand=True)

    cadena = f"Usuario: {nombre.get()}\n\n1. Ves {listaRespuestas[0]} animales\n\n2. Ves {listaRespuestas[1]} personas\n\n"
    cadena += f"3. Ves {listaRespuestas[2]} animales\n\n4. Consideras que la pelota {listaRespuestas[3]} es más grande\n\n"
    cadena += f"5. Ves un {listaRespuestas[4]} en la imagen"

    Label(frame, text="Estos son los resultados de tu juego", font=("curier", 20)).pack(pady=10)
    Label(frame, text=cadena).pack(pady=5)

    listaJugadores[nombre.get()] = listaRespuestas

    listaRespuestas = []

    Button(frame, text="Cerrar", command=lambda:abrirVentanaInicio(ventana)).pack(pady=5)

    ventana.mainloop()

'''Método que genera y abre la interfaz de inicio del juego'''
def abrirVentanaInicio(ventana):
    ventana.destroy()
    root.deiconify()

'''Método que genera y abre la interfaz de los resultados de todos los jugadores'''
def abrirVentanaResultadosGrupo():
    cadena = ""
    global listaJugadores

    if len(listaJugadores)>0:
        root.withdraw()

        for i in listaJugadores.keys():
            lista = listaJugadores[i]
            cadena += f"Nombre del jugador: {i}\n\n1. El jugador vio {lista[0]} animales\n2. El jugador vio {lista[1]} personas\n3. El jugador vio {lista[2]} animales\n"
            cadena += f"4. El jugador considera que la pelota {lista[3]} es mas grande\n5. El jugador ve un {lista[4]}\n\n"


        ventana = Toplevel()
        ventana.title("Resultados")
        ventana.geometry("500x500")

        frame = Frame(ventana)
        frame.pack(fill="both", expand=True)

        Label(frame, text="Resultados de todos los jugadores", font=("curier", 20)).pack(pady=10)
        Label(frame, text=cadena).pack(pady=5)

        Button(frame, text="Cerrar", command=lambda:abrirVentanaInicio(ventana)).pack(pady=5)

        ventana.mainloop()
    else:
        messagebox.showinfo("Informacion", "Aun no ha jugado nadie, por favor juegue para mostrar los resultados generales")


#Ventana de inicio
root = Tk()
root.title("Juego de ilusiones opticas")
#root.geometry("500x650")
frame = Frame(root)
frame.pack()
#imagenPortada = PhotoImage(file="Parcial1IA/img/portada.png")
#Label(frame, image=imagenPortada).pack(side=TOP, pady=10)
Label(frame, text="Bienvenido a este juego que retara\ntu manera de ver la realidad", font="curier 14").pack(anchor="center", pady=10)
Label(frame, text="Ingresa tu nombre", font="curier 14").pack(anchor="center", pady=10)
nombre = StringVar()
entradaNombre = Entry(frame)
entradaNombre.pack(padx=20)
entradaNombre.config(bd=10, font=("curier", 20), textvariable=nombre)
botonJugar = Button(frame, text="Jugar")
botonJugar.pack(pady=10)
botonJugar.config(bd=5, font=("curier", 10), command=ingresarJuego1)
botonResultadosGenerales = Button(frame, text="Resultados generales")
botonResultadosGenerales.pack(pady=10)
botonResultadosGenerales.config(bd=5, font=("curier", 10), command=abrirVentanaResultadosGrupo)

root.mainloop()