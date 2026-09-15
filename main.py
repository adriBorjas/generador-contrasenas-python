import tkinter as tk
import tkinter.messagebox as messagebox
from utils import archivo, generador, fuerza


def generar():
    longitud = validar_longitud()
    try:
        pwd = generador.generar_contrasena(
            longitud,
            incluir_mayusculas=mayusculas_var.get(),
            incluir_minusculas=minusculas_var.get(),
            incluir_numeros=numeros_var.get(),
            incluir_simbolos=simbolos_var.get(),
            evitar_ambiguos=evitar_ambiguos_var.get(),
            excluir_caracteres=excluir_caracteres_var.get()
        )
    except ValueError as error:
        messagebox.showerror("Generar contraseña", str(error))
        return
    entry_var.set(pwd)
    actualizar_indicador_fuerza(pwd)
    actualizar_resumen(1)
    # Habilitar los botones de copia y guardado sólo si se ha generado una contraseña
    if pwd:
        copy_btn.config(state='normal')
        save_btn.config(state='normal')


def generar_varias():
    cantidad = validar_cantidad()
    longitud = validar_longitud()
    try:
        contrasenas = generador.generar_varias_contrasenas(
            cantidad,
            longitud,
            incluir_mayusculas=mayusculas_var.get(),
            incluir_minusculas=minusculas_var.get(),
            incluir_numeros=numeros_var.get(),
            incluir_simbolos=simbolos_var.get(),
            evitar_ambiguos=evitar_ambiguos_var.get(),
            excluir_caracteres=excluir_caracteres_var.get()
        )
    except ValueError as error:
        messagebox.showerror("Generar varias contraseñas", str(error))
        return
    lista_contrasenas.delete(0, tk.END)
    for contrasena in contrasenas:
        lista_contrasenas.insert(tk.END, contrasena)
    actualizar_resumen(len(contrasenas))
    copiar_varias_btn.config(state='normal')
    guardar_varias_btn.config(state='normal')


def actualizar_indicador_fuerza(contrasena):
    fuerza_texto = fuerza.evaluar_fuerza(contrasena)
    fuerza_var.set(fuerza_texto)


def copiar_contrasena():
    contrasena = entry_var.get()
    if contrasena:
        root.clipboard_clear()
        root.clipboard_append(contrasena)
        messagebox.showinfo("Copiar contraseña", "Contraseña copiada al portapapeles.")


def guardar_contrasena():
    contrasena = entry_var.get()
    if contrasena:
        try:
            archivo.guardar_contrasena_en_archivo(contrasena)
        except OSError:
            messagebox.showerror("Guardar contraseña", "No se ha podido guardar la contraseña.")
        else:
            messagebox.showinfo("Guardar contraseña", "Contraseña guardada correctamente.")


def obtener_contrasenas_mostradas():
    return list(lista_contrasenas.get(0, tk.END))


def copiar_varias_contrasenas():
    contrasenas = obtener_contrasenas_mostradas()
    if contrasenas:
        root.clipboard_clear()
        root.clipboard_append("\n".join(contrasenas))
        messagebox.showinfo("Copiar contraseñas", "Contraseñas copiadas al portapapeles.")


def guardar_varias_contrasenas():
    contrasenas = obtener_contrasenas_mostradas()
    if contrasenas:
        try:
            archivo.guardar_varias_contrasenas(contrasenas)
        except OSError:
            messagebox.showerror("Guardar contraseñas", "No se han podido guardar las contraseñas.")
        else:
            messagebox.showinfo("Guardar contraseñas", "Contraseñas guardadas correctamente.")


def validar_longitud():
    valor = spinbox_longitud.get()
    try:
        longitud = int(valor)
    except (ValueError, TypeError):
        longitud = 12

    if longitud < 8:
        longitud = 8
    elif longitud > 64:
        longitud = 64

    longitud_var.set(longitud)
    return longitud


def validar_cantidad():
    valor = spinbox_cantidad.get()
    try:
        cantidad = int(valor)
    except (ValueError, TypeError):
        cantidad = 5

    if cantidad < 5:
        cantidad = 5
    elif cantidad > 10:
        cantidad = 10

    cantidad_var.set(cantidad)
    return cantidad


def actualizar_resumen(cantidad_generada):
    categorias = []
    if mayusculas_var.get():
        categorias.append("Mayúsculas")
    if minusculas_var.get():
        categorias.append("Minúsculas")
    if numeros_var.get():
        categorias.append("Números")
    if simbolos_var.get():
        categorias.append("Símbolos")

    resumen_var.set(
        f"Longitud: {longitud_var.get()}\n"
        f"Contraseñas generadas: {cantidad_generada}\n"
        f"Categorías: {', '.join(categorias) or 'Ninguna'}\n"
        f"Evitar ambiguos: {'Sí' if evitar_ambiguos_var.get() else 'No'}\n"
        f"Caracteres excluidos: {excluir_caracteres_var.get() or 'Ninguno'}"
    )

