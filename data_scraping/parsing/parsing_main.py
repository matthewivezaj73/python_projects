#importing libraries.
import urllib.request as req
# from bs4 import BeautifulSoup
#Creating a variable and assigning it a web page.
html = 'https://en.wikipedia.org/wiki/List_of_most_popular_websites'
# print(bs.h1)
response = req.urlopen(html)