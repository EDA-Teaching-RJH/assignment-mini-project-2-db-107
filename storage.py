#stores valid passwords

import csv
import os
import main

file_name = "password_storage.csv"

#this checks that the password file has been made/ 
# exists and makes a file if not.
def storage_check():
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["password"])


def storage_save(password):

    #Continues from "def storage_check"
    storage_check()

    with open(file_name, "a") as file:
        writer = csv.writer(file)
        writer.writerow([password])
#Previously - writer.writerow({"password": password }) which caused
# the sotorage to save only the word "password" only.
    print("\nPassword Saved.")



#def storage_saved():
    return