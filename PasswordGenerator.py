# Password Generator

import string
import secrets

longitud = int(input("Ingrese el tamaño de la contraseña (mínimo 8): "))

# Validar longitud mínima
if longitud < 8:
    print("¡La contraseña debe tener al menos 8 caracteres!")
    exit()

caracteres = string.ascii_letters + string.digits + string.punctuation

# Generar asegurando al menos un carácter de cada categoría
while True:
    contrasena = []
    contrasena.append(secrets.choice(string.ascii_lowercase))
    contrasena.append(secrets.choice(string.ascii_uppercase))
    contrasena.append(secrets.choice(string.digits))
    contrasena.append(secrets.choice(string.punctuation))
    
    # Completar con caracteres aleatorios
    for _ in range(longitud - 4):
        contrasena.append(secrets.choice(caracteres))
    
    # Mezclar y convertir a cadena
    secrets.SystemRandom().shuffle(contrasena)
    contrasena = ''.join(contrasena)
    
    # Verificar que cumple todos los criterios
    if (any(c.islower() for c in contrasena) and
        any(c.isupper() for c in contrasena) and
        any(c.isdigit() for c in contrasena) and
        any(c in string.punctuation for c in contrasena)):
        break

print(f"Contraseña generada: {contrasena}")