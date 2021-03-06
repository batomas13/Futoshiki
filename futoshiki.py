import time
import random
import atexit
import threading
import webbrowser
import tkinter as tk
from datetime import datetime
from tkinter import messagebox


def principal():
    global top_10_facil
    global top_10_inter
    global top_10_diff
    global times
    configuracio = ["FÁCIL", "SI", "derecha"]
    top_10_inter = [('kkk', '0:0:30'), ('hum', '0:0:59'), ('Pedro', '0:2:15'), ('JUAN', '0:2:20'), ('PAPA', '0:2:25'),
                   ('him', '0:1:30'), ('her', '0:36:40'), ('MAMA', '0:3:50'), ('casa', '0:4:50'), ('TOMAS', '0:5:30')]
    top_10_facil = []
    top_10_diff = []
    times = 0

    """"""""""""""" FUNCIONES """""""""

    def configuracion(configuracio):
        global times
        times = 0
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
            if b.get() in ["FÁCIL", "INTERMEDIO", "DIFÍCIL"]:  # Analiza lo seleccionad por el usuario
                configuracio[0] = b.get()                      # Lo agrega a configuración
                messagebox.showinfo("SE AGREGÓ", "SE AGREGÓ A CONFIGURACIÓN EL NIVEL DE DIFICULTAD") # manda el mensaje
            if b.get() in ["SI", "NO", "TIMER"]:
                if b.get() == "TIMER":                                    # Si al opción del usuario es el timer
                    horasLabel = tk.Label(configraci, text="Horas")       # Despliega cada opción para el timer
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
                    messagebox.showinfo("SE AGREGÓ", "SE AGREGÓ A CONFIGURACIÓN EL RELOJ")  # Si no es timer nada más
                    configuracio[1] = b.get()                                               # lo agrega
            if b.get() in ["derecha", "izquierda"]:
                configuracio[-1] = b.get()                                                 # Analiza la posición de los
                messagebox.showinfo("SE AGREGÓ", "SE AGREGÓ A CONFIGURACIÓN LA POSICIÓN DE LOS BOTONES")  # Botones
            f = open("futoshiki2021configuración.dat", "wt")                              # Crea y guarda el archivo
            f.write(str(configuracio))                                                    # con la configuración
            f.close()

        def aceptar(h, m, s, configuracio):         # funcion para validar el timer
            global times
            hor = int(h.get())
            min = int(m.get())
            seg = int(s.get())
            if hor == 0 and min == 0 and seg == 0:        # Si todos los datos del tiempo son igual a 0 manda el error
                messagebox.showerror("ERROR", "TIENE QUE AGREGAR TIEMPO")  # Correspondiente
                return
            if 0 <= hor <= 2 and 0 <= min <= 59 and 0 <= seg <= 59:      # Si cumplen las restricciones
                times = hor * 3600 + min * 60 + seg
                tiempo = h.get() + ":" + m.get() + ":" + s.get()
                configuracio[1] = "TIMER"
                if len(configuracio) == 4:                                    # Si quiere cambiar el timer seleccionado
                    configuracio[2] = tiempo
                else:
                    configuracio.insert(-1, tiempo)                           # Si no hay tiempo seleccionado
                messagebox.showinfo("SE AGREGÓ", "SE AGREGÓ A CONFIGURACIÓN EL TIMER")
                f = open("futoshiki2021configuración.dat", "wt")
                f.write(str(configuracio))
                f.close()

            else:
                messagebox.showerror("Error", "Tiene que cumplir las restricciones")

        nivelLabel = tk.Label(configraci, text="Nivel: ")
        nivelLabel.pack()
        facilButton = tk.Radiobutton(configraci, text="Fácil", variable=facil, value="FÁCIL", selectcolor="red",
                                     command=lambda: agregar(facil, configuracio))
        facil.set("off")
        facilButton.pack()
        intermedioButton = tk.Radiobutton(configraci, text="Intermedio", variable=intermedio, value="INTERMEDIO",
                                          command=lambda: agregar(intermedio, configuracio))
        intermedio.set("off")
        intermedioButton.pack()
        dificilButton = tk.Radiobutton(configraci, text="Difícil", variable=dificil, value="DIFÍCIL",
                                       command=lambda: agregar(dificil, configuracio))
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
        global lista_guardar
        global listaBotones
        global listajugadas
        global top_10_facil
        global top_10_inter
        global countganador
        global top_10_diff
        global count150
        global running
        global count3
        global times
        global tims
        global tim
        global run
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
                    (">", 0, 0), (">", 0, 1), ("4", 2, 1), ("<", 2, 1), ("˅", 3, 0), (">", 3, 1), (">", 4, 1),
                    ("˅", 4, 4)),
                (
                    ("1", 0, 1), ("4", 0, 4), (">", 1, 1), (">", 1, 3), ("^", 2, 1), ("^", 2, 3),
                    ("˅", 3, 3),
                    (">", 3, 3), ("^", 4, 0)),
                ((">", 1, 1), ("^", 1, 4), ("˅", 2, 0), (">", 3, 0), ("^", 3, 4), (">", 4, 0), ("3", 3, 1),
                 ("˅", 3, 1))]}
        lista_jugadas = []
        lista_guardar = []
        tupla_jugadas = ()
        tupla_jugador = ()
        listajugadas = []
        tims = 0
        run = 0
        count3 = 0
        tim = times
        count150 = 0
        running = True
        countganador = 0
        numero_botones = 0
        min = tk.StringVar()
        seg = tk.StringVar()
        hora = tk.StringVar()
        nombre = tk.StringVar()

        jueg = tk.Toplevel()
        jueg.geometry("1000x850")
        jueg.title("Futoshiki")
        """"""""""""""""""""""""" Funciones """""""""""""

        def crear_cuadricula(lista_cuadricula):     # Funcion que crea la cuadricula
            global countganador
            global count150
            count150 = 0
            countganador = 0
            count1 = 165
            count2 = 300
            listaBotones = []
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
                                    C = tk.Button(jueg, text=cuadricula[0], height=1, width=2, bd=0)
                                    C.config(command=lambda C=C: error(C))
                                    C.place(x=count2 + (columnas + 10), y=count1 + (filas - 25))
                                    if len(listaBotones) < 25:
                                        B = tk.Button(jueg, compound="c", height=2, width=5, bg="white")
                                        B.config(
                                            command=lambda columnas=columnas, filas=filas, B=B: nombre_boton(
                                                columnas, filas, B, configuracio))
                                        B.place(x=count2 + columnas, y=count1 + filas)
                                        count150 += 1
                                        listaBotones += [1]
                                else:
                                    C = tk.Button(jueg, text=cuadricula[0], height=1, width=2, bd=0)
                                    C.config(command=lambda C=C: error(C))
                                    C.place(x=count2 + (columnas + 50), y=count1 - (filas - 10))
                                    if len(listaBotones) < 25:
                                        B = tk.Button(jueg, compound="c", height=2, width=5, bg="white")
                                        B.config(command=lambda columnas=columnas, filas=filas, B=B:
                                        nombre_boton(columnas, filas, B, configuracio))
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
                                                                                                     filas, B,
                                                                                                     configuracio))
                                B.place(x=count2 + columnas, y=count1 + filas)
                                count150 += 1
                                listaBotones += [1]
                        count2 += 75
                    count1 += 75
                    count2 = 300
                count1 = 165

        def confirmar(nombre, configuracio, cuadricula):         # Funcion que valida el nombre de usuario
            global tupla_jugador
            global top_10_facil
            global top_10_inter
            global top_10_diff
            for jugadores in top_10_facil:
                if jugadores[0] == nombre.get():
                    messagebox.showerror("ERROR", "EL NOMBRE NO PUEDE ESTAR EN EL TOP 10")
                    return
            for jugadores in top_10_inter:
                if jugadores[0] == nombre.get():
                    messagebox.showerror("ERROR", "EL NOMBRE NO PUEDE ESTAR EN EL TOP 10")
                    return
            for jugadores in top_10_diff:
                if jugadores[0] == nombre.get():
                    messagebox.showerror("ERROR", "EL NOMBRE NO PUEDE ESTAR EN EL TOP 10")
                    return
            if len(nombre.get()) == 0 or len(nombre.get()) > 20:
                messagebox.showerror("ERROR", "TIENE QUE SER UN NOMBRE VALIDO")
                return
            else:
                tupla_jugador = (nombre.get(),)
                iniciarjuegoButton.config(command=lambda: iniciar_juego(configuracio, cuadricula))
                messagebox.showinfo("SE AGREGÓ", "SE AGREGÓ EL NOMBRE DE USUARIO, SUERTE EN LA PARTIDA")

        def definirtop(configuracio, tupla_jugador):            # Funcion que valida si tiene que entrar al top10
            global top_10_facil
            global top_10_inter
            global top_10_diff
            if configuracio[0] == "FÁCIL":
                top_10_facil.append(tupla_jugador)
                top_10_facil = sorted(top_10_facil, key=lambda x: x[1])
                if len(top_10_facil) > 10:
                    del top_10_facil[-1]
            if configuracio[0] == "INTERMEDIO":
                top_10_inter.append(tupla_jugador)
                top_10_inter = sorted(top_10_inter, key=lambda x: x[1])
                print(len(top_10_inter))
                if len(top_10_inter) > 10:
                    del top_10_inter[-1]
            if configuracio[0] == "DIFÍCIL":
                top_10_diff.append(tupla_jugador)
                top_10_diff = sorted(top_10_diff, key=lambda x: x[1])
                if len(top_10_diff) > 10:
                    del top_10_diff[-1]

        def nombre_boton(x, y, B, configuracio):           # Funcion que determina si puede agreagar la jugada así como
            global times                                   # si ya ganó
            global numero_botones
            global tupla_jugador
            global tupla_jugadas
            global lista_jugadas
            global lista_guardar
            global listajugadas
            global listaBotones
            global countganador
            global top_10_facil
            global top_10_inter
            global top_10_diff
            global count150
            global count3
            global tim
            global tims
            global run
            global running
            lista_jugada = lista_jugadas
            tupla_jugadas = (str(numero_botones), x, y)
            count1 = 0
            if numero_botones == 0:
                B.config(bg="RED")
                r = messagebox.showerror("ERROR", " FALTA QUE SELECCIONE UN DÍGITO")
                if r == "ok":
                    B.config(bg="White")
                return
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
                            return
                        if jugadas[2] == y:
                            B.config(bg="RED")
                            r = messagebox.showerror("ERROR",
                                                     "NO PUEDEN EXISTIR DOS CASILLAS IGUALES EN LA MISMA FILA")
                            if r == "ok":
                                B.config(bg="White")
                            count1 += 1
                            return
                if jugadas[1] == x and jugadas[2] == y:
                    if jugadas[0] not in "^><˅":
                        count = lista_jugadas.index(jugadas)
                        lista_jugadas[count] = list(lista_jugadas[count])
                        lista_jugadas[count][0] = str(numero_botones)
                        lista_jugadas[count] = tuple(lista_jugadas[count])
                        listajugadas += ((str(numero_botones), x, y),)
                        B.config(text=numero_botones)
                        return
                    else:
                        if jugadas[0] == "^":
                            for jugada in lista_jugadas:
                                if jugada[1] == x - 1 and jugada[2] == y and jugada[0].isdigit():
                                    if jugada[0] > str(numero_botones):
                                        B.config(bg="Red")
                                        r = messagebox.showerror("ERROR", "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA "
                                                                      "RESTRICCIÓN DE MAYOR")
                                        if r == "ok":
                                            B.config(bg="White")
                                        return
                        if jugadas[0] == "<":
                            for jugada in lista_jugadas:
                                if jugada[1] == x and jugada[2] == y + 1 and jugada[0].isdigit():
                                    if jugada[0] < str(numero_botones):
                                        B.config(bg="Red")
                                        r = messagebox.showerror("ERROR", "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA "
                                                                      "RESTRICCIÓN DE MENOR")
                                        if r == "ok":
                                            B.config(bg="White")
                                        return
                        if jugadas[0] == ">":
                            for jugada in lista_jugadas:
                                if jugada[1] == x and jugada[2] == y + 1 and jugada[0].isdigit():
                                    if jugada[0] > str(numero_botones):
                                        B.config(bg="Red")
                                        r = messagebox.showerror("ERROR", "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA "
                                                                      "RESTRICCIÓN DE MAYOR")
                                        if r == "ok":
                                            B.config(bg="White")
                                        return
                        if jugadas[0] == "˅":
                            for jugada in lista_jugadas:
                                if jugada[1] == x - 1 and jugada[2] == y and jugada[0].isdigit():
                                    if jugada[0] < str(numero_botones):
                                        B.config(bg="Red")
                                        r = messagebox.showerror("ERROR", "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA "
                                                                      "RESTRICCIÓN DE MENOR")
                                        if r == "ok":
                                            B.config(bg="White")
                                        return
                if jugadas[1] == x and jugadas[2] == y - 1:
                    if jugadas[0] == "<":
                        for jugada in lista_jugadas:
                            if jugada[1] == x and jugada[2] == y - 1 and jugada[0].isdigit():
                                if jugada[0] > str(numero_botones):
                                    B.config(bg="Red")
                                    r = messagebox.showerror("ERROR", "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA "
                                                                      "RESTRICCIÓN DE MENOR")
                                    if r == "ok":
                                        B.config(bg="White")
                                    return
                    if jugadas[0] == ">":
                        for jugada in lista_jugadas:
                            if jugada[1] == x and jugada[2] == y - 1 and jugada[0].isdigit():
                                if jugada[0] < str(numero_botones):
                                    B.config(bg="Red")
                                    r = messagebox.showerror("ERROR", "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA "
                                                                      "RESTRICCIÓN DE MAYOR")
                                    if r == "ok":
                                        B.config(bg="White")
                                    return
                if jugadas[1] == x + 1 and jugadas[2] == y:
                    if jugadas[0] == "˅":
                        for jugada in lista_jugadas:
                            if jugada[1] == x + 1 and jugada[2] == y and jugada[0].isdigit():
                                if jugada[0] > str(numero_botones):
                                    B.config(bg="Red")
                                    r = messagebox.showerror("ERROR", "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA "
                                                                      "RESTRICCIÓN DE MAYOR")
                                    if r == "ok":
                                        B.config(bg="White")
                                    return
                    if jugadas[0] == "^":
                        for jugada in lista_jugadas:
                            if jugada[1] == x + 1 and jugada[2] == y and jugada[0].isdigit():
                                if jugada[0] < str(numero_botones):
                                    B.config(bg="Red")
                                    r = messagebox.showerror("ERROR", "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA "
                                                                      "RESTRICCIÓN DE MENOR")
                                    if r == "ok":
                                        B.config(bg="White")
                                    return
            if count1 == 0:
                if numero_botones != 0:
                    B.config(text=numero_botones)
                    if not (str(numero_botones), x, y) in lista_jugadas:
                        lista_jugadas.append((str(numero_botones), x, y))
                        count3 += 1
                        listajugadas += ((str(numero_botones), x, y),)
                        lista_guardar += ((str(numero_botones), x, y),)
                        if count150 - countganador == count3:
                            running = False
                            run = False
                            messagebox.showinfo("FELICIDADES", "¡EXCELENTE! JUEGO TERMINADO CON ÉXITO.")
                            tupla_jugador = list(tupla_jugador)
                            if configuracio[1] == "TIMER":
                                tiempo_actual = tim - times
                                mins, secs = divmod(tiempo_actual, 60)
                            else:
                                mins, secs = divmod(tims, 60)
                            h = 0
                            if mins >= 60:
                                h, mins = divmod(mins, 60)
                            tiempo_total = str(h) + ":" + str(mins) + ":" + str(secs)
                            tupla_jugador.append(tiempo_total)
                            tupla_jugador = tuple(tupla_jugador)
                            if configuracio[1] != "NO":
                                definirtop(configuracio, tupla_jugador)
                            jueg.destroy()
                            juego(configuracio)

        def iniciar_juego(configuracio, cua):             # Función que crear la cuadricula por primera vez y activa
            global lista_cuadricula                       # las otras funciones
            global lista_guardar
            global tupla_jugadas
            global lista_jugadas
            global listaBotones
            global countganador
            global count150
            global run
            run = True
            iniciarjuegoButton.config(command=lambda: nada())
            guardarpartidaButton.config(command=lambda: guardar())
            borrarjugadaButton.config(command=lambda: borrar_jugada())
            borrarjuegoButton.config(command=lambda: borrar_juego())
            terminarjuegoButton.config(command=lambda: terminar_juego(configuracio, cua))
            listaBotones = []
            count1 = 165
            count2 = 300
            if configuracio[1] == "TIMER":
                countdown_tread.start()
            if configuracio[1] == "SI":
                countdown_tread.start()
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
                                        lista_guardar += ((cuadricula[0], cuadricula[1], cuadricula[2], "P"),)
                                    else:
                                        if cuadricula[0] == "˅" or cuadricula[0] == "^":
                                            C = tk.Button(jueg, text=cuadricula[0], height=1, width=2, bd=0)
                                            C.config(command=lambda C=C: error(C))
                                            C.place(x=count2 + (columnas + 10), y=count1 + (filas - 25))
                                            lista_guardar += ((cuadricula[0], cuadricula[1], cuadricula[2], "P"),)
                                            if len(listaBotones) < 25:
                                                B = tk.Button(jueg, compound="c", height=2, width=5, bg="white")
                                                B.config(
                                                    command=lambda columnas=columnas, filas=filas, B=B: nombre_boton(
                                                        columnas, filas, B, configuracio))
                                                B.place(x=count2 + columnas, y=count1 + filas)
                                                count150 += 1
                                                listaBotones += [1]
                                        else:
                                            C = tk.Button(jueg, text=cuadricula[0], height=1, width=2, bd=0)
                                            C.config(command=lambda C=C: error(C))
                                            C.place(x=count2 + (columnas + 50), y=count1 - (filas - 10))
                                            lista_guardar += ((cuadricula[0], cuadricula[1], cuadricula[2], "P"),)
                                            if len(listaBotones) < 25:
                                                B = tk.Button(jueg, compound="c", height=2, width=5, bg="white")
                                                B.config(command=lambda columnas=columnas, filas=filas, B=B:
                                                nombre_boton(columnas, filas, B, configuracio))
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
                                                                                                             filas, B,
                                                                                                             configuracio))
                                        B.place(x=count2 + columnas, y=count1 + filas)
                                        count150 += 1
                                        listaBotones += [1]
                                count2 += 75
                            count1 += 75
                            count2 = 300
                        count1 = 165

        def borrar_jugada():             # Funcion que  borra cada jugada que el usuario hizo
            global lista_jugadas
            global listajugadas
            global count3
            count1 = 165
            count2 = 300
            if not listajugadas:
                messagebox.showerror("ERROR", " NO HAY MÁS JUGADAS PARA BORRAR.")
                return
            r = messagebox.askquestion("BORRAR JUGADA", "ESTÁ SEGURO?")
            if r == "yes":
                for filas in range(5):
                    for columnas in range(5):
                        if filas == listajugadas[-1][1] and columnas == listajugadas[-1][2]:
                            B = tk.Button(jueg, compound="c", height=2, width=5, bg="white", text="")
                            B.config(command=lambda columnas=columnas, filas=filas, B=B:
                            nombre_boton(filas, columnas, B, configuracio))
                            B.place(x=count2 + columnas, y=count1 + filas)
                        count2 += 75
                    if count2 == 675:
                        count2 = 300
                    count1 += 75
                count3 -= 1
                jugada = listajugadas[-1]
                del listajugadas[-1]
                if jugada in lista_jugadas:
                    lista_jugadas.remove(jugada)
                    messagebox.showinfo("BORRAR JUGADA", "SE BORRO LA JUGADA")

        def borrar_juego():          # Borra el juego y crea una cuadricula de forma aleatoria
            global lista_cuadricula
            global lista_jugadas
            global listajugadas
            global countganador
            global count150
            global count3
            r = messagebox.askquestion("BORRAR", "¿ESTÁ SEGURO DE BORRAR EL JUEGO?", )
            if r == "yes":
                count3 = 0
                count150 = 0
                countganador = 0
                listajugadas = []
                lista_jugadas = []
                crear_cuadricula(lista_cuadricula)

        def button1():                     # Funcion que agrega el numero y pone el boton de color verde
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

        def error(C):                   # Funcion si se presiona un boton predeterminado.
            C.config(bg="RED")
            r = messagebox.showerror("Error", "JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            if r == "ok":
                C.config(bg="white")

        def guardar():         # Funcion que guarda la partida
            global lista_cuadricula
            global lista_jugadas
            global tupla_jugador
            global lista_guardar
            global tims
            global runs
            runs = False
            tupla_jugador += (tims,)
            f = open("futoshiki2021juegoactual.dat", "w")
            f.write(str(configuracio) + "\n")
            f.write(str(lista_guardar).replace(">", ">").replace("<", "<").replace("^", "^").replace("˅", "v") + "\n")
            f.write(str(tupla_jugador))
            f.close()
            messagebox.showinfo("SE GUARDÓ", "SE GUARDÓ SU PARTIDA")

        def cargar(cuadricula):             # Funcion que crea la partida
            global tupla_jugador
            global lista_jugada
            global configuracio
            global countganador
            global count150
            global count3
            global tims
            global run
            count1 = 165
            count2 = 300
            count150 = 0
            countganador = 0
            listaBotones = []
            configuracio = []
            P = 25
            run = True
            nombres = ""
            tiempo = ""
            confg = ""
            borrarjuegoButton.config(command=lambda: borrar_juego())
            terminarjuegoButton.config(command=lambda: terminar_juego(configuracio, cuadricula))
            borrarjugadaButton.config(command=lambda: borrar_jugada())
            guardarpartidaButton.config(command=lambda: guardar())
            test = open("futoshiki2021juegoactual.dat", 'r')
            for x, b in enumerate(test):
                if x == 0:
                    configracio = b
                    for conf in configracio:
                        if conf.isalpha():
                            confg += conf
                        else:
                            if confg.isalpha():
                                configuracio += [confg]
                                confg = ""
                if x == 1:
                    cua = b.split("),")
                    for a in cua:
                        if not "P" in a:
                            P -= 1
                    for e in cua:
                        for columnas in range(5):
                            for filas in range(5):
                                if "P" in e:
                                    if columnas == int(e[7]) and filas == int(e[10]):
                                        if e[3].isdigit():
                                            C = tk.Button(jueg, text=e[3], compound="c", height=2, width=5, bg="White")
                                            C.place(x=columnas + count2, y=filas + count1)
                                            C.config(command=lambda C=C: error(C))
                                            countganador += 1
                                        else:
                                            if e[3] == "v" or e[3] == "^":
                                                C = tk.Button(jueg, height=1, width=2, bd=0)
                                                if e[3] == "v":
                                                    C.config(text="˅")
                                                else:
                                                    C.config(text=e[3])
                                                C.place(x=count2 + (columnas + 10), y=count1 + (filas - 25))
                                                if len(listaBotones) < 25:
                                                    B = tk.Button(jueg, compound="c", height=2, width=5, bg="White")
                                                    B.place(x=columnas + count2, y=filas + count1)
                                                    B.config(command=lambda B=B, columnas=int(columnas), filas=int(filas):
                                                    nombre_boton(columnas, filas, B, configuracio))
                                                    listaBotones += [1]
                                                    count150 += 1
                                            else:
                                                C = tk.Button(jueg, text=e[3], height=1, width=2, bd=0)
                                                C.config(command=lambda C=C: error(C))
                                                C.place(x=count2 + (columnas + 50), y=count1 - (filas - 10))
                                                if len(listaBotones) < 25:
                                                    B = tk.Button(jueg, compound="c", height=2, width=5, bg="White")
                                                    B.place(x=columnas + count2, y=filas + count1)
                                                    B.config(command=lambda B=B, columnas=int(columnas), filas=int(filas):
                                                    nombre_boton(columnas, filas, B, configuracio))
                                                    listaBotones += [1]
                                                    count150 += 1
                                        if e[3] == "v":
                                            tupla_jugadas = ("˅", int(columnas), int(filas))
                                        else:
                                            tupla_jugadas = (e[3], int(columnas), int(filas))
                                        lista_jugadas.append((tupla_jugadas), )
                                    else:
                                        if len(listaBotones) < P:
                                            B = tk.Button(jueg, compound="c", height=2, width=5, bg="White")
                                            B.place(x=columnas + count2, y=filas + count1)
                                            B.config(command=lambda B=B, columnas=int(columnas), filas=int(filas):
                                            nombre_boton(columnas, filas, B, configuracio))
                                            listaBotones += [1]
                                            count150 += 1
                                else:
                                    if len(listaBotones) < 25:
                                        if columnas == int(e[7]) and filas == int(e[10]):
                                            B = tk.Button(jueg, compound="c", height=2, width=5, bg="White", text=e[3])
                                            B.place(x=columnas + count2, y=filas + count1)
                                            B.config(command=lambda B=B, columnas=int(columnas), filas=int(filas):
                                            nombre_boton(columnas, filas, B, configuracio))
                                            listaBotones += [1]
                                            count150 += 1
                                            count3 += 1
                                            tupla_jugadas = (e[3], int(columnas), int(filas))
                                            lista_jugadas.append((tupla_jugadas),)
                                count2 += 75
                            count2 = 300
                            count1 += 75
                        count1 = 165
                if x == 2:
                    tuplajugador = b
                    for jugas in tuplajugador:
                        if jugas.isdigit():
                            tiempo += jugas
                        if jugas.isalpha():
                            nombres += jugas
                    tiempo = int(tiempo)
                    tupla_jugador = (nombres, tiempo)
                    tims = tiempo
                    if "TIMER" not in configuracio:
                        countdown_tread.start()
            dificultadLabel.config(text=("NIVEL", configuracio[0]))
            if configuracio[1] == "TIMER":
                tiempo = ""
                for confg in configracio:
                    if confg.isdigit() or confg == ":":
                        tiempo += confg
                configuracio.insert(-1, tiempo)
                horasLabel = tk.Label(jueg, text="HORA")
                horasLabel.place(x=100, y=700)
                minutosLabel = tk.Label(jueg, text="MINUTOS")
                minutosLabel.place(x=150, y=700)
                segundosLabel = tk.Label(jueg, text="SEGUNDOS")
                segundosLabel.place(x=210, y=700)
                horaactual = tk.Label(jueg, text=configuracio[-2][0:1])
                horaactual.place(x=100, y=720)
                minutosactualLabel = tk.Label(jueg)
                if ":" in configuracio[-2][2:4]:
                    minutosactualLabel.config(text=configuracio[-2][2:3])
                else:
                    minutosactualLabel.config(text=configuracio[-2][2:4])
                minutosactualLabel.place(x=150, y=720)
                segundosactualesLabel = tk.Label(jueg)
                if ":" in configuracio[-2][4:7]:
                    segundosactualesLabel.config(text=configuracio[-2][5:7])
                else:
                    segundosactualesLabel.config(text=configuracio[-2][4:7])
                segundosactualesLabel.place(x=210, y=720)
            test.close()

        def nada():
            pass

        def terminar_juego(configuracio, cuadriculas):                  # Funcion que termina el juego
            global lista_jugadas
            global listajugadas
            global count3
            global count150
            global countganador
            r = messagebox.askquestion("TERMINAR JUEGO", "¿ESTÁ SEGURO DE TERMINAR EL JUEGO (SI o NO)?")
            if r == "yes":
                listajugadas = []
                lista_jugadas = []
                count3 = 0
                count150 = 0
                countganador = 0
                for juegos in cuadriculas:
                    if juegos == configuracio[0]:
                        count = random.randint(0, 2)
                        lista_cuadricula = cuadriculas[juegos][count]
                        crear_cuadricula(lista_cuadricula)

        def aceptar(h, m, s, configuracio):         # funcion que valida los nuevos datos de ingreso del timer
            global times
            hor = int(h.get())
            min = int(m.get())
            seg = int(s.get())
            if hor == 0 and min == 0 and seg == 0:
                messagebox.showerror("ERROR", "TIENE QUE AGREGAR TIEMPO")
                return
            if 0 <= hor <= 2 and 0 <= min <= 59 and 0 <= seg <= 59:
                times = hor * 3600 + min * 60 + seg
                tiempo = h.get() + ":" + m.get() + ":" + s.get()
                configuracio[2] = tiempo
                messagebox.showinfo("SE AGREGÓ", "SE AGREGÓ A CONFIGURACIÓN EL TIMER")
                f = open("futoshiki2021configuración.dat", "wt")
                f.write(str(configuracio))
                f.close()
                horaactual.config(text=h.get())
                minutosactualLabel.config(text=m.get())
                segundosactualesLabel.config(text=s.get())
            else:
                messagebox.showerror("Error", "Tiene que cumplir las restricciones")

        def top10(configuracio):             # Funcion que crea la ventana con el timer
            global top_10_facil
            global top_10_inter
            global top_10_diff
            global running
            f = open("futoshiki2021top10.dat", "w")
            f.write(str(top_10_facil) + "\n")
            f.write(str(top_10_inter) + "\n")
            f.write(str(top_10_diff))
            f.close()
            running = False
            top_10 = tk.Toplevel()
            count0 = 40
            count1 = 40
            count2 = 40

            def destroy():
                global running
                running = True
                top_10.destroy()
                timer()

            top_10.title("TOP 10")
            top_10.geometry("1000x1000")
            nivelfacilLabel = tk.Label(top_10, text="Nivel Fácil:")
            jugadorfacilLabel = tk.Label(top_10, text="Jugador")
            tiempofacilLabel = tk.Label(top_10, text="Tiempo")
            nivelfacilLabel.place(x=10, y=10)
            jugadorfacilLabel.place(x=100, y=10)
            tiempofacilLabel.place(x=210, y=10)
            for c in range(len(top_10_facil)):
                tk.Label(top_10, text=c + 1).place(x=10, y=count0)
                tk.Label(top_10, text=top_10_facil[c][0]).place(x=100, y=count0)
                tk.Label(top_10, text=top_10_facil[c][1]).place(x=210, y=count0)
                count0 += 50
            tk.Label(top_10, text="Nivel Intermedio").place(x=300, y=10)
            tk.Label(top_10, text="JUGADOR").place(x=410, y=10)
            tk.Label(top_10, text="Tiempo").place(x=500, y=10)
            for c in range(len(top_10_inter)):
                tk.Label(top_10, text=c + 1).place(x=300, y=count1)
                tk.Label(top_10, text=top_10_inter[c][0]).place(x=410, y=count1)
                tk.Label(top_10, text=top_10_inter[c][1]).place(x=500, y=count1)
                count1 += 50
            tk.Label(top_10, text="Nivel Dificil").place(x=600, y=10)
            tk.Label(top_10, text="JUGADOR").place(x=700, y=10)
            tk.Label(top_10, text="Tiempo").place(x=800, y=10)
            for c in range(len(top_10_diff)):
                tk.Label(top_10, text=c + 1).place(x=600, y=count2)
                tk.Label(top_10, text=top_10_diff[c][0]).place(x=700, y=count2)
                tk.Label(top_10, text=top_10_diff[c][1]).place(x=800, y=count2)
                count2 += 50
            if configuracio[1] == "TIMER":
                top_10.protocol("WM_DELETE_WINDOW", destroy)
            top_10.mainloop()

        def timer():                 # Funcion que hace un timer
            global times
            global tim
            global running
            while running:
                minutos, segundos = divmod(times, 60)
                horas = 0
                if minutos > 60:
                    horas, minutos = divmod(minutos, 60)
                horaactual.config(text=horas)
                minutosactualLabel.config(text=minutos)
                segundosactualesLabel.config(text=segundos)
                if times == 0:
                    r = messagebox.askquestion("ERROR", "TIEMPO EXPIRADO. ¿DESEA CONTINUAR EL MISMO JUEGO (SI O NO)?")
                    if r == "yes":
                        times += tim + 1
                    else:
                        jueg.destroy()
                        juego(configuracio)

                time.sleep(1)
                #jueg.update()
                times -= 1

        def timer_inverso():           # En caso de que no haya timer funcion que cuenta el tiempo de juego del usuario
            global run
            global tims
            while run:
                tims += 1
                time.sleep(1)

        def destroy():
            global run
            run = False
            jueg.destroy()

        if configuracio[1] == "TIMER":
            countdown_tread = threading.Thread(target=timer)
        if configuracio[1] == "SI":
            countdown_tread = threading.Thread(target=timer_inverso)

        jueg.protocol("WM_DELETE_WINDOW", destroy)

        futoshikiLabel = tk.Label(jueg, text="FUTOSHIKI", bg="red", bd=50, width=50, fg="White", font=22)
        futoshikiLabel.pack()
        futoshikiLabel.place(x=250, y=0)
        dificultadLabel = tk.Label(jueg, text=("NIVEL", configuracio[0]))
        dificultadLabel.place(x=500, y=120)
        nombredeljugadorLabel = tk.Label(jueg, text="Nombre del jugador: ")
        nombredeljugadorLabel.place(x=4, y=140)
        nombredeljugadorEntry = tk.Entry(jueg, textvariable=nombre, width=50)
        nombredeljugadorEntry.place(x=150, y=140)
        confirmarButton = tk.Button(jueg, text="CONFIRMAR", command=lambda: confirmar(nombre, configuracio, cuadriculas))
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
            horaactual = tk.Label(jueg, text=configuracio[-2][0:1])
            horaactual.place(x=100, y=720)
            minutosactualLabel = tk.Label(jueg)
            if ":" in configuracio[-2][2:4]:
                minutosactualLabel.config(text=configuracio[-2][2:3])
            else:
                minutosactualLabel.config(text=configuracio[-2][2:4])
            minutosactualLabel.place(x=150, y=720)
            segundosactualesLabel = tk.Label(jueg)
            if ":" in configuracio[-2][4:7]:
                segundosactualesLabel.config(text=configuracio[-2][5:7])
            else:
                segundosactualesLabel.config(text=configuracio[-2][4:7])
            segundosactualesLabel.place(x=210, y=720)

            horacambiarLabel = tk.Label(jueg, text="HORA NUEVA")
            horacambiarLabel.place(x=50, y=750)
            minutosnuevosLabel = tk.Label(jueg, text="MINUTOS NUEVOS")
            minutosnuevosLabel.place(x=150, y=750)
            segundosnuevsoLabel = tk.Label(jueg, text="SEGUNDOS NUEVOS")
            segundosnuevsoLabel.place(x=280, y=750)
            horasEntry = tk.Entry(jueg, textvariable=hora, width=5)
            minutosEntry = tk.Entry(jueg, textvariable=min, width=5)
            segundosEntry = tk.Entry(jueg, textvariable=seg, width=5)
            horasEntry.place(x=50, y=770)
            minutosEntry.place(x=150, y=770)
            segundosEntry.place(x=280, y=770)
            okButton = tk.Button(jueg, text="ok", command=lambda: aceptar(hora, min, seg, configuracio))
            okButton.place(x=370, y=770)

        iniciarjuegoButton = tk.Button(jueg, text="INICIAR JUEGO", bg="RED", bd=10)
        iniciarjuegoButton.place(x=60, y=600)

        borrarjugadaButton = tk.Button(jueg, text="BORRAR JUGADA", bg="light blue", bd=10)
        borrarjugadaButton.place(x=250, y=600)

        terminarjuegoButton = tk.Button(jueg, text="TERMINAR JUEGO", bg="Green", bd=10)
        terminarjuegoButton.place(x=450, y=600)

        borrarjuegoButton = tk.Button(jueg, text="BORRAR JUEGO", bg="blue", bd=10)
        borrarjuegoButton.place(x=650, y=600)

        top10Button = tk.Button(jueg, text="TOP 10", bg="yellow", bd=10, command=lambda: top10(configuracio))
        top10Button.place(x=850, y=600)

        guardarpartidaButton = tk.Button(jueg, text="GUARDAR PARTIDA")
        guardarpartidaButton.place(x=450, y=800)
        cargarpartidaButton = tk.Button(jueg, text="CARGAR PARTIDA", command=lambda: cargar(cuadriculas))
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

    def ayuda():
        path = "https://drive.google.com/file/d/1sawtc9kHX_HquP2LpGDDSaBf2hKax7QA/view?usp=sharing"
        webbrowser.open_new(path)
    """"""""""""""""" Programa Principal"""""
    menu = tk.Tk()
    menu.geometry("1000x500")
    menu.title("Menu")
    menubar = tk.Menu(menu)

    menubar.add_command(label="Jugar", command=lambda: juego(configuracio))
    menubar.add_command(label="Configurar", command=lambda: configuracion(configuracio))
    menubar.add_command(label="Ayuda", command=lambda: ayuda())
    menubar.add_command(label="Acerca de", command=lambda: acerca_de())
    menubar.add_command(label="Salir", command=lambda: salir())

    menu.config(menu=menubar)
    menu.mainloop()



