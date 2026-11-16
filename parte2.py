import time

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def eliminar_conexion(self, nodo):
        if nodo in self.conexiones:
            self.conexiones.remove(nodo)
            print(f"{self.nombre} ha desconectado a {nodo.nombre}")

    def enviar_mensaje(self, mensaje):
        print(f"\n{self.nombre} envía: {mensaje}")
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje, self.nombre)

    def recibir_mensaje(self, mensaje, remitente):
        print(f"{self.nombre} recibió de {remitente}: {mensaje}")



servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")


servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)

cliente1.agregar_conexion(servidor)
cliente2.agregar_conexion(servidor)
cliente3.agregar_conexion(servidor)


servidor.enviar_mensaje("Hola clientes, este es el servidor")


print("Simulando desconexion")
servidor.eliminar_conexion(cliente2)


time.sleep(2)


servidor.enviar_mensaje("Mensaje durante la desconexión")


print("simulando desconexion y reconexion")
servidor.agregar_conexion(cliente2)


time.sleep(2)


servidor.enviar_mensaje("¡Hola de nuevo a todos!")