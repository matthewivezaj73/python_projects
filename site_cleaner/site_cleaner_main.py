#Importing the library.
from os import read
from urllib.request import urlopen
#Assinging a variable to the path of the text file.
my_file = "text_files/site_text.txt"
#Importing class.
from classes.scraping_validator import ScrapingValidator
#Creating an instance of a class.
my_site_scraper = ScrapingValidator("https://www.google.com/",23)
#Setting a flag.

