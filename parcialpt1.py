import tkinter as tk

ventana = tk.Tk()
ventana.title("Eleccion de reina")
ventana.geometry("600x500")
ventana.configure(bg="pink")

titulo= tk.Label(ventana, text="Eleccion de reina", font=("Arial",25,"bold"),fg="white", bg="pink")
titulo.place(x=165, y=50)

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