import random
import string
import pyperclip # type: ignore

def generate_password(length, use_upper=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Demander les pr�f�rences � l'utilisateur
length = int(input("Entrez la longueur du mot de passe : "))
use_upper = input("Inclure des lettres majuscules ? (y/n) ").lower() == 'y'
use_digits = input("Inclure des chiffres ? (y/n) ").lower() == 'y'
use_special = input("Inclure des caract�res sp�ciaux ? (y/n) ").lower() == 'y'

# G�n�rer le mot de passe
password = generate_password(length, use_upper, use_digits, use_special)
print(f"Mot de passe g�n�r� : {password}")

# Copier dans le presse-papiers (optionnel)
pyperclip.copy(password)
print("Mot de passe copi� dans le presse-papiers !")

