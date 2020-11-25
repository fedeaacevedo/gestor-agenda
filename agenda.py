from tkinter import *
from tkinter import messagebox

lista= []

def guardar():
    print (nombre.get()+" "+app.get()+" "+correo.get())

def eliminar():
     print("Hola")

ventana = Tk()
nombre= StringVar()
app= StringVar()
apm= StringVar()
correo= StringVar()
telefono= StringVar()
conteliminar= StringVar()
colorFondo= "grey"
colorLetra= "black"
ventana.title("Gestor Clientes ZR")
ventana.geometry("700x500")
ventana.configure(background = colorFondo)

etiquetaTitulo= Label(ventana, text="Agenda de Contactos", bg=colorFondo, fg=colorLetra).place(x=270, y=10)

etiquetaN= Label(ventana, text="Nombre", bg=colorFondo, fg=colorLetra).place(x=50, y=50)
cajaN=Entry(ventana, textvariable=nombre).place(x=150, y=50)

etiquetaApp= Label(ventana, text="Apellido", bg=colorFondo,fg=colorLetra).place(x=50, y=80)
cajaApp= Entry(ventana, textvariable=app).place(x=150, y=80)

etiquetaT= Label(ventana, text="Telefono", bg=colorFondo, fg=colorLetra).place(x=50, y=140)
cajaT= Entry(ventana, textvariable=telefono).place(x=150, y=140)

etiquetaC= Label(ventana, text="Correo", bg=colorFondo, fg=colorLetra).place(x=50, y=170)
cajaC= Entry(ventana, textvariable=correo).place(x=150, y=170)

etiquetaEliminar= Label(ventana, text="Telefono: ", bg=colorFondo, fg=colorLetra).place(x=370, y=50)
spinTelefono= Spinbox(ventana, textvariable=conteliminar).place(x=450, y=50)
botoGuardar= Button(ventana, text="Guardar", command=guardar, bg="#009", fg="white").place(x=180, y=200)
botoEliminar = Button(ventana, text="Eliminar", command=eliminar, bg="#009", fg="white").place(x=480, y=80)

mainloop()


