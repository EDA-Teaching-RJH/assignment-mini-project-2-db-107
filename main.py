#main: password checker/ generator.
#will link to other files - collect/ correlate data.
#List options:
#   generate password (give suggestions/ asks users input what they want to include & length)
#   checks passwords (length, character, symbols, etc...) - gives a score on the strength of the password (1-10)
#   stores passwords (refer back to the storage in future searches/ retreives history)
#create a list of allowed characters, letters and numbers allowed (include upper an lower)
#limit character length
#options - generate password, check password, view passwords, delete passwords, (update passwords? - maybe), end/ terminate programme.

import checker
import storage

active = True
def main():
    print("Welcome \nPlease Selection an option to continue")


    while True:
        print(" Please select an option from below")
        print("\n1. Generate New Password")
        print("2. View Passwords") # include delete (maybe update) options within 
        print("3. Check Password")
        print("4. Quit")

        opt = input

        if opt == "1":
            print("Below is a list of password options")
            print("Please choose one to continue")
            #
        elif opt == "2":
            def storage == get_storage()

            

        elif opt == "4":
            print("Shutting Down")
            break

        else:
            print("Invalid Option")

def main():