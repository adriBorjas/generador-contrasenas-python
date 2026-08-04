import tkinter as tk
from utils import generador


def generar():
    pwd = generador.generar_contrasena()
    entry_var.set(pwd)


root = tk.Tk()
root.title("Generador de contraseñas")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=30, font=('Arial', 12))
entry.pack(padx=20, pady=(20,10))

btn = tk.Button(root, text="Generar contraseña", command=generar)
btn.pack(padx=20, pady=(0,20))

if __name__ == "__main__":
    root.mainloop()
