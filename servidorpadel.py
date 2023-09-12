import socket
import threading

Jugador1Cancha1 = "Jug1"
Jugador2Cancha1 = "Jug2"
Jugador3Cancha1 = "Jug3"
Jugador4Cancha1 = "Jug4"

Jugador1Cancha2 = ""
Jugador2Cancha2 = ""
Jugador3Cancha2 = ""
Jugador4Cancha2 = ""

Jugador1Cancha3 = ""
Jugador2Cancha3 = ""
Jugador3Cancha3 = ""
Jugador4Cancha3 = ""

Jugador1Cancha4 = ""
Jugador2Cancha4 = ""
Jugador3Cancha4 = ""
Jugador4Cancha4 = ""

print("Servidor iniciado.")
Ch1 = socket.socket()
Ch1.bind(('localhost', 8001))
Ch1.listen(5)

Ch2 = socket.socket()
Ch2.bind(('localhost', 8202))
Ch2.listen(5)

Ch3 = socket.socket()
Ch3.bind(('localhost', 8303))
Ch3.listen(5)

Ch4 = socket.socket()
Ch4.bind(('localhost', 8404))
Ch4.listen(5)

admin = socket.socket()
admin.bind(('localhost', 8313))
admin.listen(5)

# Creamos un objeto Event para esperar la variable peticion
esperando = threading.Event()



def Cancha1(conexion, addr):
    global Jugador1Cancha1
    global Jugador2Cancha1
    global Jugador3Cancha1
    global Jugador4Cancha1


    mensaje = "Nombres"
    conexion.send(mensaje.encode())
    esperando.set()
    # Esperamos a que la variable peticion sea procesada
    esperando.wait()
    peticion = conexion.recv(1024)
    esperando.set()
    # Esperamos a que la variable peticion sea procesada
    esperando.wait()
    if peticion.decode() == "Jugador1":
        mensaje = str(Jugador1Cancha1)
        conexion.send(mensaje.encode())
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    if peticion.decode() == "Jugador2":
        mensaje = str(Jugador2Cancha1)
        conexion.send(mensaje.encode())
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    if peticion.decode() == "Jugador3":
        mensaje = str(Jugador3Cancha1)
        conexion.send(mensaje.encode())
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    if peticion.decode() == "Jugador4":
        mensaje = str(Jugador4Cancha1)
        conexion.send(mensaje.encode())
        esperando.set()
        esperando.wait()
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()

    conexion.close()


def Cancha2(conexion, addr):
    global Jugador1Cancha2
    global Jugador2Cancha2
    global Jugador3Cancha2
    global Jugador4Cancha2

    mensaje = "Nombres"
    conexion.send(mensaje.encode())
    esperando.set()
    # Esperamos a que la variable peticion sea procesada
    esperando.wait()
    peticion = conexion.recv(1024)
    esperando.set()
    # Esperamos a que la variable peticion sea procesada
    esperando.wait()
    if peticion.decode() == "Jugador1":
        mensaje = str(Jugador1Cancha2)
        conexion.send(mensaje.encode())
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    if peticion.decode() == "Jugador2":
        mensaje = str(Jugador2Cancha2)
        conexion.send(mensaje.encode())
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    if peticion.decode() == "Jugador3":
        mensaje = str(Jugador3Cancha2)
        conexion.send(mensaje.encode())
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    if peticion.decode() == "Jugador4":
        mensaje = str(Jugador4Cancha2)
        conexion.send(mensaje.encode())
        esperando.set()
        esperando.wait()
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    conexion.close()


def Cancha3(conexion, addr):
    global Jugador1Cancha3
    global Jugador2Cancha3
    global Jugador3Cancha3
    global Jugador4Cancha3

    mensaje = "Nombres"
    conexion.send(mensaje.encode())
    esperando.set()
    # Esperamos a que la variable peticion sea procesada
    esperando.wait()
    peticion = conexion.recv(1024)
    esperando.set()
    # Esperamos a que la variable peticion sea procesada
    esperando.wait()
    if peticion.decode() == "Jugador1":
        mensaje = str(Jugador1Cancha3)
        conexion.send(mensaje.encode())
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    if peticion.decode() == "Jugador2":
        mensaje = str(Jugador2Cancha3)
        conexion.send(mensaje.encode())
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    if peticion.decode() == "Jugador3":
        mensaje = str(Jugador3Cancha3)
        conexion.send(mensaje.encode())
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    if peticion.decode() == "Jugador4":
        mensaje = str(Jugador4Cancha3)
        conexion.send(mensaje.encode())
        esperando.set()
        esperando.wait()
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()

    conexion.close()


