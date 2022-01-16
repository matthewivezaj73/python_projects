#Importing the library.
from os import read
from urllib.request import urlopen
#Assinging a variable to the path of the text file.
my_file = "text_files/site_text.txt"
#Creating an instance of a class.
my_site_scraper = urlopen("https://en.wikipedia.org/wiki/Flower",23)
#Setting a flag.
not_scraped = False
#Testing for input from the user.
for line in my_site_scraper:
    print(line)