root = tk.Tk()
root.title("Generador de contraseñas")

resumen_var = tk.StringVar()

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=30, font=('Arial', 12))
entry.pack(padx=20, pady=(20, 10))

fuerza_var = tk.StringVar(value="Sin contraseña")
fuerza_label = tk.Label(root, textvariable=fuerza_var, font=('Arial', 10))
fuerza_label.pack(padx=20, pady=(0, 10))

longitud_var = tk.IntVar(value=12)

longitud_label = tk.Label(root, text="Longitud de la contraseña:")
longitud_label.pack(padx=20, pady=(0, 5))
spinbox_longitud = tk.Spinbox(root, from_=8, to=64, textvariable=longitud_var, width=5)
spinbox_longitud.pack(padx=20, pady=(0, 15))

cantidad_var = tk.IntVar(value=5)

cantidad_label = tk.Label(root, text="Cantidad de contraseñas:")
cantidad_label.pack(padx=20, pady=(0, 5))
spinbox_cantidad = tk.Spinbox(root, from_=5, to=10, textvariable=cantidad_var, width=5)
spinbox_cantidad.pack(padx=20, pady=(0, 15))

evitar_ambiguos_var = tk.BooleanVar(value=False)
evitar_ambiguos_check = tk.Checkbutton(
    root,
    text="Evitar caracteres ambiguos (0, O)",
    variable=evitar_ambiguos_var
)
evitar_ambiguos_check.pack(padx=20, pady=(0, 5), anchor='w')

excluir_caracteres_var = tk.StringVar()
excluir_caracteres_label = tk.Label(root, text="Caracteres a excluir:")
excluir_caracteres_label.pack(padx=20, pady=(0, 5), anchor='w')
excluir_caracteres_entry = tk.Entry(root, textvariable=excluir_caracteres_var, width=30)
excluir_caracteres_entry.pack(padx=20, pady=(0, 15))

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
        varias_btn.config(state='normal')
    else:
        btn.config(state='disabled')
        varias_btn.config(state='disabled')

def crear_checkbutton(frame, text, variable, row, column, padx=(0, 0)):
    check = tk.Checkbutton(frame, text=text, variable=variable, command=comprobar_opciones)
    check.grid(row=row, column=column, sticky='w', padx=padx)
    return check

checkbox_frame = tk.Frame(root)
checkbox_frame.pack(padx=20, pady=(0, 15), anchor='w')

check_mayusculas = crear_checkbutton(checkbox_frame, "Mayúsculas", mayusculas_var, 0, 0)
check_minusculas = crear_checkbutton(checkbox_frame, "Minúsculas", minusculas_var, 0, 1, padx=(10, 0))
check_numeros = crear_checkbutton(checkbox_frame, "Números", numeros_var, 1, 0)
check_simbolos = crear_checkbutton(checkbox_frame, "Símbolos", simbolos_var, 1, 1, padx=(10, 0))

btn = tk.Button(root, text="Generar contraseña", command=generar)
btn.pack(padx=20, pady=(0, 10))

varias_btn = tk.Button(root, text="Generar varias contraseñas", command=generar_varias)
varias_btn.pack(padx=20, pady=(0, 10))

lista_contrasenas = tk.Listbox(root, width=30, height=6)
lista_contrasenas.pack(padx=20, pady=(0, 15))

resumen_frame = tk.LabelFrame(root, text="Resumen")
resumen_frame.pack(padx=20, pady=(0, 15), fill='x')
resumen_label = tk.Label(
    resumen_frame,
    textvariable=resumen_var,
    justify='left',
    anchor='w'
)
resumen_label.pack(padx=10, pady=10, anchor='w')

copiar_varias_btn = tk.Button(
    root,
    text="Copiar todas las contraseñas",
    command=copiar_varias_contrasenas,
    state='disabled'
)
copiar_varias_btn.pack(padx=20, pady=(0, 10))

guardar_varias_btn = tk.Button(
    root,
    text="Guardar todas las contraseñas",
    command=guardar_varias_contrasenas,
    state='disabled'
)
guardar_varias_btn.pack(padx=20, pady=(0, 10))

copy_btn = tk.Button(root, text="Copiar contraseña", command=copiar_contrasena, state='disabled')
copy_btn.pack(padx=20, pady=(0, 10))

save_btn = tk.Button(root, text="Guardar contraseña", command=guardar_contrasena, state='disabled')
save_btn.pack(padx=20, pady=(0, 20))

# Establecer el estado inicial del botón según las opciones por defecto
comprobar_opciones()
actualizar_resumen(0)

if __name__ == "__main__":
    root.mainloop()
