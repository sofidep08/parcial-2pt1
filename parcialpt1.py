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
                        codigo,nombre,edad,institucion,municipio,puntos = linea.split(":")
                        Agregar.participantes[codigo] ={
                            "nombre":nombre,
                            "edad":edad,
                            "institucion":institucion,
                            "municipio":municipio,
                            "puntos":puntos
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
            puntos=0

            if codigo and nombre:
                Agregar.participantes[codigo] = {
                    "nombre":nombre,
                    "edad":edad,
                    "institucion":institucion,
                    "municipio":municipio,
                    "puntos":puntos
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
                archivo.write(f"{codigo}:{participante['nombre']}:{participante['edad']}:{participante['institucion']}:{participante['municipio']}:{participante['puntos']}\n")

class Puntaje:
    @staticmethod
    def abrir_ventana_puntaje():
        ventana3=tk.Toplevel(ventana)
        ventana3.title("Puntaje")
        ventana3.geometry("450x350")
        ventana3.configure(bg="pink")

        etiqueta1=tk.Label(ventana3,text="Ingrese el codigo del participante", font=("Arial",10,"bold"), fg="white", bg="pink")
        etiqueta1.pack(pady=2)
        entrada1=tk.Entry(ventana3)
        entrada1.pack(pady=2)

        etiqueta2=tk.Label(ventana3,text="Puntaje de cultura general",font=("Arial",10,"bold"),fg="white", bg="pink")
        etiqueta2.pack(pady=2)
        entrada2=tk.Entry(ventana3)
        entrada2.pack(pady=2)

        etiqueta3=tk.Label(ventana3,text="Puntaje de proyección escénica",font=("Arial",10,"bold"),fg="white", bg="pink")
        etiqueta3.pack(pady=2)
        entrada3=tk.Entry(ventana3)
        entrada3.pack(pady=2)

        etiqueta4 = tk.Label(ventana3, text="Puntaje de entrevista", font=("Arial", 10, "bold"),fg="white", bg="pink")
        etiqueta4.pack(pady=2)
        entrada4=tk.Entry(ventana3)
        entrada4.pack(pady=2)

        def guardar_puntos():
            codigo=entrada1.get()
            if codigo in Agregar.participantes:
                try:
                    punto1=float(entrada2.get())
                    punto2=float(entrada3.get())
                    punto3=float(entrada4.get())
                    promedio=(punto1+punto2+punto3)/3
                    Agregar.participantes[codigo]["puntos"]=promedio
                    Agregar.guardar_participantes()
                    print(f"Puntaje guardado para {codigo}")
                    ventana3.destroy()
                except ValueError:
                    print("Ingrese unicamente numeros")
        boton_guardar=tk.Button(ventana3, text="Guardar", command=guardar_puntos, font=("Arial",10,"bold"), fg="turquoise",activebackground="gray",relief="raised",bd=3)
        boton_guardar.pack(pady=10)

class Mostrar:
    @staticmethod
    def abrir_ventana_mostrar():
        ventana4 = tk.Toplevel(ventana)
        ventana4.title("Participantes")
        ventana4.geometry("450x350")
        ventana4.configure(bg="pink")

        titulo4 = tk.Label(ventana4, text="Lista de Participantes",font=("Arial", 15, "bold"), fg="white", bg="pink")
        titulo4.pack(pady=10)

        texto= "Código | Nombre | Edad | Institución | Municipio | Puntaje\n"
        texto += "-" * 70 + "\n"

        for codigo, participante in Agregar.participantes.items():
            texto += f"{codigo} | {participante['nombre']} | {participante['edad']} | {participante['institucion']} | {participante['municipio']} | {participante['puntos']}\n"

        mostrar = tk.Label(ventana4, text=texto, font=("Arial", 10), bg="pink", justify="left", anchor="w")
        mostrar.pack(padx=10, pady=10)

        boton_cerrar = tk.Button(ventana4, text="Cerrar", command=ventana4.destroy,font=("Arial", 10, "bold"), fg="turquoise", relief="raised", bd=2)
        boton_cerrar.pack(pady=5)

Participante()

boton_agregar=tk.Button(ventana,text="Registrar reina",command=Agregar.abrir_ventana_participante,font=("Arial",14,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_agregar.place(x=115,y=150)

boton_puntaje=tk.Button(ventana,text="Calificar candidatas",command=Puntaje.abrir_ventana_puntaje,font=("Arial",14,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_puntaje.place(x=315,y=150)

boton_calcular=tk.Button(ventana,text="Calcular puntaje",command=ventana.quit,font=("Arial",14,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_calcular.place(x=115,y=200)

boton_mostrar=tk.Button(ventana,text="Mostrar participantes",command=Mostrar.abrir_ventana_mostrar,font=("Arial",14,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_mostrar.place(x=315,y=200)

boton_salir=tk.Button(ventana,text="Salir",command=ventana.quit,font=("Arial",14,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_salir.place(x=270,y=300)

ventana.mainloop()