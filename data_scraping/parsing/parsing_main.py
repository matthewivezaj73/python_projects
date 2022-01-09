#importing libraries.
from urllib.request import urlopen
from bs4 import BeautifulSoup
#Creating a variable and assigning it a web page.
html = urlopen('http://www.pythonscraping.com/pages/page1.html')