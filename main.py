# main: password checker/ generator.
# will link to other files - collect/ correlate data.
# List options:
#   generate password (give suggestions/ asks users input what they want to include & length)
#   checks passwords (length, character, symbols, etc...) - gives a score on the strength of the password (1-10)
#   stores passwords (refer back to the storage in future searches/ retreives history)
# create a list of allowed characters, letters and numbers allowed (include upper an lower)
# limit character length
# options - generate password, check password, view passwords, delete passwords, (update passwords? - maybe), end/ terminate programme.

from unicodedata import name

import cowsay
#used the chat to install cowsay (wouldn't work without)
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
    
    #ask 
    print("\nLength of password (between 6 and 45 characters): ")
    length = int(input("Length: "))
    if length < min_length or length > max_length:
        print("Invalid Length, Y to Try Again or Q to Quit")
        
        # Gives the user a choice whether to put in another value
        # or return to the main menu.

        opt = input("Option: ").capitalize()
        if opt == "Q":
            return
        if opt == "Y":
            return password_gen()
        # generates a password using the allowed characters and the length specified by the user.

    
    
    

def password_view():
           # def storage == get_storage()
    print("...")

def password_check():
    
    print("...")

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