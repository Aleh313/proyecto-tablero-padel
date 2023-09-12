import socket
import threading
import random
import time

Jugador1Cancha1 = ""
Jugador2Cancha1 = ""
Jugador3Cancha1 = ""
Jugador4Cancha1 = ""

Jugador1Cancha2 = ""
Jugador2Cancha2 = ""
Jugador3Cancha2 = ""
Jugador4Cancha2 = ""

Jugador1Cancha3 = ""
Jugador2Cancha3 = ""
Jugador3Cancha3 = ""
Jugador4Cancha3 = ""

Jugador1Cancha3 = ""
Jugador2Cancha3 = ""
Jugador3Cancha3 = ""
Jugador4Cancha3 = ""

def Send_data():
    connected = False
    max_attempts = 3
    wait_time = 5
    attempts = 0

    while not connected and attempts < max_attempts:
        try:
            mi_socket = socket.socket()
            mi_socket.connect(('localhost', 8000))
            connected = True
        except ConnectionRefusedError:
            attempts += 1
            print(f"No se pudo establecer la conexión. Intentando de nuevo en {wait_time} segundos...")
            time.sleep(wait_time)

    if not connected:
        print("Se alcanzó el número máximo de intentos.")
        mi_socket.close()
        print("cliente se ha cerrado inesperadamente.")
        return

    

    respuesta = mi_socket.recv(1024)
    if respuesta.decode() == "temp":
        print(respuesta.decode())
        mensaje = str(T)
        mi_socket.send(mensaje.encode())
        respuesta = mi_socket.recv(1024)

    if respuesta.decode() == "humedad":
        print(respuesta.decode())
        mensaje = str(H)
        mi_socket.send(mensaje.encode())
        respuesta = mi_socket.recv(1024)
    if respuesta.decode() == "DioxCarbon":
        print(respuesta.decode())
        mensaje = str(CO2)
        mi_socket.send(mensaje.encode())
        respuesta = mi_socket.recv(1024)
    if respuesta.decode() == "MonoxCarbon":
        print(respuesta.decode())
        mensaje = str(CO)
        mi_socket.send(mensaje.encode())
        respuesta = mi_socket.recv(1024)
    if respuesta.decode() == "Ozono":
        print(respuesta.decode())
        mensaje = str(O3)
        mi_socket.send(mensaje.encode())
        respuesta = mi_socket.recv(1024)

    mi_socket.close()


def Timer_Interrupt():
    global T, H, CO, CO2, O3
    T = random.randint(0, 35)
    H = random.randint(10, 40)
    CO = random.randint(0, 100)
    CO2 = random.randint(0, 100)
    O3 = random.randint(0, 100)
# Aquí puedes poner las sentencias que quieras ejecutar cada 10 segundos
    # Por ejemplo, puedes imprimir los valores generados aleatoriamente
    print(f"T: {T}, H: {H}, CO: {CO}, CO2: {CO2}, O3: {O3}")

    # Programar la siguiente ejecución de Timer_Interrupt
    threading.Timer(10, Timer_Interrupt).start()
    Send_data()

esperando = threading.Event()


Send_data()


threading.Timer(10, Timer_Interrupt).start()
