def evaluar_fuerza(contrasena):
    """Clasifica una contraseña en Débil, Media o Fuerte."""
    if not contrasena:
        return "Sin contraseña"

    longitud = len(contrasena)
    tiene_mayusculas = any(caracter.isupper() for caracter in contrasena)
    tiene_minusculas = any(caracter.islower() for caracter in contrasena)
    tiene_numeros = any(caracter.isdigit() for caracter in contrasena)
    tiene_simbolos = any(not caracter.isalnum() for caracter in contrasena)

    variedad = sum([
        tiene_mayusculas,
        tiene_minusculas,
        tiene_numeros,
        tiene_simbolos,
    ])

    if longitud >= 16 and variedad >= 3:
        return "Fuerte"
    if longitud >= 12 and variedad >= 2:
        return "Media"
    return "Débil"
