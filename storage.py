#stores valid passwords

import csv
import main

def save(password):
    with open(file_name, "a") as file:
        writer = csv.DictWriter(fieldnames=["password"])
        writer.writerow({"password": password })




file_name = "password_storage.csv"

#this checks that the password file has been made/ 
# exists and makes a file if not.
def storage_check():
    

#this is where passwords generated or inputted will be saved.
def storage_passwords():
     passwords = main.password_gen()

def storage_saved():
    return


