#Importing the library.
from urllib.request import urlopen
#Setting a flag.
not_scraped = False
#Testing for input from the user.
while not not_scraped:
    #Setting a flag.
    not_site_entered = False
    #Asking for input from the user.
    site_entered = input("Please enter the name of a site whose data you would like scaped: ")
    #Testing to ensure the data is ok.
    while not not_site_entered:
#Creating a variable that points to a site.
my_site = "http://olympus.realpython.org/profiles/aphrodite"
#Creating a variable that grabs the text from a site.
read_site = urlopen(my_site)
#Creating a variable that reads the content.

#Reading each line on the site
for line in read_site:
    print(line)