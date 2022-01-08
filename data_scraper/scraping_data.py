#Importing the library.
from urllib.request import urlopen
#Setting a flag.
not_scraped = False
#Testing for input from the user.
while not not_scraped:
    #Asking for input from the user.
#Creating a variable that points to a site.
my_site = "http://olympus.realpython.org/profiles/aphrodite"
#Creating a variable that grabs the text from a site.
read_site = urlopen(my_site)
#Creating a variable that reads the content.

#Reading each line on the site
for line in read_site:
    print(line)