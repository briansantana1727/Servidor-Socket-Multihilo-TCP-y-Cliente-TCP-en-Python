import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 8080
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!Desconectado"
#Función donde se cachan los mensajes mandados
def handle_client(conn, addr):
    print(f"[Nueva Conección] {addr} Conectado.")

    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False

        print(f"[{addr}] {msg}")
        conn.send(msg.encode(FORMAT))

    conn.close()
#Función donde se inica el servidor y se crean las conexiones.
def main():
    print("[Iniciando] El servidor esta iniciado...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[Escuchando] El servidor esta escuchando a: {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("[Conecciones activas]", threading.activeCount() - 1, thread.getName())

if __name__ == "__main__":
    main()


