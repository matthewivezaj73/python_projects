#Importing the library.
from os import read
from urllib.request import urlopen
#Assinging a variable to the path of the text file.
my_file = "text_files/site_text.txt"
#Importing class.
#Creating an instance of a class.
#Reading the conents of the site.
read_site = urlopen("https://hellopoetry.com/poem/1830922/five-little-flowers/")
website_arr = []
for line in read_site:
    line = str(line).replace("b'","")

print(line)