def Cancha4(conexion, addr):
    global Jugador1Cancha4
    global Jugador2Cancha4
    global Jugador3Cancha4
    global Jugador4Cancha4

    mensaje = "Nombres"
    conexion.send(mensaje.encode())
    esperando.set()
    # Esperamos a que la variable peticion sea procesada
    esperando.wait()
    peticion = conexion.recv(1024)
    esperando.set()
    # Esperamos a que la variable peticion sea procesada
    esperando.wait()
    if peticion.decode() == "Jugador1":
        mensaje = str(Jugador1Cancha4)
        conexion.send(mensaje.encode())
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    if peticion.decode() == "Jugador2":
        mensaje = str(Jugador2Cancha4)
        conexion.send(mensaje.encode())
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    if peticion.decode() == "Jugador3":
        mensaje = str(Jugador3Cancha4)
        conexion.send(mensaje.encode())
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()
    if peticion.decode() == "Jugador4":
        mensaje = str(Jugador4Cancha4)
        conexion.send(mensaje.encode())
        esperando.set()
        esperando.wait()
        peticion = conexion.recv(1024)
        esperando.set()
        esperando.wait()

    conexion.close()


def aceptar_conexiones_admin():
    # Función que acepta conexiones entrantes y crea un hilo para manejar cada conexión
    while True:
        conexion, addr = admin.accept()
        print("Cliente conectado: ", addr)

        # Creamos un hilo separado para manejar la conexión entrante
        hilo = threading.Thread(target=manejar_admin, args=(conexion, addr))
        hilo.start()


def aceptar_conexiones_Cancha1():
    # Función que acepta conexiones entrantes y crea un hilo para manejar cada conexión
    while True:
        conexion1, addr1 = Ch1.accept()
        print("Cliente conectado: ", addr1)

        # Creamos un hilo separado para manejar la conexión entrante
        hilo1 = threading.Thread(target=Cancha1, args=(conexion1, addr1))
        hilo1.start()


def aceptar_conexiones_Cancha2():
    # Función que acepta conexiones entrantes y crea un hilo para manejar cada conexión
    while True:
        conexion2, addr2 = Ch2.accept()
        print("Cliente conectado: ", addr2)

        # Creamos un hilo separado para manejar la conexión entrante
        hilo2 = threading.Thread(target=Cancha2, args=(conexion2, addr2))
        hilo2.start()


def aceptar_conexiones_Cancha3():
    # Función que acepta conexiones entrantes y crea un hilo para manejar cada conexión
    while True:
        conexion3, addr3 = Ch3.accept()
        print("Cliente conectado: ", addr3)

        # Creamos un hilo separado para manejar la conexión entrante
        hilo3 = threading.Thread(target=Cancha3, args=(conexion3, addr3))
        hilo3.start()


def aceptar_conexiones_Cancha4():
    # Función que acepta conexiones entrantes y crea un hilo para manejar cada conexión
    while True:
        conexion4, addr4 = Ch4.accept()
        print("Cliente conectado: ", addr4)

        # Creamos un hilo separado para manejar la conexión entrante
        hilo4 = threading.Thread(target=Cancha4, args=(conexion4, addr4))
        hilo4.start()


# Creamos dos hilos separados para manejar las conexiones entrantes
hilo= threading.Thread(target=manejar_admin)
hilo.start()

hilo2 = threading.Thread(target=Cancha1)
hilo2.start()

hilo2 = threading.Thread(target=Cancha2)
hilo2.start()

hilo3 = threading.Thread(target=Cancha3)
hilo3.start()

hilo4 = threading.Thread(target=Cancha4)
hilo4.start()
