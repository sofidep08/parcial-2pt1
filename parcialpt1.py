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
    participantes = {}
    @staticmethod
    def abrir_ventana_participante():
        ventana2 = tk.Toplevel(ventana)
        ventana2.title("Agregar")
        ventana2.geometry("450x350")
        ventana2.configure(bg="pink")

        titulo2 = tk.Label(ventana2, text="Informacion del participante", font=("Arial", 15, "bold"), fg="white", bg="pink")
        titulo2.pack(pady=2)

        etiqueta1=tk.Label(ventana2,text="Ingrese el codigo", font=("Arial", 10, "bold"),fg="white", bg="pink")
        etiqueta1.pack(pady=2)
        entrada1 = tk.Entry(ventana2)
        entrada1.pack(pady=2)

        etiqueta2 = tk.Label(ventana2, text="Ingrese el nombre", font=("Arial", 10, "bold"), fg="white", bg="pink")
        etiqueta2.pack(pady=2)
        entrada2 = tk.Entry(ventana2)
        entrada2.pack(pady=2)

        etiqueta3 = tk.Label(ventana2, text="Ingrese la edad", font=("Arial", 10, "bold"), fg="white", bg="pink")
        etiqueta3.pack(pady=2)
        entrada3 = tk.Entry(ventana2)
        entrada3.pack(pady=2)

        etiqueta4 = tk.Label(ventana2, text="Ingrese la institucion", font=("Arial", 10, "bold"), fg="white", bg="pink")
        etiqueta4.pack(pady=2)
        entrada4 = tk.Entry(ventana2)
        entrada4.pack(pady=2)

        etiqueta5 = tk.Label(ventana2, text="Ingrese el municipio", font=("Arial", 10, "bold"), fg="white", bg="pink")
        etiqueta5.pack(pady=2)
        entrada5 = tk.Entry(ventana2)
        entrada5.pack(pady=2)


        def guardar_participante():
            codigo=entrada1.get()
            nombre=entrada2.get()
            edad=entrada3.get()
            institucion=entrada4.get()
            municipio=entrada5.get()

            if codigo and nombre:
                Agregar.participantes[codigo] = {
                    "nombre":nombre,
                    "edad":edad,
                    "institucion":institucion,
                    "municipio":municipio
                }
                Agregar.guardar_participantes()
                print("Participante guardada desde entrada.")
                ventana2.destroy()

        boton_guardar = tk.Button(ventana2, text="Guardar", command=guardar_participante,font=("Arial",10,"bold"),fg="turquoise",activebackground="gray",relief="raised",bd=3)
        boton_guardar.pack(pady=10)

    @staticmethod
    def guardar_participantes():
        with open("participantes.txt","w",encoding="utf-8") as archivo:
            for codigo, participante in Agregar.participantes.items():
                archivo.write(f"{codigo}:{participante['nombre']}\n")

Participante()

boton_agregar=tk.Button(ventana,text="Registrar reina",command=Agregar.abrir_ventana_participante,font=("Arial",14,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
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