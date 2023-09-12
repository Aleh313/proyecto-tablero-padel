import tkinter as tk



class tablero_padel():

    def __init__(self):
        ####### crear ventana#########
        self.mywindow = tk.Tk()
        self.mywindow.geometry("1880x1080")  # resolucion de ventana
        # (1,0) se puede variar el tamño de la ventana   (0,1) se puede minimizar la pantalla  (0,0) pantalla fija
        self.mywindow.resizable(0, 0)
        self.mywindow.title("tablero padel")  # titulo de la ventana
        self.mywindow.config(background='#C0392B')  # color de fondo ventana
        self.valor_recibido = tk.Label(text="", font=(
            'Algerian', 50), fg='#FDFEFE', bg='#C0392B', pady=3, padx=3)
        self.valor_recibido.place(x=50, y=50)

    # nombres

        self.fondo1 = tk.Label(text=" ", font=(
            'Algerian', 300), fg='#FDFEFE', bg='#F39C12', pady=10, padx=800)
        self.jugador1 = tk.Label(text="Stupasuck Franco", font=(
            'Algerian', 50), fg='#FDFEFE', bg='#F39C12', pady=3, padx=3)
        self.jugador2 = tk.Label(text="Di nenno martin", font=(
            'Algerian', 50), fg='#FDFEFE', bg='#F39C12', pady=3, padx=3)
        self.jugador3 = tk.Label(text="Galan Alejandro", font=(
            'Algerian', 50), fg='#FDFEFE', bg='#F39C12', pady=3, padx=3)
        self.jugador4 = tk.Label(text="Lebron Juan", font=(
            'Algerian', 50), fg='#FDFEFE', bg='#F39C12', pady=3, padx=3)

        self.fondo1.place(x=100, y=300)
        self.jugador1.place(x=200, y=310)
        self.jugador2.place(x=200, y=400)
        self.jugador3.place(x=200, y=590)
        self.jugador4.place(x=200, y=670)

    # tablero
        self.set1pareja1 = tk.Label(text="0", font=(
            'Algerian', 145), fg='#FDFEFE', bg='#C0392B', pady=1, padx=1)
        self.set1pareja2 = tk.Label(text="0", font=(
            'Algerian', 145), fg='#FDFEFE', bg='#C0392B', pady=1, padx=1)
        self.set2pareja1 = tk.Label(text="0", font=(
            'Algerian', 145), fg='#FDFEFE', bg='#C0392B', pady=1, padx=3)
        self.set2pareja2 = tk.Label(text="0", font=(
            'Algerian', 145), fg='#FDFEFE', bg='#C0392B', pady=1, padx=3)
        self.set3pareja1 = tk.Label(text="0", font=(
            'Algerian', 145), fg='#FDFEFE', bg='#C0392B', pady=1, padx=3)
        self.set3pareja2 = tk.Label(text="0", font=(
            'Algerian', 145), fg='#FDFEFE', bg='#C0392B', pady=1, padx=3)
        self.scorepareja1 = tk.Label(text="40", font=(
            'Algerian', 145), fg='#FDFEFE', bg='#1C2833', pady=1, padx=3)
        self.scorepareja2 = tk.Label(text="40", font=(
            'Algerian', 145), fg='#FDFEFE', bg='#1C2833', pady=1, padx=3)

        self.set1pareja1.place(x=1000, y=305)
        self.set1pareja2.place(x=1000, y=544)
        self.set2pareja1.place(x=1160, y=305)
        self.set2pareja2.place(x=1160, y=544)
        self.set3pareja1.place(x=1320, y=305)
        self.set3pareja2.place(x=1320, y=544)
        self.scorepareja1.place(x=1480, y=305)
        self.scorepareja2.place(x=1480, y=544)

       


def main():
    tablero = tablero_padel()
    tablero.mywindow.mainloop()


if __name__ == "__main__":
    main()
