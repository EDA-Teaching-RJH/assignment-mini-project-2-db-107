#stores valid passwords

import csv
import os


file_name = "password_storage.csv"
#This checks that the password file has been made/ 
# exists with the correct title and creates it if not.
def storage_check():
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["password"])


def storage_save(password):

    #Continues from "def storage_check"
    # to save passwords to the csv file.
    storage_check() #files and header - check.

    with open(file_name, "a") as file:
        writer = csv.writer(file)
        writer.writerow([password])
#Previously - writer.writerow({"password": password }) which caused
# the sotorage to save only the word "password" only.
    print("\nPassword Saved.")


def storage_list():
    #Finds the storage file - if it doesn't exist
    # it prints "No Passwords Saved" otheriwse it continues.
    storage_check() #files and header - check.
    
    passwords = []
    #reads the passwords from the csv file in a list.
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            passwords.append({"password": row["password"]}) #row by row
        
        if not passwords:
            print("\nNo Passwords Saved.")
            return #if no passwords, goes to main.
    
        print("\n- - Saved Passwords - -")
        #"x" is used because the passwords are stored as a dictionary, 
        # so x is used to give the dictionary a value.
        for item in sorted (passwords, key=lambda x: x["password"]):
            print(f"--> {item['password']}")

def storage_deleteall():
    storage_check() #files and header - check.
    passwords = []

    clear_all = input("Clear all passwords? Y/N: ").capitalize()
    if clear_all == "Y":

        print("\nClearing Passwords...")
        #re-writes the csv file as blank then tells the user
        # its been cleared.
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow({file_name: passwords})
        print("\nPasswords Cleared.")
    else:
        return
    