# Generador de contraseñas con Python

Aplicación de escritorio desarrollada en Python como proyecto formativo del módulo 6 (M6T3) del curso de Python de Tokio School.

Permite generar contraseñas personalizadas, consultar una estimación básica de su fuerza y copiar o guardar los resultados.

## Funcionalidades

- Generar una contraseña o crear varias de una vez (entre 5 y 10).
- Elegir la longitud de la contraseña (entre 8 y 64 caracteres).
- Seleccionar los tipos de caracteres: mayúsculas, minúsculas, números y símbolos.
- Evitar caracteres ambiguos, como `0`, `O`, `o`, `I`, `l` y `1`.
- Excluir caracteres específicos indicados por el usuario.
- Consultar una clasificación orientativa de fuerza: débil, media o fuerte.
- Copiar una contraseña o todas las generadas al portapapeles.
- Guardar una o varias contraseñas en un archivo de texto local.
- Consultar un resumen de las opciones utilizadas.

## Tecnologías

- Python 3.
- Tkinter para la interfaz gráfica.
- Módulos de la biblioteca estándar: `secrets`, `string`, `datetime` y `pathlib`.

El proyecto no necesita instalar dependencias externas. Tkinter debe estar disponible en la instalación de Python.

## Requisitos

- Python 3 instalado.
- Tkinter disponible.

## Cómo ejecutar el proyecto

1. Clona este repositorio o descarga el código.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta:

```bash
python main.py
```

En algunos sistemas puede ser necesario utilizar `python3 main.py`.

## Estructura del proyecto

```text
generador-contrasenas-python/
├── main.py
├── requirements.txt
└── utils/
    ├── __init__.py
    ├── archivo.py
    ├── fuerza.py
    └── generador.py
```

- `main.py`: crea la interfaz gráfica y coordina las acciones del usuario.
- `utils/generador.py`: contiene la lógica de generación de contraseñas.
- `utils/fuerza.py`: realiza la clasificación orientativa de fuerza.
- `utils/archivo.py`: gestiona el guardado de contraseñas en un archivo de texto.
- `contraseñas_guardadas.txt`: se crea localmente cuando se guardan contraseñas desde la aplicación. Está excluido del repositorio mediante `.gitignore` y no se sube a GitHub.

## Consideraciones de seguridad

La generación utiliza el módulo `secrets` de Python para seleccionar caracteres aleatoriamente. Sin embargo, las contraseñas que se guardan desde la aplicación se escriben en texto plano en `contraseñas_guardadas.txt`, sin cifrado. No utilices esa opción para almacenar contraseñas reales o sensibles.

La clasificación de fuerza es una comprobación sencilla basada en la longitud y la variedad de caracteres; no constituye una auditoría de seguridad.

## Contexto

Proyecto realizado con fines formativos como ejercicio práctico de Python y desarrollo de una interfaz gráfica con Tkinter.
