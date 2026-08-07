from datetime import datetime
from pathlib import Path


def obtener_ruta_archivo():
    return Path(__file__).resolve().parent.parent / "contraseñas_guardadas.txt"


def guardar_contrasena_en_archivo(contrasena, ruta=None):
    """Guarda una contraseña y su fecha de guardado en un archivo .txt."""
    if ruta is None:
        ruta = obtener_ruta_archivo()
    else:
        ruta = Path(ruta)

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    contenido = f"Fecha y hora: {fecha_hora}\nContraseña: {contrasena}\n\n"

    with ruta.open("a", encoding="utf-8") as archivo:
        archivo.write(contenido)
