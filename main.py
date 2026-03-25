# main: password checker/ generator.
# will link to other files - collect/ correlate data.
# List options:
#   generate password (give suggestions/ asks users input what they want to include & length)
#   checks passwords (length, character, symbols, etc...) - gives a score on the strength of the password (1-10)
#   stores passwords (refer back to the storage in future searches/ retreives history)
# create a list of allowed characters, letters and numbers allowed (include upper an lower)
# limit character length
# options - generate password, check password, view passwords, delete passwords, (update passwords? - maybe), end/ terminate programme.


import random

import cowsay

import checker

import storage



def password_gen():

    # Tells the programme what characters, letters and numbers 
    # are allowed to be used in the code generator.
    characters = "!£$%^&*()_+-={}~#][@:;'?><,./"
    numbers = "0123456789"
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    all_allowed = characters + numbers + lower + upper

    max_length = 45
    min_length = 6
    
    #Ask the user a length for the password.
    print("\nLength of password (between 6 & 45 characters): ")
    length = int(input("Length: "))

    if length < min_length or length > max_length:
        print("Invalid Length, Y to Try Again or Q to Quit")
        
        #Gives the user a choice whether to put in another value
        # or return to the main menu.

        opt = input("Option: ").capitalize()
        if opt == "Q":
            return
        if opt == "Y":
            return password_gen()
        else:
            print("\nInvalid Option")
            return
        # Generates a password using the specified list of allowed 
        # characters/ numbers and the length from the user input.

    password = ""
    for i in range(length):
        password += random.choice(all_allowed)
        #This takes the users input (length) and applies that integer
        # this is then added to the "password" with randomly selected "all_allowed"
        # variables until it reaches the users inputted length.

    # This prints the password with the given values and the users input.
    print(f"Generated Password: {password}")

    # If "Y" the password is taken to storage and saved
    # If "N" this goe sback to the main menu.
    save = input("Save Password? Y/N: ").capitalize()
    if save == "Y":
        storage.storage_save(password)
    else:
        return



def password_view():
    #choice of view functions
    print("\n- - Saved Passwords - -")
    print("\n1. View Saved")
    print("2. Clear all")
    print("3. Return to Main Menu")

    opt = input(f"Select an option between 1-3: ")

    #Opt 1 will open the file where the passwords are stored
    # and print each password in the file.
    if opt =="1":
        print("\n- - Password List - -")
        passwords = storage.list_passwords()

        # If there are no passwords no passwords will show
        # If there are then passwords will be printed in a list.
        if not passwords:
            print("No passwords saved.")
        else:
            for password in passwords:
                print(f"- {password}")
            

    elif opt == "2":
        print("\nClearing Passwords...")
        storage.clear()
        print("Passwords Cleared.")
    elif opt == "3":
        return
    else:
        print("Not an Option, Enter a Valid Option")
    
    

def password_check():
    
    print("\n- - Password Checker")
    print("\n1. Enter Password")
    print("2. Test Saved Password")
    print("3. Return to Main Menu")

    opt = input("Choose an option between 1-3: ")
    if opt == "1":
        password = input("Password: ")
        checker.check(password)
    elif opt == "2":
        storage.view()
        password = input("Password: ")
        checker.check(password)
    elif opt == "3":
        return
    else:
        print("Not an Option, Enter a Valid Option")




active = True

#runs main, asks user for name.
def main():
    print("\n- - - STARTING - - -")
    name = input("\nName: ").capitalize()

    cowsay.turtle(f"Welcome, {name}")
#ask user to input a no. from 1-4 a links that option to a definition else where.
    while True:
        print("\n-- Menu --")
        print("\n1. Generate New Password")
        print("2. View Passwords") # include delete (maybe update) options within 
        print("3. Check Password")
        print("4. Quit")

#creates links to main (definition) sections of code
#this had caused issues with the programme from running and had to add the {} to name to fix.
        opt = input(f"{name}, Please Select an Option (1-4): ")

        if opt == "1":
            password_gen()
        elif opt == "2":
            password_view()
        elif opt == "3":
            password_check()
        elif opt == "4":
            print("Shutting Down")
            break
        else:
            print("Invalid Option")

if __name__ == "__main__":
    main()



#during a test i had an issue with option 2 (view password) linking to the code of
# option 1 (password gen).
#simple mistake such as capital letters/ typos
