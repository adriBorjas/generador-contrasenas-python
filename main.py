import tkinter as tk
from utils import generador


def generar():
    longitud = int(longitud_var.get())
    pwd = generador.generar_contrasena(longitud)
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

btn = tk.Button(root, text="Generar contraseña", command=generar)
btn.pack(padx=20, pady=(0, 20))

if __name__ == "__main__":
    root.mainloop()
