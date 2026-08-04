import string
import secrets


def generar_contrasena():
    """Genera una contraseña aleatoria de exactamente 12 caracteres
    compuesta únicamente por letras (mayúsculas y minúsculas) y números.
    """
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(12))
