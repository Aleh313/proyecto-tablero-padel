import tkinter as tk



class servidor_padel():

    def __init__(self):

        # Crear ventana
        self.mywindow = tk.Tk()
        self.mywindow.geometry("1924x1080")  # Resolucion de ventana
        # (1,0) se puede variar el tamaño de la ventana   (0,1) se puede minimizar la pantalla  (0,0) pantalla fija
        self.mywindow.resizable(0, 0)
        self.mywindow.title("Servidor")  # Titulo de la ventana
        self.mywindow.config(background='#C0392B')  # Color de fondo ventana

    # CANCHA 1
        # Label
        lbcancha1 = tk.Label(text="CANCHA 1", font=(
            "Arial Black", 30), fg=('#FDFEFE'), background=('#C0392B'))
        lbcancha1.place(x=150, y=30)

        lbJugador1 = tk.Label(text="jugador1:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador1.place(x=20, y=100)

        lbJugador2 = tk.Label(text="jugador2:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador2.place(x=20, y=140)

        lbJugador3 = tk.Label(text="jugador3:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador3.place(x=20, y=180)

        lbJugador4 = tk.Label(text="jugador4:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador4.place(x=20, y=220)

        # Campo de texto

        self.entrada1 = tk.StringVar()
        self.entrada2 = tk.StringVar()
        self.entrada3 = tk.StringVar()
        self.entrada4 = tk.StringVar()

        CANCHA1JUG1 = tk.Entry(self.mywindow, textvariable=self.entrada1, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA1JUG1.place(x=130, y=103)

        CANCHA1JUG2 = tk.Entry(self.mywindow, textvariable=self.entrada2, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA1JUG2.place(x=130, y=143)

        CANCHA1JUG3 = tk.Entry(self.mywindow, textvariable=self.entrada3, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA1JUG3.place(x=130, y=183)

        CANCHA1JUG4 = tk.Entry(self.mywindow, textvariable=self.entrada4, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA1JUG4.place(x=130, y=223)

        # Botones
        cargar = tk.Button(self.mywindow, text="Cargar", font=(
            "Arial Black", 10), command=self.cargar_cancha1, width=10, fg='#212F3C', background='#F1C40F')
        cargar.place(x=50, y=300)

        reset = tk.Button(self.mywindow, text="Reset", command=self.reset, font=(
            "Arial Black", 10), width=10, fg='#212F3C', background='#F1C40F')
        reset.place(x=200, y=300)

    # CANCHA 2
        #Label
        lbcancha2 = tk.Label(text="CANCHA 2", font=(
            "Arial Black", 30), fg=('#FDFEFE'), background=('#C0392B'))
        lbcancha2.place(x=1150, y=30)

        lbJugador1C2 = tk.Label(text="jugador1:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador1C2.place(x=1020, y=100)

        lbJugador2C2 = tk.Label(text="jugador2:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador2C2.place(x=1020, y=140)

        lbJugador3C2 = tk.Label(text="jugador3:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador3C2.place(x=1020, y=180)

        lbJugador4C2 = tk.Label(text="jugador4:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador4C2.place(x=1020, y=220)

        # Campo de texto

        self.entrada5 = tk.StringVar()
        self.entrada6 = tk.StringVar()
        self.entrada7 = tk.StringVar()
        self.entrada8 = tk.StringVar()

        CANCHA2JUG1 = tk.Entry(self.mywindow, textvariable=self.entrada5, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA2JUG1.place(x=130, y=703)

        CANCHA2JUG2 = tk.Entry(self.mywindow, textvariable=self.entrada6, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA2JUG2.place(x=130, y=743)

        CANCHA2JUG3 = tk.Entry(self.mywindow, textvariable=self.entrada7, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA2JUG3.place(x=130, y=783)

        CANCHA2JUG4 = tk.Entry(self.mywindow, textvariable=self.entrada8, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA2JUG4.place(x=130, y=823)

        # Botones
        cargar2 = tk.Button(self.mywindow, text="Cargar", font=(
            "Arial Black", 10), command=self.cargar_cancha2, width=10, fg='#212F3C', background='#F1C40F')
        cargar2.place(x=1050, y=300)

        reset2 = tk.Button(self.mywindow, text="Reset", command=self.reset2, font=(
            "Arial Black", 10), width=10, fg='#212F3C', background='#F1C40F')
        reset2.place(x=1200, y=300)

     # CANCHA 3
        # Label
        lbcancha3 = tk.Label(text="CANCHA 3", font=(
            "Arial Black", 30), fg=('#FDFEFE'), background=('#C0392B'))
        lbcancha3.place(x=150, y=630)

        lbJugador1C3 = tk.Label(text="jugador1:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador1C3.place(x=20, y=700)

        lbJugador2C3 = tk.Label(text="jugador2:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador2C3.place(x=20, y=740)

        lbJugador3C3 = tk.Label(text="jugador3:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador3C3.place(x=20, y=780)

        lbJugador4C3 = tk.Label(text="jugador4:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador4C3.place(x=20, y=820)

        # Campo de texto

        self.entrada9 = tk.StringVar()
        self.entrada10 = tk.StringVar()
        self.entrada11 = tk.StringVar()
        self.entrada12 = tk.StringVar()

        CANCHA2JUG1 = tk.Entry(self.mywindow, textvariable=self.entrada9, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA2JUG1.place(x=1130, y=103)

        CANCHA2JUG2 = tk.Entry(self.mywindow, textvariable=self.entrada10, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA2JUG2.place(x=1130, y=143)

        CANCHA2JUG3 = tk.Entry(self.mywindow, textvariable=self.entrada11, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA2JUG3.place(x=1130, y=183)

        CANCHA2JUG4 = tk.Entry(self.mywindow, textvariable=self.entrada12, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA2JUG4.place(x=1130, y=223)

        # Botones
        cargar3 = tk.Button(self.mywindow, text="Cargar", font=(
            "Arial Black", 10), command=self.cargar_cancha3, width=10, fg='#212F3C', background='#F1C40F')
        cargar3.place(x=50, y=900)

        reset3 = tk.Button(self.mywindow, text="Reset", command=self.reset3, font=(
            "Arial Black", 10), width=10, fg='#212F3C', background='#F1C40F')
        reset3.place(x=200, y=900)

        # CANCHA 4
        # Label
        lbcancha4 = tk.Label(text="CANCHA 4", font=(
            "Arial Black", 30), fg=('#FDFEFE'), background=('#C0392B'))
        lbcancha4.place(x=1150, y=630)

        lbJugador1C4 = tk.Label(text="jugador1:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador1C4.place(x=1020, y=700)

        lbJugador2C4 = tk.Label(text="jugador2:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador2C4.place(x=1020, y=740)

        lbJugador3C4 = tk.Label(text="jugador3:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador3C4.place(x=1020, y=780)

        lbJugador4C4 = tk.Label(text="jugador4:", font=(
            "Arial Black", 14), fg='#FDFEFE', background='#C0392B')
        lbJugador4C4.place(x=1020, y=820)

        # Campo de texto

        self.entrada13 = tk.StringVar()
        self.entrada14 = tk.StringVar()
        self.entrada15 = tk.StringVar()
        self.entrada16 = tk.StringVar()

        CANCHA4JUG1 = tk.Entry(self.mywindow, textvariable=self.entrada13, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA4JUG1.place(x=1130, y=703)

        CANCHA4JUG2 = tk.Entry(self.mywindow, textvariable=self.entrada14, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA4JUG2.place(x=1130, y=743)

        CANCHA4JUG3 = tk.Entry(self.mywindow, textvariable=self.entrada15, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA4JUG3.place(x=1130, y=783)

        CANCHA4JUG4 = tk.Entry(self.mywindow, textvariable=self.entrada16, font=(
            "Arial Black", 14), width=30, fg='#212F3C', background='#F1C40F')
        CANCHA4JUG4.place(x=1130, y=823)

        # Botones
        

        reset4 = tk.Button(self.mywindow, text="Reset", command=self.reset4, font=(
            "Arial Black", 10), width=10, fg='#212F3C', background='#F1C40F')
        reset4.place(x=1200, y=900)

    def cargar_cancha1(self):

        self.entrada1.set('')
        self.entrada2.set("")
        self.entrada3.set("")
        self.entrada4.set("")

    def cargar_cancha2(self):

        self.entrada9.set('')
        self.entrada10.set("")
        self.entrada11.set("")
        self.entrada12.set("")

    def cargar_cancha3(self):

        self.entrada5.set('')
        self.entrada6.set("")
        self.entrada7.set("")
        self.entrada8.set("")

    def cargar_cancha4(self):

        self.entrada13.set('')
        self.entrada14.set("")
        self.entrada15.set("")
        self.entrada16.set("")

    def reset(self):

        self.entrada1.set('')
        self.entrada2.set("")
        self.entrada3.set("")
        self.entrada4.set("")

    def reset2(self):
        self.entrada9.set('')
        self.entrada10.set("")
        self.entrada11.set("")
        self.entrada12.set("")

    def reset3(self):
        self.entrada5.set('')
        self.entrada6.set("")
        self.entrada7.set("")
        self.entrada8.set("")

        

    def reset4(self):

        self.entrada13.set('')
        self.entrada14.set("")
        self.entrada15.set("")
        self.entrada16.set("")



    def run(self):
        # Iniciar la ventana
        self.mywindow.mainloop()


if __name__ == '__main__':
    main = servidor_padel()
    main.run()
