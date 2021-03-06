#Importing the library.
from os import read
from urllib.request import urlopen
#Assinging a variable to the path of the text file.
my_file = "text_files/site_text.txt"
#Created a flag.
not_done = False
#Starting a while loop.
while not not_done:
    #Asking the user for the name of a site they would like scraped.
    enter_site = input("Please enter the full url of a site that you would like scraped: ")
    #Added a try block
    try:
        #Handling the case where the user enters a site.
        if len(enter_site) >= 1:
            #Creating an instance of a class.
            urlopen(enter_site)
    except:
        print(f"Sorry, but we can't connect to \'{enter_site}\', please try again")
    #Asking the user what they would like to do with the scraped data.
    user_choice = input("Enter \'S\' if you would like to save the site that you scraped onto a file.")
