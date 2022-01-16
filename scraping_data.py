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
