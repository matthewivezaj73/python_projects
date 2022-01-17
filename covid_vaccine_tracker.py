#Importing the library.
from urllib.request import urlopen

#Creating a variable that points to a site.
my_site = "https://data.thetimesherald.com/covid-19-vaccine-tracker/michigan/wayne-county/26163/"
#Creating a variable that grabs the text from a site.
read_site = urlopen(my_site)
#Creating a variable that reads the content.

#Reading each line on the site
for line in read_site:
    print(line)