#stores valid passwords

import os
import main

file_name = "password_storage.txt"


#this is where passwords generated or inputted will be saved.
def storage_passwords():
     passwords = []

while open("passwords.txt", "r") as file:
        lines = file.readlines()
        file.write(f"{passwords}\n")

        file = open("passwords.txt", "r") as file:
        lines = file.readlines()
    
        for line in lines:
            print(line)
        return

def storage_saved():
    return