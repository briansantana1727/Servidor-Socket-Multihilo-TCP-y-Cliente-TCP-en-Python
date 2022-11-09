from cmath import exp
import importlib
from textwrap import wrap
import threading
from tkinter import scrolledtext
from tkinter import *
import socket
from turtle import width

host = socket.gethostbyname(socket.gethostname())
puerto = 8080
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Función para comprobar si se puede conetar
def comprobar():
   conectado = socket1.connect((host,puerto))
   conectado = True
   if conectado: 
      conectado_list.insert(END,(f"Cliente conectado a la IP: {host}\nCon el puerto:{puerto}\n"))
   else: 
      conectado_list.insert(END,"Problema de conexión!!!!\n")
#Función para guardar el nombre del usuario 
def guardar():
    conectado_list.insert(END,f'Se guardo el nombre {entrada.get()} correctamente\n')
#Función donde se manda el mensaje y lo muestra en el historial 
def mandar():
    msg = lista_mensaje.get(1.0, "end")
    nombre = entrada.get()
    mensaje_final = nombre + ": " + msg
    socket1.send(mensaje_final.encode(encoding="ascii", errors="ignore"))
    conectado_list.insert(END,mensaje_final)
    lista_mensaje.delete(1.0,"end")

#Creación de la ventana
root = Tk()
root.title(".::: G2146006 - Brandon Jesus Santana Gudiño :::.")
root.geometry("400x500")
#Funciones para la entrada del nombre del usuario
nombre = Label(root, text="Ingresa tu nombre:")
nombre.grid(padx=10, pady=10, row=0, column=0, columnspan=2)
entrada = Entry(root,relief="groove",borderwidth=5, width=50)
entrada.grid(padx=10, pady=10, row=1, column=0, columnspan=2)
#Lista donde se muestra el historial de las funciones realizadas
conectado_list = scrolledtext.ScrolledText(root,width=45,height=10,bg="#F5EEF8")
conectado_list.grid(padx=10, pady=10, row=3, column=0, columnspan=2)
#Funciones para hacer el campo de entrada para mandar los mensajes
lista_mensaje = scrolledtext.ScrolledText(master=root,wrap= WORD,width= 45,height= 1)
lista_mensaje.tag_configure("tag-center", justify="center")
lista_mensaje.grid(padx=10, pady=10, row=4, column=0, columnspan=2)
#Todos lo bote¿ones que se ocupan
comprobar_cone = Button(root,relief="groove", borderwidth=5,cursor="hand2", bg="#D2B4DE",width=20, text="Comprobar", command=comprobar)
comprobar_cone.place(x=35, y=410)
guardar_nom = Button(root, relief="groove", borderwidth=5,cursor="hand2", bg="#76D7C4",width=45, text="Guardar nombre", command=guardar)
guardar_nom.grid(padx=10, pady=10, row=2, column=0,columnspan=2)
mandar_men = Button(root,relief="groove", borderwidth=5,cursor="hand2", width=20,bg="#ABEBC6",text="Mandar", command=mandar)
mandar_men.place(x=205, y=410)


root.mainloop()