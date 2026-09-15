import string
import secrets


def generar_contrasena(
    longitud=12,
    incluir_mayusculas=True,
    incluir_minusculas=True,
    incluir_numeros=True,
    incluir_simbolos=True,
    evitar_ambiguos=False,
    excluir_caracteres=''
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

    caracteres_ambiguos = '0OoIl1'
    caracteres_excluidos = set(excluir_caracteres or '')
    if evitar_ambiguos:
        caracteres_excluidos.update(caracteres_ambiguos)
    chars = ''.join(char for char in chars if char not in caracteres_excluidos)

    if not chars:
        raise ValueError("Las exclusiones eliminan todos los caracteres disponibles")

    return ''.join(secrets.choice(chars) for _ in range(longitud))


def generar_varias_contrasenas(
    cantidad,
    longitud=12,
    incluir_mayusculas=True,
    incluir_minusculas=True,
    incluir_numeros=True,
    incluir_simbolos=True,
    evitar_ambiguos=False,
    excluir_caracteres=''
):
    """Genera entre 5 y 10 contraseñas reutilizando generar_contrasena()."""
    if isinstance(cantidad, bool) or not isinstance(cantidad, int) or not 5 <= cantidad <= 10:
        raise ValueError("La cantidad debe ser un número entero entre 5 y 10")

    return [
        generar_contrasena(
            longitud,
            incluir_mayusculas,
            incluir_minusculas,
            incluir_numeros,
            incluir_simbolos,
            evitar_ambiguos=evitar_ambiguos,
            excluir_caracteres=excluir_caracteres
        )
        for _ in range(cantidad)
    ]
