import tkinter as tk
from tkinter import messagebox


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x350")
        self.resizable(0, 0)
        self.title("Calculadora")
        self.iconbitmap("calculadora.ico")
        #Atributos de clase
        self.expresion = ""
        #Caja de texto
        self.entrada = None
        #StringVar lo utilizamos para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        #Creamos los componentes
        self.crearcomponentes()

    #Metodos de clase
    def crearcomponentes(self):
        #Creamos un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=50, background="grey")
        entrada_frame.pack(side=tk.TOP)

        #Caja de texto
        entrada = tk.Entry(entrada_frame, font=("arial", 18, "bold"), textvariable=self.entrada_texto, width=22, justify=tk.RIGHT) #bold es negrita
        entrada.grid(row=0, column=0, ipady=10, ipadx=5)

        #Creamos otro Frame para la parte inferior
        botones_frame = tk.Frame(self, width=400, height=450, background="grey")
        botones_frame.pack()

        #Botones - Primer renglon
        #Limpiar
        boton_limpieza = tk.Button(botones_frame, text="C", width=32, height=3, bd=0, bg= "#eee", cursor="hand2", command=self.limpiar) #bd = border ; cursor buscar en gg
        boton_limpieza.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        #Dividir
        boton_dividir = tk.Button(botones_frame, text="/", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.evento_click("/")) #Con el parametro lambda no llama la funcion a la primera
        boton_dividir.grid(row=0, column=3, padx=1, pady=1)

        #Segundo renglon
        #Siete
        boton_siete = tk.Button(botones_frame, text="7", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.evento_click(7))
        boton_siete.grid(row=1, column=0, padx=1, pady=1)

        #Ocho
        boton_ocho = tk.Button(botones_frame, text="8", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                                command=lambda: self.evento_click(8))
        boton_ocho.grid(row=1, column=1, padx=1, pady=1)

        #Nueve
        boton_nueve = tk.Button(botones_frame, text="9", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                                command=lambda: self.evento_click(9))
        boton_nueve.grid(row=1, column=2, padx=1, pady=1)

        #Multiplicacion
        boton_multiplicar = tk.Button(botones_frame, text="*", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                                command=lambda: self.evento_click("*"))
        boton_multiplicar.grid(row=1, column=3, padx=1, pady=1)

        #Tercer renglon
        #Cuatro
        boton_cuatro = tk.Button(botones_frame, text="4", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                                command=lambda: self.evento_click(4))
        boton_cuatro.grid(row=2, column=0, padx=1, pady=1)

        #Cinco
        boton_cinco = tk.Button(botones_frame, text="5", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                                command=lambda: self.evento_click(5))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)

        #Seis
        boton_seis = tk.Button(botones_frame, text="6", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                                command=lambda: self.evento_click(6))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)

        #Resta
        boton_resta = tk.Button(botones_frame, text="-", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                                command=lambda: self.evento_click("-"))
        boton_resta.grid(row=2, column=3, padx=1, pady=1)

        #Tercer renglon
        #Uno
        boton_uno = tk.Button(botones_frame, text="1", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                                command=lambda: self.evento_click(1))
        boton_uno.grid(row=3, column=0, padx=1, pady=1)

        #Dos
        boton_dos = tk.Button(botones_frame, text="2", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                                command=lambda: self.evento_click(2))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)

        #Tres
        boton_tres = tk.Button(botones_frame, text="3", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                                command=lambda: self.evento_click(3))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)

        #Suma
        boton_suma = tk.Button(botones_frame, text="+", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                                command=lambda: self.evento_click("+"))
        boton_suma.grid(row=3, column=3, padx=1, pady=1)

        #Cuarto Renglon
        #Cero
        boton_cero = tk.Button(botones_frame, text="0", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
                                command=lambda: self.evento_click(0))
        boton_cero.grid(row=4, column=0, padx=1, pady=1, columnspan=2)

        #Punto
        boton_punto = tk.Button(botones_frame, text=".", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                                command=lambda: self.evento_click("."))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)

        #Igual
        boton_igual = tk.Button(botones_frame, text="=", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                                command=self.evento_evaluar)
        boton_igual.grid(row=4, column=3, padx=1, pady=1)

    def evento_evaluar(self):
        #Eval = Si un str contiene operadores aritmeticos o cualquier expresion que se necesite evaluar, entonces ejecuta la operacion que se contenga dentro de la cadena
        try:
            if self.expresion: #Si tenemos algun valor en la expresion
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror("Error", f"Fatal Error: {e}")
        finally:
            self.expresion = ""
    def limpiar(self):
        self.expresion = ""
        self.entrada_texto.set(self.expresion)

    def evento_click(self, elemento):  #Recibe un nuevo elemente
        #Concatenamos el nuevo elemento a la expresion existente
        self.expresion = f"{self.expresion}{elemento}" #La variable expresion ya contiene alguna informacion, entonces esa info la concatenamos al nuevo elemento que recibe
        self.entrada_texto.set(self.expresion) #Y aca por medio del metodo set se actualiza a la nueva expresion

        #Cada ves que presionamos un boton va sucediendo lo explicado de arriba

if __name__ == "__main__":
    ventana = Calculadora()
    ventana.mainloop()