import string
import secrets


def generar_contrasena(
    longitud=12,
    incluir_mayusculas=True,
    incluir_minusculas=True,
    incluir_numeros=True,
    incluir_simbolos=True
):
    """Genera una contraseña aleatoria de longitud especificada
    compuesta por los tipos de caracteres seleccionados.
    """
    chars = ''
    if incluir_mayusculas:
        chars += string.ascii_uppercase
    if incluir_minusculas:
        chars += string.ascii_lowercase
    if incluir_numeros:
        chars += string.digits
    if incluir_simbolos:
        chars += string.punctuation

    if not chars:
        raise ValueError("Debe seleccionarse al menos una categoría de caracteres")

    return ''.join(secrets.choice(chars) for _ in range(longitud))
