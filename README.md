# Password Generator

A secure and customizable password generator written in Python.

## Features

- **Secure Randomness**: Uses the `secrets` module for cryptographically strong random numbers.
- **Custom Length**: Allows users to specify the password length (minimum 8 characters).
- **Strong Complexity**: Guarantees that every generated password contains at least:
  - One lowercase letter
  - One uppercase letter
  - One digit
  - One special character (punctuation)

## Requirements

- Python 3.6 or higher

## Usage

1. Run the script:
   ```bash
   python PasswordGenerator.py
   ```
2. Enter the desired length when prompted.
3. The generated password will be displayed in the terminal.

## Example

```text
Ingrese el tamaño de la contraseña (mínimo 8): 12
Contraseña generada: 7jB$9vQ!2p*X
```

## Security Note

This tool is intended for personal use and provides a quick way to generate strong passwords locally.
