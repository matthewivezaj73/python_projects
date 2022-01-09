#Importing the library.
from urllib.request import urlopen
#Assinging a variable to the path of the text file.
my_file = "/text_files/site_text.txt"
#Importing class.
from classes.scraping_validator import ScrapingValidator
#Creating an instance of a class.
my_site_scraper = ScrapingValidator("https://www.google.com/",23)
#Setting a flag.
not_scraped = False
#Testing for input from the user.
while not not_scraped:
    #Printing a message to the user.
    #Setting a flag.
    not_site_entered = False
    #Testing to ensure the data is ok.
    while not not_site_entered:
        #Asking for input from the user.
        site_entered = input("Please enter the name of a site whose data you would like scaped: ")
        #Grabbing content from the site.
        site_entered = my_site_scraper.validateSite(site_entered)
        #Validating the site_entered variable.
        not_site_entered = my_site_scraper.validateSite(site_entered)
    #Opening a file.
#Creating a variable that points to a site.
my_site = "http://olympus.realpython.org/profiles/aphrodite"
#Creating a variable that grabs the text from a site.
read_site = urlopen(my_site)
#Creating a variable that reads the content.

#Reading each line on the site
for line in read_site:
    print(line)