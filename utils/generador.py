import string
import secrets


def generar_contrasena(longitud=12):
    """Genera una contraseña aleatoria de longitud especificada
    compuesta únicamente por letras (mayúsculas y minúsculas) y números.
    """
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(longitud))
