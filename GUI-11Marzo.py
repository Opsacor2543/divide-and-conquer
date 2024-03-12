import tkinter as tk
import csv

# FUNCION QUE EXTRAE UNA MATRIZ
def extraer_matriz():
    # VARIABLES GLOBALES
    global M, filas, columnas

    # SE OPERAN LOS VALORES PROPORCIONADOS POR EL USUARIO Y SE GENERA UNA MATRIZ ALEATORIA (BACK END)
    try:
        filas = int(entry_filas.get())
        columnas = int(entry_columnas.get())

        # ABRE CSV Y EXTRAE MATRIZ
        with open("nueva_matriz.csv", "r") as file:
            reader = csv.reader(file)
            M = [list(map(int, row)) for row in reader]

        mostrar_matriz()
    
    # MENSAJE DE ERROR
    except ValueError:
        tk.messagebox.showerror("Los datos no son válidos. Por favor intente de nuevo...")

# FUNCION QUE MUESTRA LA MATRIZ
def mostrar_matriz():
    # VARIABLES GLOBALES
    global matriz_frame

    # CREA UN FRAME PARA MOASTRAR LA MATRIZ
    if matriz_frame:
        matriz_frame.destroy()
    
    matriz_frame = tk.Frame(root)
    matriz_frame.pack(padx=10, pady=10)

    # ITERA LA MATRIZ Y SE ETIQUETA CADA ELEMENTO Y ASIGNA UN COLOR DE FONDO 
    for i in range(filas):
        for j in range(columnas):
            valor = M[i][j]
            color = ''
            if valor == 0: # CAMINO
                color = 'white'
            elif valor == 1: # PARED
                color = 'black'
            elif valor == -1: # INICIO
                color = 'gray'
            elif valor == -2: # META
                color = 'green'
            elif valor == -3: # TELETRANSPORTACION
                color = 'blue'
            elif valor == -4: # PREGUNTA
                color = 'purple'
            else: # CUALQUIER OTRO NUMERO (SIMBOLIZA UN ERROR EN LA GENERACION DE LA MATRIZ)
                color = 'red'

            # ASIGNA ETIQUETA
            tk.Label(matriz_frame, bg=color, width=2, height=1).grid(row=i, column=j)

def resuelve_laberinto():
    pass # FUNCION DEL LABERINTO (BACK END)

# CREA LA VENTANA
root = tk.Tk()
root.title("Interfaz de Usuario")

# DECLARACIONES
matriz_frame = None
filas = 0
columnas = 0
M = []

# FRAME
frame = tk.Frame(root)
frame.pack(padx=80, pady=30)

# CAMPO COLUMNAS
tk.Label(frame, text="Filas:").grid(row=0, column=0)
entry_filas = tk.Entry(frame)
entry_filas.grid(row=0, column=1)

# CAMPO FILAS
tk.Label(frame, text="Columnas:").grid(row=1, column=0)
entry_columnas = tk.Entry(frame)
entry_columnas.grid(row=1, column=1)

btn_generar = tk.Button(frame, text="GENERAR", command=extraer_matriz)
btn_generar.grid(row=2, columnspan=2, pady=10)

btn_resolver = tk.Button(frame, text="RESOLVER", command=resuelve_laberinto)
btn_resolver.grid(row=3, columnspan=2, pady=10)

root.mainloop()
