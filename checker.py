#checks passwords validity:
#   length, character, numbers.
#   rates the passwords strength (1-10)


def password_checker():
    length = "..."
    
    character = "..."

    number = "..."

    letter = "..."


    password_strength = length + character + number + letter

    print(f"Password Strength: {password_strength}/10")

    if password_strength < 4:
        print("Password is weak.")
    elif password_strength < 6:
        print("Password is moderate.")
    elif password_strength < 9:
        print("Password is good.")
    elif password_strength <= 10:
        print("Password is strong.")
    else:
        print("Error")

    return 