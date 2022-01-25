#Importing the library.
from os import read
from urllib.request import urlopen
#Assinging a variable to the path of the text file.
my_file = "text_files/site_text.txt"
#Importing class.
#Creating an instance of a class.
my_site_scraper = "https://www.google.com/"
#Reading the conents of the site.
read_site = urlopen(my_site_scraper)
#Setting a flag.

