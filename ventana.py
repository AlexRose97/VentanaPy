from tkinter import *


ventana = Tk()
ventana.title("Ejemplo")
#ventana.geometry("600x500")  #ancho y alto de ventana


def enviarTexto():
    #obtener texto de cuadro de texto
    input=cuadroTxt.get(1.0,"end-1c")
    #aca podrias manipularlo
    #por ejemplo agregarle texto
    input="Se analizo:"+input
    agregarSalida(input)

def GenerarArchivo():
    input=cuadroTxtSalida.get(1.0,"end-1c")
    with open('mi_fichero', 'w') as f:
        f.write(input)


#cuadro de texto
cuadroTxt=Text(ventana,width=70,height=20)
cuadroTxt.grid(row=0, column=0)

#cuadro de texto output
cuadroTxtSalida=Text(ventana,width=70,height=10)
cuadroTxtSalida.grid(row=1, column=0)

#boton, en command se agrega el metodo que se ejecuta al dale clic
botonAnalizar=Button(ventana,text="Ejecutar", fg="black",command=enviarTexto)
botonAnalizar.grid(row=2,column=0,padx=20,pady=20)

#boton, Generear excel
botonCrear=Button(ventana,text="Crear Archivo", fg="black",command=GenerarArchivo)
botonCrear.grid(row=3,column=0,padx=20,pady=20)


#configuracion de colores de salida
cuadroTxtSalida.tag_configure("error",  foreground="red")
cuadroTxtSalida.tag_configure("exito",  foreground="green")
cuadroTxtSalida.tag_configure("normal", foreground="black")
cuadroTxtSalida.tag_configure("alert", foreground="orange")
cuadroTxtSalida.tag_configure("table", foreground="blue")



def agregarSalida(mensaje):
    cuadroTxtSalida.insert('end',mensaje+"\n","exito")



ventana.mainloop()