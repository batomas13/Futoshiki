import random
import tkinter as tk
from datetime import datetime
from tkinter import messagebox


def principal():
    configuracio = ["FÁCIL", "SI", "derecha"]

    """"""""""""""" FUNCIONES """""""""

    def configuracion(configuracio):
        configraci = tk.Toplevel()
        configraci.title("Configuración")
        configraci.geometry("700x700")
        horas = tk.StringVar()
        minutos = tk.StringVar()
        segundos = tk.StringVar()
        facil = tk.StringVar()
        intermedio = tk.StringVar()
        dificil = tk.StringVar()
        si = tk.StringVar()
        no = tk.StringVar()
        timer = tk.StringVar()
        derecha = tk.StringVar()
        izquierda = tk.StringVar()

        """"""""""""""""""""" FUNCION """""""""""""""

        def agregar(b, configuracio):
            if b.get() in ["FÁCIL", "INTERMEDIO", "DIFÍCIL"]:
                configuracio[0] = b.get()
                messagebox.showinfo("SE AGREGÓ", "SE AGREGÓ A CONFIGURACIÓN EL NIVEL DE DIFICULTAD")
            if b.get() in ["SI", "NO", "TIMER"]:
                if b.get() == "TIMER":
                    horasLabel = tk.Label(configraci, text="Horas")
                    minutosLabel = tk.Label(configraci, text="Minutos")
                    segundosLabel = tk.Label(configraci, text="Segundos")
                    horasLabel.pack()
                    horasEntry = tk.Entry(configraci, textvariable=horas)
                    horasEntry.pack()
                    minutosLabel.pack()
                    minutosEntry = tk.Entry(configraci, textvariable=minutos)
                    minutosEntry.pack()
                    segundosLabel.pack()
                    segundosEntry = tk.Entry(configraci, textvariable=segundos)
                    segundosEntry.pack()
                    confirmarButton = tk.Button(configraci, text="Confirmar", command=lambda: aceptar(horas, minutos,
                                                                                                      segundos,
                                                                                                      configuracio))
                    confirmarButton.pack()
                else:
                    messagebox.showinfo("SE AGREGÓ", "SE AGREGÓ A CONFIGURACIÓN EL RELOJ")
                    configuracio[1] = b.get()
            if b.get() in ["derecha", "izquierda"]:
                configuracio[-1] = b.get()
                messagebox.showinfo("SE AGREGÓ", "SE AGREGÓ A CONFIGURACIÓN LA POSICIÓN DE LOS BOTONES")
            f = open("futoshiki2021configuración.dat", "wt")
            f.write(str(configuracio))
            f.close()

        def aceptar(h, m, s, configuracio):
            if "0" <= h.get() <= "2" and "0" <= m.get() <= "59" and "0" <= s.get() <= "59":
                tiempo = h.get() + ":" + m.get() + ":" + s.get()
                configuracio.insert(-1, tiempo)
                messagebox.showinfo("SE AGREGÓ", "SE AGREGÓ A CONFIGURACIÓN EL TIMER")
                f = open("futoshiki2021configuración.dat", "wt")
                f.write(str(configuracio))
                f.close()

            else:
                messagebox.showerror("Error", "Tiene que cumplir las restricciones")

        nivelLabel = tk.Label(configraci, text="Nivel: ")
        nivelLabel.pack()
        facilButton = tk.Radiobutton(configraci, text="Fácil", variable=facil, value="FÁCIL", selectcolor="red",
                                     command=
                                     lambda: agregar(facil, configuracio))
        facil.set("off")
        facilButton.pack()
        intermedioButton = tk.Radiobutton(configraci, text="Intermedio", variable=intermedio, value="INTERMEDIO",
                                          command=
                                          lambda: agregar(intermedio, configuracio))
        intermedio.set("off")
        intermedioButton.pack()
        dificilButton = tk.Radiobutton(configraci, text="Difícil", variable=dificil, value="DIFÍCIL", command=lambda:
        agregar(dificil, configuracio))
        dificil.set("off")
        dificilButton.pack()

        relojLabel = tk.Label(configraci, text="Reloj: ")
        relojLabel.pack()
        siButton = tk.Radiobutton(configraci, text="Si", variable=si, value="SI", selectcolor="red",
                                  command=lambda: agregar(si, configuracio))
        si.set("off")
        siButton.pack()
        noButton = tk.Radiobutton(configraci, text="No", variable=no, value="NO",
                                  command=lambda: agregar(no, configuracio))
        no.set("off")
        noButton.pack()
        timerButton = tk.Radiobutton(configraci, text="Timer", variable=timer, value="TIMER",
                                     command=lambda: agregar(timer, configuracio))
        timer.set("off")
        timerButton.pack()

        posicionLabel = tk.Label(configraci, text="Posición en la ventana del panel de dígitos:")
        posicionLabel.pack()
        derechaButton = tk.Radiobutton(configraci, text="Derecha", variable=derecha, value="derecha", selectcolor="red",
                                       command=lambda: agregar(derecha, configuracio))
        derecha.set("off")
        derechaButton.pack()
        izquierdaButton = tk.Radiobutton(configraci, text="Izquierda", variable=izquierda, value="izquierda",
                                         command=lambda: agregar(izquierda, configuracio))
        izquierda.set("off")
        izquierdaButton.pack()

        configraci.mainloop()

    def juego(configuracio):
        global lista_cuadricula
        global numero_botones
        global lista_jugadas
        global tupla_jugadas
        global tupla_jugador
        global listaBotones
        global countganador
        global count150
        global count3
        cuadriculas = {
            "FÁCIL": [(("1", 0, 2), ("5", 0, 3), ("1", 1, 1), ("2", 1, 2), ("3", 1, 4), ("2", 3, 3), ("4", 4, 2),
                       ("1", 4, 3), ("2", 4, 4)), (
                          ("3", 0, 1), ("4", 0, 2,), ("1", 0, 3), ("3", 2, 2), ("1", 3, 1), ("2", 3, 2),
                          ("2", 4, 1),
                          ("1", 4, 2), ("3", 4, 3)), (
                          ("1", 0, 1), ("3", 0, 3), ("1", 1, 0), ("4", 1, 3), ("2", 2, 1), ("1", 2, 2),
                          ("3", 4, 0),
                          ("2", 4, 4))], "INTERMEDIO": [(("1", 0, 2), ("5", 0, 3), ("^", 1, 1), ("1", 1, 3),
                                                         ("<", 2, 0), ("3", 2, 1), ("^", 3, 2), ("<", 4, 1),
                                                         ("3", 4, 2)), (
                                                            (">", 0, 2), ("4", 1, 4), ("^", 1, 0), ("˅", 2, 0),
                                                            ("˅", 2, 1), ("1", 2, 4), ("2", 3, 0), ("^", 3, 3),
                                                            ("^", 4, 2), ("^", 4, 4)), (
                                                            ("3", 0, 3), ("4", 0, 4), ("^", 1, 0), ("˅", 1, 2),
                                                            ("˅", 2, 1), ("˅", 2, 2), ("˅", 2, 4), ("˅", 3, 1),
                                                            ("˅", 3, 4), ("˅", 4, 1), ("^", 4, 2))], "DIFÍCIL": [
                (
                (">", 0, 0), (">", 0, 1), ("4", 2, 1), ("<", 2, 1), ("˅", 3, 0), (">", 3, 1), (">", 4, 1), ("˅", 4, 4)),
                (
                    ("1", 0, 1), ("4", 0, 4), (">", 1, 1), (">", 1, 3), ("^", 2, 1), ("˅", 2, 3), ("^", 2, 3),
                    ("˅", 3, 3),
                    (">", 3, 3), ("^", 4, 0)),
                ((">", 1, 1), ("^", 1, 4), ("˅", 2, 0), (">", 3, 0), ("^", 3, 4), (">", 4, 0), ("3", 3, 1),
                 ("˅", 3, 1))]}
        lista_jugadas = []
        tupla_jugadas = ()
        tupla_jugador = ()
        top_10_facil = []
        top_10_inter = []
        top_10_diff = []
        count3 = 0
        count150 = 0
        countganador = 0
        numero_botones = 0
        jueg = tk.Toplevel()
        jueg.geometry("1000x850")
        jueg.title("Futoshiki")
        nombre = tk.StringVar()

        """"""""""""""""""""""""" Funciones """""""""""""

        def confirmar(nombre, configuracio):
            global tupla_jugador
            tupla_jugador += (nombre.get(), datetime.now().strftime('%H:%M:%S'))
            iniciarjuegoButton.config(command=lambda: iniciar_juego(configuracio))
            messagebox.showinfo("SE AGREGÓ", "SE AGREGÓ EL NOMBRE DE USUARIO")

        def nombre_boton(x, y, B):
            global numero_botones
            global tupla_jugadas
            global lista_jugadas
            global count150
            global listaBotones
            global countganador
            global count3
            lista_jugada = lista_jugadas
            tupla_jugadas = (str(numero_botones), x, y)
            count1 = 0
            if numero_botones == 0:
                B.config(bg="RED")
                r = messagebox.showerror("ERROR", " FALTA QUE SELECCIONE UN DÍGITO")
                if r == "ok":
                    B.config(bg="White")
            for jugadas in lista_jugada:
                if jugadas[1] == x or jugadas[2] == y:
                    if jugadas[0] == str(numero_botones):
                        if jugadas[1] == x:
                            B.config(bg="RED")
                            r = messagebox.showerror("ERROR", "NO PUEDEN EXISTIR DOS CASILLAS IGUALES EN LA MISMA "
                                                              "COLUMNA")
                            if r == "ok":
                                B.config(bg="White")
                            count1 += 1
                            break
                        if jugadas[2] == y:
                            B.config(bg="RED")
                            r = messagebox.showerror("ERROR",
                                                     "NO PUEDEN EXISTIR DOS CASILLAS IGUALES EN LA MISMA FILA")
                            if r == "ok":
                                B.config(bg="White")
                            count1 += 1
                            break
                if jugadas[1] == x and jugadas[2] == y:
                    if jugadas[0] not in "^><˅":
                        count = lista_jugadas.index(jugadas)
                        lista_jugadas[count] = list(lista_jugadas[count])
                        lista_jugadas[count][0] = str(numero_botones)
                        lista_jugadas[count] = tuple(lista_jugadas[count])
                        break
                    else:
                        pass
            if count1 == 0:
                if numero_botones != 0:
                    B.config(text=numero_botones)
                    if not (str(numero_botones), x, y) in lista_jugadas:
                        lista_jugadas.append((str(numero_botones), x, y))
                        count3 += 1
                        print(count150, countganador, count3)

        def iniciar_juego(configuracio):
            global lista_cuadricula
            global tupla_jugadas
            global lista_jugadas
            global listaBotones
            global count150
            global countganador
            iniciarjuegoButton.config(command=lambda: nada())
            guardarpartidaButton.config(command=lambda: guardar())
            borrarjuegoButton.config(command=lambda: borrar_juego())
            terminarjuegoButton.config(command=lambda: terminar_juego(configuracio))
            listaBotones = []
            count1 = 165
            count2 = 300
            for juegos in cuadriculas:
                if juegos == configuracio[0]:
                    count = random.randint(0, 2)
                    lista_cuadricula = cuadriculas[juegos][count]
                    for cuadricula in cuadriculas[juegos][count]:
                        for columnas in range(5):
                            for filas in range(5):
                                if columnas == cuadricula[1] and filas == cuadricula[2]:
                                    if cuadricula[0].isdigit():
                                        C = tk.Button(jueg, compound="c", height=2, width=5, text=cuadricula[0],
                                                      bg="white")
                                        C.config(command=lambda C=C: error(C))
                                        C.place(x=count2 + columnas, y=count1 + filas)
                                        countganador += 1
                                    else:
                                        if cuadricula[0] == "˅" or cuadricula[0] == "^":
                                            C = tk.Button(jueg, text=cuadricula[0], height=1, width=2, bd=0)
                                            C.config(command=lambda C=C: error(C))
                                            C.place(x=count2 + (columnas + 10), y=count1 + (filas - 25))
                                            if len(listaBotones) < 25:
                                                B = tk.Button(jueg, compound="c", height=2, width=5, bg="white")
                                                B.config(
                                                    command=lambda columnas=columnas, filas=filas, B=B: nombre_boton(
                                                        columnas, filas, B))
                                                B.place(x=count2 + columnas, y=count1 + filas)
                                                count150 += 1
                                                listaBotones += [1]
                                        else:
                                            C = tk.Button(jueg, text=cuadricula[0], height=1, width=2, bd=0, bg="white")
                                            C.config(command=lambda C=C: error(C))
                                            C.place(x=count2 + (columnas + 50), y=count1 - (filas - 10))
                                            if len(listaBotones) < 25:
                                                B = tk.Button(jueg, compound="c", height=2, width=5, bg="white")
                                                B.config(command=lambda columnas=columnas, filas=filas, B=B:
                                                nombre_boton(columnas, filas, B))
                                                B.place(x=count2 + columnas, y=count1 + filas)
                                                count150 += 1
                                                listaBotones += [1]
                                    tupla_jugadas = (cuadricula[0], columnas, filas)
                                    lista_jugadas.append(tupla_jugadas)
                                else:
                                    if len(listaBotones) < 25:
                                        B = tk.Button(jueg, compound="c", height=2, width=5, bg="white")
                                        B.config(
                                            command=lambda columnas=columnas, filas=filas, B=B: nombre_boton(columnas,
                                                                                                             filas, B))
                                        B.place(x=count2 + columnas, y=count1 + filas)
                                        count150 += 1
                                        listaBotones += [1]
                                count2 += 75
                            count1 += 75
                            count2 = 300
                        count1 = 165

        def borrar_jugada():
            global lista_jugadas
            global tupla_jugadas
            lista_jugadas.remove(tupla_jugadas)
            messagebox.showinfo("BORRAR JUGADA", "SE BORRO LA JUGADA")

        def borrar_juego():
            global lista_cuadricula
            global lista_jugadas
            global count150
            global countganador
            listaBotones = []
            listabotones = []
            count1 = 165
            count2 = 300
            count150 = 0
            countganador = 0
            r = messagebox.askquestion("BORRAR", "¿ESTÁ SEGURO DE BORRAR EL JUEGO?", )
            if r == "yes":
                lista_jugadas = []
                for cuadricula in lista_cuadricula:
                    for columnas in range(5):
                        for filas in range(5):
                            if columnas == cuadricula[1] and filas == cuadricula[2]:
                                if cuadricula[0].isdigit():
                                    C = tk.Button(jueg, compound="c", height=2, width=5, text=cuadricula[0], bg="white")
                                    C.config(command=lambda C=C: error(C))
                                    C.place(x=count2 + columnas, y=count1 + filas)
                                    countganador += 1
                                else:
                                    if cuadricula[0] == "˅" or cuadricula[0] == "^":
                                        C = tk.Button(jueg, text=cuadricula[0], height=1, width=2, bd=0, bg="white")
                                        C.config(command=lambda C=C: error(C))
                                        C.place(x=count2 + (columnas + 10), y=count1 + (filas - 25))
                                        if len(listaBotones) < 25:
                                            B = tk.Button(jueg, compound="c", height=2, width=5, bg="white")
                                            B.config(
                                                command=lambda columnas=columnas, filas=filas, B=B: nombre_boton(
                                                    columnas, filas, B))
                                            B.place(x=count2 + columnas, y=count1 + filas)
                                            count150 += 1
                                            listaBotones += [1]
                                    else:
                                        C = tk.Button(jueg, text=cuadricula[0], height=1, width=2, bd=0, bg="white")
                                        C.config(command=lambda C=C: error(C))
                                        C.place(x=count2 + (columnas + 50), y=count1 - (filas - 10))
                                        if len(listaBotones) < 25:
                                            B = tk.Button(jueg, compound="c", height=2, width=5, bg="white")
                                            B.config(command=lambda columnas=columnas, filas=filas, B=B:
                                            nombre_boton(columnas, filas, B))
                                            B.place(x=count2 + columnas, y=count1 + filas)
                                            count150 += 1
                                            listaBotones += [1]
                                tupla_jugadas = (cuadricula[0], columnas, filas)
                                lista_jugadas.append(tupla_jugadas)
                            else:
                                if len(listaBotones) < 25:
                                    B = tk.Button(jueg, compound="c", height=2, width=5, bg="White")
                                    B.config(
                                        command=lambda columnas=columnas, filas=filas, B=B: nombre_boton(columnas,
                                                                                                         filas, B))
                                    B.place(x=count2 + columnas, y=count1 + filas)
                                    count150 += 1
                                    listaBotones += [1]
                            count2 += 75
                        count1 += 75
                        count2 = 300
                    count1 = 165

        def button1():
            global numero_botones
            numero1Button.config(bg="green")
            numero2Button.config(bg="white")
            numero3Button.config(bg="white")
            numero4Button.config(bg="white")
            numero5Button.config(bg="white")
            numero_botones = 1

        def button2():
            global numero_botones
            numero1Button.config(bg="white")
            numero2Button.config(bg="green")
            numero3Button.config(bg="white")
            numero4Button.config(bg="white")
            numero5Button.config(bg="white")
            numero_botones = 2

        def button3():
            global numero_botones
            numero1Button.config(bg="white")
            numero2Button.config(bg="white")
            numero3Button.config(bg="green")
            numero4Button.config(bg="white")
            numero5Button.config(bg="white")
            numero_botones = 3

        def button4():
            global numero_botones
            numero1Button.config(bg="white")
            numero2Button.config(bg="white")
            numero3Button.config(bg="white")
            numero4Button.config(bg="green")
            numero5Button.config(bg="white")
            numero_botones = 4

        def button5():
            global numero_botones
            numero1Button.config(bg="white")
            numero2Button.config(bg="white")
            numero3Button.config(bg="white")
            numero4Button.config(bg="white")
            numero5Button.config(bg="green")
            numero_botones = 5

        def error(C):
            C.config(bg="RED")
            r = messagebox.showerror("Error", "JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            if r == "ok":
                C.config(bg="white")

        def guardar():
            global lista_cuadricula
            global lista_jugadas
            global tupla_jugador
            f = open("futoshiki2021juegoactual.dat", "a")
            f.write(str(configuracio)),
            f.write(str(lista_cuadricula))
            f.write(str(tupla_jugador[0]))
            f.close()
            messagebox.showinfo("SE GUARDÓ", "SE GUARDÓ SU PARTIDA")

        def nada():
            pass

        def terminar_juego(configuracio):
            global lista_jugadas
            r = messagebox.askquestion("TERMINAR JUEGO", "¿ESTÁ SEGURO DE TERMINAR EL JUEGO (SI o NO)?")
            if r == "yes":
                lista_jugadas = []
                iniciar_juego(configuracio)

        futoshikiLabel = tk.Label(jueg, text="FUTOSHIKI", bg="red", bd=50, width=50, fg="White", font=22)
        futoshikiLabel.pack()
        futoshikiLabel.place(x=250, y=0)
        dificultadLabel = tk.Label(jueg, text=("NIVEL", configuracio[0]))
        dificultadLabel.place(x=500, y=120)
        nombredeljugadorLabel = tk.Label(jueg, text="Nombre del jugador: ")
        nombredeljugadorLabel.place(x=4, y=140)
        nombredeljugadorEntry = tk.Entry(jueg, textvariable=nombre, width=50)
        nombredeljugadorEntry.place(x=150, y=140)
        confirmarButton = tk.Button(jueg, text="CONFIRMAR", command=lambda: confirmar(nombre, configuracio))
        confirmarButton.place(x=455, y=135)

        numero1Button = tk.Button(jueg, text=1, command=lambda: button1(), bg="White", width=5, height=3)
        numero2Button = tk.Button(jueg, text=2, command=lambda: button2(), bg="White", width=5, height=3)
        numero3Button = tk.Button(jueg, text=3, command=lambda: button3(), bg="White", width=5, height=3)
        numero4Button = tk.Button(jueg, text=4, command=lambda: button4(), bg="White", width=5, height=3)
        numero5Button = tk.Button(jueg, text=5, command=lambda: button5(), bg="White", width=5, height=3)

        if configuracio[-1] == "derecha":
            numero1Button.place(x=900, y=200)
            numero2Button.place(x=900, y=260)
            numero3Button.place(x=900, y=320)
            numero4Button.place(x=900, y=380)
            numero5Button.place(x=900, y=440)

        if configuracio[-1] == "izquierda":
            numero1Button.place(x=60, y=200)
            numero2Button.place(x=60, y=260)
            numero3Button.place(x=60, y=320)
            numero4Button.place(x=60, y=380)
            numero5Button.place(x=60, y=440)

        if configuracio[1] == "TIMER":
            horasLabel = tk.Label(jueg, text="HORA")
            horasLabel.place(x=100, y=700)
            minutosLabel = tk.Label(jueg, text="MINUTOS")
            minutosLabel.place(x=150, y=700)
            segundosLabel = tk.Label(jueg, text="SEGUNDOS")
            segundosLabel.place(x=210, y=700)
            horaactual = tk.Label(jueg, text=configuracio[-2][0:2])
            horaactual.place(x=100, y=720)
            minutosactualLabel = tk.Label(jueg, text=configuracio[-2][3:5])
            minutosactualLabel.place(x=150, y=720)
            segundosactualesLabel = tk.Label(jueg, text=configuracio[-2][6:8])
            segundosactualesLabel.place(x=210, y=720)

        iniciarjuegoButton = tk.Button(jueg, text="INICIAR JUEGO", bg="RED", bd=10)
        iniciarjuegoButton.place(x=60, y=600)

        borrarjugadaButton = tk.Button(jueg, text="BORRAR JUGADA", bg="light blue", bd=10,
                                       command=lambda: borrar_jugada())
        borrarjugadaButton.place(x=250, y=600)

        terminarjuegoButton = tk.Button(jueg, text="TERMINAR JUEGO", bg="Green", bd=10)
        terminarjuegoButton.place(x=450, y=600)

        borrarjuegoButton = tk.Button(jueg, text="BORRAR JUEGO", bg="blue", bd=10)
        borrarjuegoButton.place(x=650, y=600)

        top10Button = tk.Button(jueg, text="TOP 10", bg="yellow", bd=10)
        top10Button.place(x=850, y=600)

        guardarpartidaButton = tk.Button(jueg, text="GUARDAR PARTIDA")
        guardarpartidaButton.place(x=450, y=800)
        cargarpartidaButton = tk.Button(jueg, text="CARGAR PARTIDA")
        cargarpartidaButton.place(x=650, y=800)

        jueg.mainloop()

    def acerca_de():
        acercade = tk.Toplevel()
        acercade.title("Acerca de")
        acercade.geometry("300x100")
        nombreprogramaLabel = tk.Label(acercade, text="Nombre del programa: ")
        nombreprogramaLabel.pack()
        nombreprogramaLabel.grid(row=0, column=0)
        nombreproLabel = tk.Label(acercade, text="FUTOSHIKI")
        nombreproLabel.grid(row=0, column=1)
        versionLabel = tk.Label(acercade, text="Version: ")
        versionLabel.grid(row=1, column=0)
        versioLabel = tk.Label(acercade, text="0.0.0")
        versioLabel.grid(row=1, column=1)
        fechacreacionLabel = tk.Label(acercade, text="Fecha de creación: ")
        fechacreacionLabel.grid(row=2, column=0)
        fechaLabel = tk.Label(acercade, text="29/06/2021")
        fechaLabel.grid(row=2, column=1)
        nombreautorLabel = tk.Label(acercade, text="Nombre del autor")
        nombreautorLabel.grid(row=3, column=0)
        nombreLabel = tk.Label(acercade, text="Tomás Coto Quesada")
        nombreLabel.grid(row=3, column=1)

        acercade.mainloop()

    def salir():
        menu.destroy()

    """"""""""""""""" Programa Principal"""""
    menu = tk.Tk()
    menu.geometry("1000x500")
    menu.title("Menu")
    menubar = tk.Menu(menu)

    menubar.add_command(label="Jugar", command=lambda: juego(configuracio))
    menubar.add_command(label="Configurar", command=lambda: configuracion(configuracio))
    menubar.add_command(label="Ayuda")
    menubar.add_command(label="Acerca de", command=lambda: acerca_de())
    menubar.add_command(label="Salir", command=lambda: salir())

    menu.config(menu=menubar)
    menu.mainloop()
