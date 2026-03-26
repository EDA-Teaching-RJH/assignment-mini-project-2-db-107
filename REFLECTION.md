Assignment 2 – Coding Fundamentals: 
db107 

I chose to code a password generator since it would be a good fit for the assessment requirements and my coding ability. The 3 pages needed were “main”, “checker”, and “storage”. This is because the password generator needed a main menu page for everything to link back to with different choices.  

Which are: 

Password generator 

Check password(s) - links to storage and checker to fetch and verify the information before making a decision with what to do with the data. 

View password(s) - links to storage to create (from the generator or user input), delete (all) and store passwords (in “storage_passwords.csv”) 

 

Creating the main file was quite simple compared to linking between the other 2 files since it was just creating options and linking the options with the suitable “def _____” sections with more links to the other two implemented files. With functions such as storage.storage_save to take the user to the next part of the code/ file to progress the command.  

Having clear definition labels clearly link to each file such as all the definitions in “storage” start with storage and then their function, same as in main they are all labelled with “password” and then the function then “check” and same again. 

The main area I had difficulties was getting the passwords to save, so after trying different attempts at referring to the previous classes and looking at GitHub, I eventually figured it out by creating “storage_save” and “storage_check” which checks that the csv file exists and creates it otherwise and any (password) that goes into the “storage_save” then gets written into the csv file, generated passwords are limited to 6 – 45 characters and custom passwords are any length. 

Some issues I had that were actually simple fixes were things like small typos or just moving a word or section but a larger issue I had was the actual linking between main and storage couple times throughout the code gave me an error saying it couldn't find a way to save passwords or find any of the storage file. This was an easy fix but took me while before I realised, I just had to use “import storage”, “import_checker”. 

I also had the third option where you can enter you own password and test saved, however it would then ask to save the already saved passwords causing a duplication, to solve this I re-made the save connection as its own definition instead of implemented into the checker where it would force the question with no way around. This was better for optimising the save option as it allowed me to add the save option wherever I like in the main menu file by just using: 

“if save == "Y": 

storage.storage_save(password)”. 
