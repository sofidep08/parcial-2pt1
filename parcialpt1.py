import tkinter as tk

ventana = tk.Tk()
ventana.title("Eleccion de reina")
ventana.geometry("600x500")
ventana.configure(bg="pink")

titulo= tk.Label(ventana, text="Eleccion de reina", font=("Arial",25,"bold"),fg="white", bg="pink")
titulo.place(x=165, y=50)

class Participante:
    def __init__(self):
        self.cargar_participantes()

    def cargar_participantes(self):
        try:
            with open("participantes.txt","r",encoding="utf-8") as archivo:
                for linea in archivo:
                    linea=linea.strip()
                    if linea:
                        codigo,nombre,edad,institucion,municipio = linea.split(":")
                        Agregar.participantes[codigo] ={
                            "nombre":nombre,
                            "edad":edad,
                            "institucion":institucion,
                            "municipio":municipio
                        }
            print("Participantes importados desde participantes.txt")
        except FileNotFoundError:
            print("El archivo participantes.txt no existe, se creara despues de guardar")


class Agregar:
    participantes={}
    def __init__(self,codigo, nombre, edad, institucion, municipio):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.institucion = institucion
        self.municipio = municipio

        Agregar.participantes[self.codigo] = {
            "nombre": self.nombre,
            "edad": self.edad,
            "institucion": self.institucion,
            "municipio": self.municipio
        }
        self.guardar_participantes()
        print("Participante guardada")

    def guardar_participantes(self):
        with open("participantes.txt","w",encoding="utf-8") as archivo:
            for codigo, participante in Agregar.participantes.items():
                archivo.write(f"{codigo}:{participante['nombre']}\n")

Participante()



boton_agregar=tk.Button(ventana,text="Registrar reina",command=ventana.quit,font=("Arial",14,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_agregar.place(x=115,y=150)

boton_puntaje=tk.Button(ventana,text="Calificar candidatas",command=ventana.quit,font=("Arial",14,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_puntaje.place(x=315,y=150)

boton_calcular=tk.Button(ventana,text="Calcular puntaje",command=ventana.quit,font=("Arial",14,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_calcular.place(x=115,y=200)

boton_mostrar=tk.Button(ventana,text="Mostrar participantes",command=ventana.quit,font=("Arial",14,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_mostrar.place(x=315,y=200)

#boton_puntaje=tk.Button(ventana,text="Calificar candidatas",command=ventana.quit,font=("Arial",14,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
#boton_puntaje.place(x=115,y=350)

boton_puntaje=tk.Button(ventana,text="Salir",command=ventana.quit,font=("Arial",14,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_puntaje.place(x=270,y=300)


ventana.mainloop()