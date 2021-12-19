#Importing the validate_music_box file. 
from classes.validate_music_box import ValidateMusic
#Instantiating the class.
new_music = ValidateMusic("Mike L", "Omega", "Sprigal")
#Creating a flag.
not_done = False
#Testing for user input.
while not not_done:
    #Asking the user to enter a choice.
    user_action = input("Enter \'a\' to add an entry.\n\nEnter \'s\' to show all entries.\n\nEnter \'e\' to edit an entry.\n\nEnter \'x\' to exit.")
    #Handling the case where the user enters a.
    if user_action.lower() == "a":
        #Creating a flag.
        not_artist = False
        #Notifying the user they will make a profile.
        print(f"Please ensure that you follow this format when creating the list:\n\n{new_music.__str__()}")
        #Testing for the artist.
        while not not_artist:
            #Asking the user for the artist name.
            artist_name = input("Please enter the artist's name: ")
            #Validating the artist name.
            not_artist = new_music.validate_artist(artist_name)
        #Adding a flag.
        not_album = False
        #Testing for the artist.
        while not not_album:
            #Asking the user for the name of the album.
            album_name = input("Please enter the artist's name: ")
            #Validating the artist name.
            not_album = new_music.validate_artist(artist_name)