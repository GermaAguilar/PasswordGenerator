# Password Generator

import secrets
import string
import sys

LONGITUD_MINIMA = 8


def generar_contrasena(longitud):
    """Genera una contraseña con al menos una minúscula, una mayúscula, un dígito y un símbolo."""
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Un carácter de cada categoría, para garantizar que estén todas
    contrasena = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    # Completar con caracteres aleatorios
    for _ in range(longitud - 4):
        contrasena.append(secrets.choice(caracteres))

    # Mezclar para que los primeros cuatro no queden siempre en el mismo orden
    secrets.SystemRandom().shuffle(contrasena)
    return ''.join(contrasena)


def main():
    entrada = input(f"Ingrese el tamaño de la contraseña (mínimo {LONGITUD_MINIMA}): ")

    try:
        longitud = int(entrada)
    except ValueError:
        sys.exit("Debe ingresar un número entero.")

    if longitud < LONGITUD_MINIMA:
        sys.exit(f"¡La contraseña debe tener al menos {LONGITUD_MINIMA} caracteres!")

    print(f"Contraseña generada: {generar_contrasena(longitud)}")


if __name__ == "__main__":
    main()
