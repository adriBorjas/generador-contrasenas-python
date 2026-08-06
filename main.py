import tkinter as tk
from utils import generador


def generar():
    longitud = int(longitud_var.get())
    pwd = generador.generar_contrasena(
        longitud,
        incluir_mayusculas=mayusculas_var.get(),
        incluir_minusculas=minusculas_var.get(),
        incluir_numeros=numeros_var.get(),
        incluir_simbolos=simbolos_var.get()
    )
    entry_var.set(pwd)


root = tk.Tk()
root.title("Generador de contraseñas")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=30, font=('Arial', 12))
entry.pack(padx=20, pady=(20, 10))

longitud_var = tk.IntVar(value=12)
longitud_label = tk.Label(root, text="Longitud de la contraseña:")
longitud_label.pack(padx=20, pady=(0, 5))
spinbox_longitud = tk.Spinbox(root, from_=8, to=64, textvariable=longitud_var, width=5)
spinbox_longitud.pack(padx=20, pady=(0, 15))

mayusculas_var = tk.BooleanVar(value=True)
minusculas_var = tk.BooleanVar(value=True)
numeros_var = tk.BooleanVar(value=True)
simbolos_var = tk.BooleanVar(value=True)

def comprobar_opciones():
    """Habilita el botón si al menos una categoría está seleccionada; lo deshabilita en caso contrario."""
    if any([
        mayusculas_var.get(),
        minusculas_var.get(),
        numeros_var.get(),
        simbolos_var.get()
    ]):
        btn.config(state='normal')
    else:
        btn.config(state='disabled')

checkbox_frame = tk.Frame(root)
checkbox_frame.pack(padx=20, pady=(0, 15), anchor='w')

check_mayusculas = tk.Checkbutton(checkbox_frame, text="Mayúsculas", variable=mayusculas_var, command=comprobar_opciones)
check_mayusculas.grid(row=0, column=0, sticky='w')
check_minusculas = tk.Checkbutton(checkbox_frame, text="Minúsculas", variable=minusculas_var, command=comprobar_opciones)
check_minusculas.grid(row=0, column=1, sticky='w', padx=(10, 0))
check_numeros = tk.Checkbutton(checkbox_frame, text="Números", variable=numeros_var, command=comprobar_opciones)
check_numeros.grid(row=1, column=0, sticky='w')
check_simbolos = tk.Checkbutton(checkbox_frame, text="Símbolos", variable=simbolos_var, command=comprobar_opciones)
check_simbolos.grid(row=1, column=1, sticky='w', padx=(10, 0))

btn = tk.Button(root, text="Generar contraseña", command=generar)
btn.pack(padx=20, pady=(0, 20))

# Establecer el estado inicial del botón según las opciones por defecto
comprobar_opciones()

if __name__ == "__main__":
    root.mainloop()
