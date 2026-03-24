# main: password checker/ generator.
# will link to other files - collect/ correlate data.
# List options:
#   generate password (give suggestions/ asks users input what they want to include & length)
#   checks passwords (length, character, symbols, etc...) - gives a score on the strength of the password (1-10)
#   stores passwords (refer back to the storage in future searches/ retreives history)
# create a list of allowed characters, letters and numbers allowed (include upper an lower)
# limit character length
# options - generate password, check password, view passwords, delete passwords, (update passwords? - maybe), end/ terminate programme.

import cowsay
import checker
import storage



def password_gen():

    # tells the programme what characters, letters and numbers 
    # are allowed to be used in the code generator.
    characters = "!£$%^&*()_+-={}~#][@:;'?><,./"
    numbers = "0123456789"
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    all_allowed = characters + numbers + lower + upper

    max_length = 45
    min_length = 6
    
    #ask 
    print("Below is a list of password options")
    
    

def password_view():
           # def storage == get_storage()
    print("...")

def password_check():
    
    print("...")

active = True

#runs main, asks user for name.
def main():
    print("- - - STARTING - - -")
    name = input("\nName: ").capitalize()

    
    cowsay.spaceship("Welcome, {name}")
#ask user to input a no. from 1-4 a links that option to a definition else where.
    while True:
        print("-- Menu --")
        print("\n1. Generate New Password")
        print("2. View Passwords") # include delete (maybe update) options within 
        print("3. Check Password")
        print("4. Quit")

#creates links to main (definition) sections of code
#this had 
        opt = input(f"{name}, Please select an option (1-4): ")

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