#Importing the validate_music_box file. 
from classes.validate_music_box import ValidateMusic
#Creating a flag.
not_done = False
#Testing for user input.
while not not_done:
    #Asking the user to enter a choice.
    user_action = input("Enter \'a\' to add an entry.\n\nEnter \'s\' to show all entries.\n\nEnter \'e\' to edit an entry.\n\n")