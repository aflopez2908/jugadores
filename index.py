
import tkinter as tk
from tkinter import ttk

class Jugador:
    def __init__(self, name, last_name, number):

        #personal information
        self.number = int(number)
        self.last_name = last_name
        self.name = name

        #rebounds information
        self.offensive_rebound= 0
        self.defensive_rebound=0

        #fauls information
        self.technical_faul=0
        self.personal_foul=0

        #2 points information
        self.two_points_goal= 0
        self.two_points_failed=0

        #three points information
        self.three_points_goal= 0
        self.three_points_failed=0

        #free trow information
        self.freetrow_goal=0
        self.freetrow_failed = 0

        #defensive information
        self.block=0
        self.steals=0

        #lost information
        self.lost_balls=0

        #attaking information
        self.attendance=0


jugadores=[]

def agregar_jugador():
    last_name = entry_last_name.get()
    number= entry_number.get()
    name= entry_nombre.get()

    jugador = Jugador(name, last_name, number)

    jugadores.append(jugador)

    # Limpiar los campos de entrada
    entry_nombre.delete(0, tk.END)
    entry_number.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    mostrar_estadisticas()

def mostrar_estadisticas():
    # Eliminar los registros anteriores de la tabla
    for row in treeview.get_children():
        treeview.delete(row)

    # Mostrar los jugadores y sus estadísticas en la tabla
    for jugador in jugadores:
        row = (jugador.name,jugador.last_name, jugador.number)
        treeview.insert("", tk.END, values=row)


def abrir_nueva_ventana():
    nueva_ventana = tk.Toplevel(window)
    nueva_ventana.title("Nueva Ventana")

    # Agregar contenido a la nueva ventana
    label = tk.Label(nueva_ventana, text="¡Esta es una nueva ventana!")
    label.pack()

def tiro_libre_anotado():

    numero=int(input("numero"))

    for i in jugadores:
        if numero==i.number:
            print(i)








window = tk.Tk()
window.title("Estadísticas de Jugadores")


columns = ("Nombre","Apellido", "Número", "Faltas", "Rebote ofensivo","rebote defensivo","tiro 2 anotado", "Asistencias")
treeview = ttk.Treeview(window, columns=columns, show="headings")
for col in columns:
    treeview.heading(col, text=col)

treeview.pack()

#configuracion de una scrollbar
scrollbar = ttk.Scrollbar(window, orient="horizontal", command=treeview.xview)
scrollbar.pack(side="bottom", fill="x")

# Configurar la tabla para utilizar el scrollbar horizontal
treeview.configure(xscrollcommand=scrollbar.set)

# Agregar el scrollbar horizontal a la tabla
treeview.configure(yscrollcommand=scrollbar.set)
treeview.configure(xscrollcommand=scrollbar.set)
scrollbar.configure(command=treeview.xview)


# Campo de entrada del nombre
label_nombre = tk.Label(window, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(window)
entry_nombre.pack()

# Campo de entrada del apellido
label_last_name = tk.Label(window, text="Apellido:")
label_last_name.pack()
entry_last_name = tk.Entry(window)
entry_last_name.pack()

#campo entrada del numero
label_number = tk.Label(window, text="Número:")
label_number.pack()
entry_number = tk.Entry(window)
entry_number.pack()

# Crear el botón para agregar jugadores
button_agregar = tk.Button(window, text="Agregar Jugador", command=agregar_jugador)
button_agregar.pack()

button_tiro_libre_anotado = tk.Button(window, text="Tiro libre anotado", command=abrir_nueva_ventana)
button_tiro_libre_anotado.pack()





window.mainloop()


