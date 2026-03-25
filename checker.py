# checks passwords validity:
#   length, character, numbers.
#   rates the passwords strength (1-10)


def password_checker(password):
    score = 0

    # Adds a score to the legth of the password
    if len(password) > 6 and len(password) < 18:
        score += 2
    if len(password) > 18 and len(password) <= 45:
        score += 2

    # Adds a score to any LETTERS used in the password
    if any(x in password for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        score += 2
    if any(x in password for x in "abcdefghijklmnopqrstuvwxyz"):
        score += 2

    # Adds a score to any NUMBERS used in the password
    if any(x in password for x in "0123456789"):
        score += 2

    # Adds a score to any SYMBOLS used in the password
    if any(x in password for x in "!£$%^&*()_+-={}~#][@:;'?><,./"):
        score += 2

    print(f"\nPassword Strength: {score}/10")
    #Scores the password based on the peramiters above - adds each score
    # to give an overall.
    if score < 4:
        print("Password is weak.")
    elif score < 6:
        print("Password is moderate.")
    elif score < 9:
        print("Password is good.")
    elif score <= 10:
        print("Password is strong.")
    else:
        print("Error")

    return 